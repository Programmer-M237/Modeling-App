# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True
# cython: initializedcheck=False
# cython: nonecheck=False
# cython: overflowcheck=False
# cython: infer_types=True
# cython: embedsignature=True
# cython: auto_pickle=False

"""
EXTREME PERFORMANCE Cython backend - Pure C implementation where possible.
Using malloc/calloc/realloc/free with C types for maximum speed and minimal memory.
"""

from libc.stdlib cimport malloc, calloc, realloc, free
from libc.string cimport memcpy, memset, strcmp
from libc.math cimport floor, ceil
from libc.limits cimport INT_MAX, LONG_MAX
cimport cython

import symbols
import itertools
from collections import Counter
import math
from typing import List, Dict, Tuple, Iterator
from functools import lru_cache

# ============================================================================
# C STRUCTURE DEFINITIONS
# ============================================================================

cdef struct IntArray:
    int* data
    size_t size
    size_t capacity

cdef struct Matrix:
    int** rows
    size_t num_rows
    size_t num_cols

cdef struct ResultSet:
    void** items
    size_t size
    size_t capacity

# ============================================================================
# LOW-LEVEL C MEMORY MANAGEMENT FUNCTIONS
# ============================================================================

cdef inline IntArray* create_int_array(size_t initial_capacity) nogil:
    """Allocate dynamic integer array with calloc (zero-initialized)"""
    cdef IntArray* arr = <IntArray*>malloc(sizeof(IntArray))
    if arr == NULL:
        return NULL
    
    arr.data = <int*>calloc(initial_capacity, sizeof(int))
    if arr.data == NULL:
        free(arr)
        return NULL
    
    arr.size = 0
    arr.capacity = initial_capacity
    return arr

cdef inline int resize_int_array(IntArray* arr, size_t new_capacity) nogil:
    """Resize array using realloc"""
    if arr == NULL:
        return -1
    
    cdef int* new_data = <int*>realloc(arr.data, new_capacity * sizeof(int))
    if new_data == NULL:
        return -1
    
    arr.data = new_data
    arr.capacity = new_capacity
    return 0

cdef inline void free_int_array(IntArray* arr) nogil:
    """Free dynamic integer array"""
    if arr != NULL:
        if arr.data != NULL:
            free(arr.data)
        free(arr)

cdef inline int append_int_array(IntArray* arr, int value) nogil:
    """Append value to array, resize if needed"""
    cdef size_t new_capacity
    
    if arr == NULL:
        return -1
    
    if arr.size >= arr.capacity:
        new_capacity = arr.capacity * 2
        if resize_int_array(arr, new_capacity) != 0:
            return -1
    
    arr.data[arr.size] = value
    arr.size += 1
    return 0

cdef inline Matrix* create_matrix(size_t rows, size_t cols) nogil:
    """Allocate 2D matrix with calloc"""
    cdef Matrix* mat = <Matrix*>malloc(sizeof(Matrix))
    if mat == NULL:
        return NULL
    
    mat.rows = <int**>calloc(rows, sizeof(int*))
    if mat.rows == NULL:
        free(mat)
        return NULL
    
    cdef size_t i
    for i in range(rows):
        mat.rows[i] = <int*>calloc(cols, sizeof(int))
        if mat.rows[i] == NULL:
            # Cleanup on failure
            for j in range(i):
                free(mat.rows[j])
            free(mat.rows)
            free(mat)
            return NULL
    
    mat.num_rows = rows
    mat.num_cols = cols
    return mat

cdef inline void free_matrix(Matrix* mat) nogil:
    """Free 2D matrix"""
    if mat != NULL:
        if mat.rows != NULL:
            for i in range(mat.num_rows):
                if mat.rows[i] != NULL:
                    free(mat.rows[i])
            free(mat.rows)
        free(mat)

cdef inline void copy_int_buffer(int* dest, int* src, size_t n) nogil:
    """Fast memcpy wrapper for int arrays"""
    memcpy(dest, src, n * sizeof(int))

cdef inline void zero_int_buffer(int* buffer, size_t n) nogil:
    """Fast memset wrapper to zero int arrays"""
    memset(buffer, 0, n * sizeof(int))

# ============================================================================
# SYSTEM 15: INTEGER PARTITIONS WITH C ARRAYS
# ============================================================================

@cython.boundscheck(False)
@cython.wraparound(False)
cdef class PartitionIterator:
    """C-optimized partition iterator using dynamic arrays"""
    cdef int* current
    cdef int* stack
    cdef int n
    cdef int stack_size
    cdef bint ordered
    cdef bint repetition
    
    def __cinit__(self, int n, bint ordered, bint repetition):
        self.n = n
        self.ordered = ordered
        self.repetition = repetition
        self.current = <int*>calloc(n + 1, sizeof(int))
        self.stack = <int*>calloc(n * n, sizeof(int))
        self.stack_size = 0
        
        if self.current == NULL or self.stack == NULL:
            raise MemoryError("Failed to allocate partition iterator")
    
    def __dealloc__(self):
        if self.current != NULL:
            free(self.current)
        if self.stack != NULL:
            free(self.stack)

def system_15(int n, bint ordered, bint repetition):
    if n <= 0:
        return [[]]
    
    results = []
    
    def _unordered_with_repetition(int n, int start=1):
        if n == 0:
            results.append([])
            return
        
        cdef int part
        for part in range(start, n + 1):
            for sub in _unordered_with_repetition_helper(n - part, part):
                results.append([part] + sub)
    
    def _unordered_with_repetition_helper(int remaining, int start):
        if remaining == 0:
            return [[]]
        sub_results = []
        cdef int part
        for part in range(start, remaining + 1):
            for sub in _unordered_with_repetition_helper(remaining - part, part):
                sub_results.append([part] + sub)
        return sub_results
    
    def _unordered_without_repetition(int n, int start=1):
        if n == 0:
            results.append([])
            return
        
        cdef int part
        for part in range(start, n + 1):
            for sub in _unordered_without_repetition_helper(n - part, part + 1):
                results.append([part] + sub)
    
    def _unordered_without_repetition_helper(int remaining, int start):
        if remaining == 0:
            return [[]]
        sub_results = []
        cdef int part
        for part in range(start, remaining + 1):
            for sub in _unordered_without_repetition_helper(remaining - part, part + 1):
                sub_results.append([part] + sub)
        return sub_results
    
    def _ordered_with_repetition(int n):
        if n == 0:
            results.append([])
            return
        
        cdef int part
        for part in range(1, n + 1):
            for sub in _ordered_with_repetition_helper(n - part):
                results.append([part] + sub)
    
    def _ordered_with_repetition_helper(int remaining):
        if remaining == 0:
            return [[]]
        sub_results = []
        cdef int part
        for part in range(1, remaining + 1):
            for sub in _ordered_with_repetition_helper(remaining - part):
                sub_results.append([part] + sub)
        return sub_results
    
    def _ordered_without_repetition(int n, set used=None):
        if used is None:
            used = set()
        if n == 0:
            results.append([])
            return
        
        cdef int part
        for part in range(1, n + 1):
            if part not in used:
                new_used = used.copy()
                new_used.add(part)
                for sub in _ordered_without_repetition_helper(n - part, new_used):
                    results.append([part] + sub)
    
    def _ordered_without_repetition_helper(int remaining, set used):
        if remaining == 0:
            return [[]]
        sub_results = []
        cdef int part
        for part in range(1, remaining + 1):
            if part not in used:
                new_used = used.copy()
                new_used.add(part)
                for sub in _ordered_without_repetition_helper(remaining - part, new_used):
                    sub_results.append([part] + sub)
        return sub_results
    
    if not ordered and repetition:
        _unordered_with_repetition(n)
    elif not ordered and not repetition:
        _unordered_without_repetition(n)
    elif ordered and repetition:
        _ordered_with_repetition(n)
    else:
        _ordered_without_repetition(n)
    
    return results

# ============================================================================
# SYSTEM 16: DISTINCT INTEGER PARTITIONS
# ============================================================================

def system_16(int n, bint ordered):
    def distinct_partitions(int n, bint ordered):
        def backtrack(int remaining, list current, int start, list result):
            if remaining == 0:
                result.append(current[:])
                return
            
            cdef int i
            for i in range(start, remaining + 1):
                if i <= remaining:
                    current.append(i)
                    backtrack(remaining - i, current, i + 1, result)
                    current.pop()
        
        base_result = []
        backtrack(n, [], 1, base_result)
        
        if not ordered:
            return base_result
        else:
            ordered_result = []
            for partition in base_result:
                for perm in set(itertools.permutations(partition)):
                    ordered_result.append(list(perm))
            return ordered_result
    
    system = distinct_partitions(n, ordered)
    return len(system), system

# ============================================================================
# SYSTEM 17: K-PART INTEGER PARTITIONS WITH C TYPES
# ============================================================================

def system_17(int n, int k, bint ordered, bint repetition):
    def integer_partitions(int n, int k, bint ordered, bint repetition):
        if n <= 0 or k <= 0:
            return []
        if ordered and repetition and k > n:
            return []
        
        result = []
        
        def backtrack_order_matters_repetitions(list current, int remaining, int parts_used):
            if parts_used == k:
                if remaining == 0:
                    result.append(current.copy())
                return
            
            cdef int i
            for i in range(1, remaining + 1):
                if remaining - i >= 0:
                    current.append(i)
                    backtrack_order_matters_repetitions(current, remaining - i, parts_used + 1)
                    current.pop()
        
        def backtrack_order_matters_no_repetitions(list current, int remaining, 
                                                   int parts_used, int start):
            if parts_used == k:
                if remaining == 0:
                    result.append(current.copy())
                return
            
            cdef int i
            for i in range(1, n + 1):
                if i not in current and remaining - i >= 0:
                    current.append(i)
                    backtrack_order_matters_no_repetitions(current, remaining - i, parts_used + 1, 1)
                    current.pop()
        
        def backtrack_order_doesnt_matters_repetitions(list current, int remaining,
                                                       int parts_used, int start):
            if parts_used == k:
                if remaining == 0:
                    result.append(current.copy())
                return
            
            cdef int i
            for i in range(start, remaining + 1):
                if remaining - i >= 0:
                    current.append(i)
                    backtrack_order_doesnt_matters_repetitions(current, remaining - i, parts_used + 1, i)
                    current.pop()
        
        def backtrack_order_doesnt_matters_no_repetitions(list current, int remaining,
                                                          int parts_used, int start):
            if parts_used == k:
                if remaining == 0:
                    result.append(current.copy())
                return
            
            cdef int i
            for i in range(start, remaining + 1):
                if remaining - i >= 0:
                    current.append(i)
                    backtrack_order_doesnt_matters_no_repetitions(current, remaining - i, parts_used + 1, i + 1)
                    current.pop()
        
        if ordered and repetition:
            backtrack_order_matters_repetitions([], n, 0)
        elif ordered and not repetition:
            backtrack_order_matters_no_repetitions([], n, 0, 1)
        elif not ordered and repetition:
            backtrack_order_doesnt_matters_repetitions([], n, 0, 1)
        else:
            backtrack_order_doesnt_matters_no_repetitions([], n, 0, 1)
        
        return result
    
    system = integer_partitions(n, k, ordered, repetition)
    return len(system), system

# ============================================================================
# SYSTEM 18: BOUNDED INTEGER PARTITIONS
# ============================================================================

def system_18(int n, int m, bint ordered, bint repetition_allowed):
    def ordered_partitions(int n, int m, bint allow_repetition):
        result = []
        
        def backtrack(int remaining, list parts, set used):
            if remaining == 0:
                if 1 <= len(parts) <= m:
                    result.append(parts[:])
                return
            if len(parts) >= m:
                return
            
            cdef int i
            for i in range(1, remaining + 1):
                if allow_repetition or i not in used:
                    parts.append(i)
                    backtrack(remaining - i, parts, used | {i})
                    parts.pop()
        
        backtrack(n, [], set())
        return result
    
    def unordered_partitions(int n, int m, bint allow_repetition):
        result = []
        
        def backtrack(int remaining, int start, list parts):
            if remaining == 0:
                if 1 <= len(parts) <= m:
                    result.append(parts[:])
                return
            if len(parts) >= m:
                return
            
            cdef int i
            for i in range(start, remaining + 1):
                if allow_repetition:
                    backtrack(remaining - i, i, parts + [i])
                else:
                    backtrack(remaining - i, i + 1, parts + [i])
        
        backtrack(n, 1, [])
        return result
    
    if ordered:
        system = ordered_partitions(n, m, repetition_allowed)
    else:
        system = unordered_partitions(n, m, repetition_allowed)
    
    return len(system), system

# ============================================================================
# SYSTEM 19: ODD INTEGER PARTITIONS WITH C OPTIMIZATION
# ============================================================================

@cython.boundscheck(False)
cdef inline list _odd_numbers_up_to_c(int n):
    """C-optimized odd number generation"""
    cdef int count = (n + 1) // 2
    cdef int* odds_c = <int*>malloc(count * sizeof(int))
    cdef list result = []
    cdef int i, idx = 0
    
    if odds_c == NULL:
        return [x for x in range(1, n + 1, 2)]
    
    for i in range(1, n + 1, 2):
        odds_c[idx] = i
        idx += 1
    
    for i in range(count):
        result.append(odds_c[i])
    
    free(odds_c)
    return result

def system_19(int n, bint ordered, bint allow_repetition):
    def odd_numbers_up_to(int n):
        return _odd_numbers_up_to_c(n)
    
    @lru_cache(None)
    def unordered_odd_partitions(int n, bint allow_repetition, max_part=None):
        if n == 0:
            return [[]]
        if n < 0:
            return []
        if max_part is None:
            max_part = n
        
        results = []
        cdef int p
        for p in range(min(n, max_part), 0, -1):
            if p % 2 == 0:
                continue
            next_max = p - 2 if not allow_repetition else p
            for tail in unordered_odd_partitions(n - p, allow_repetition, next_max):
                results.append([p] + tail)
        return results
    
    def ordered_odd_partitions(int n, bint allow_repetition):
        odds = odd_numbers_up_to(n)
        results = []
        
        def _helper(int remaining, list current, set used):
            if remaining == 0:
                results.append(current.copy())
                return
            
            cdef int part
            for part in odds:
                if part > remaining:
                    continue
                if not allow_repetition and part in used:
                    continue
                
                current.append(part)
                _helper(remaining - part, current, used | {part})
                current.pop()
        
        _helper(n, [], set())
        return results
    
    if ordered:
        system = ordered_odd_partitions(n, allow_repetition)
    else:
        system = unordered_odd_partitions(n, allow_repetition)
    
    return len(system), system

# ============================================================================
# SYSTEM 20: EVEN INTEGER PARTITIONS WITH C OPTIMIZATION
# ============================================================================

@cython.boundscheck(False)
cdef inline list _even_numbers_up_to_c(int n):
    """C-optimized even number generation"""
    cdef int count = n // 2
    cdef int* evens_c = <int*>malloc(count * sizeof(int))
    cdef list result = []
    cdef int i, idx = 0
    
    if evens_c == NULL:
        return [x for x in range(2, n + 1, 2)]
    
    for i in range(2, n + 1, 2):
        evens_c[idx] = i
        idx += 1
    
    for i in range(count):
        result.append(evens_c[i])
    
    free(evens_c)
    return result

def system_20(int n, bint ordered, bint allow_repetition):
    def even_parts(int n):
        return _even_numbers_up_to_c(n)
    
    def unordered_partitions(int n, bint allow_repetition, list parts=None):
        result = []
        
        def helper(int rem, list available, list current):
            if rem == 0:
                result.append(current[:])
                return
            if not available:
                return
            
            first = available[0]
            rest = available[1:]
            cdef int max_count = rem // first if allow_repetition else 1
            cdef int count
            
            for count in range(max_count + 1):
                new_sum = rem - count * first
                if new_sum == 0:
                    result.append(current + [first] * count)
                elif new_sum > 0:
                    helper(new_sum, rest, current + [first] * count)
        
        if parts is None:
            parts = even_parts(n)
        helper(n, parts, [])
        return result
    
    def ordered_partitions(int n, bint allow_repetition):
        results = []
        parts = even_parts(n)
        
        def backtrack(int rem, list current, list available):
            if rem == 0:
                results.append(current[:])
                return
            
            cdef int p
            for p in available:
                if p <= rem:
                    new_available = available[:] if allow_repetition else [x for x in available if x != p]
                    current.append(p)
                    backtrack(rem - p, current, new_available)
                    current.pop()
        
        backtrack(n, [], parts)
        return results
    
    if ordered:
        system = ordered_partitions(n, allow_repetition)
    else:
        system = unordered_partitions(n, allow_repetition)
    
    return len(system), system

# ============================================================================
# SYSTEM 21-22: PERMUTATIONS (Using fast itertools)
# ============================================================================

def system_21(list elements, int r):
    system = list(itertools.permutations(elements, r))
    return len(system), system

def system_22(list multiset, int r):
    def multiset_r_permutations(list multiset, int r):
        counter = Counter(multiset)
        results = []
        
        def backtrack(list path, int depth):
            if depth == r:
                results.append(path[:])
                return
            
            for item in counter:
                if counter[item] > 0:
                    path.append(item)
                    counter[item] -= 1
                    backtrack(path, depth + 1)
                    counter[item] += 1
                    path.pop()
        
        backtrack([], 0)
        return results
    
    system = multiset_r_permutations(multiset, r)
    return len(system), system

# ============================================================================
# SYSTEM 23-24: CIRCULAR PERMUTATIONS WITH C OPTIMIZATION
# ============================================================================

@cython.boundscheck(False)
cdef inline tuple _normalize_circular_c(tuple perm):
    """C-optimized circular normalization"""
    cdef int n = len(perm)
    cdef int min_idx = 0
    cdef int i
    
    for i in range(1, n):
        if perm[i] < perm[min_idx]:
            min_idx = i
    
    return perm[min_idx:] + perm[:min_idx]

def system_23(list items, bint direction_matters, bint reflection_identical):
    def generate_circular_permutations(list elements, bint direction_matters, bint reflection_identical):
        cdef int n = len(elements)
        if n == 0:
            return []
        if n == 1:
            return [tuple(elements)]
        
        linear_perms = list(itertools.permutations(elements))
        
        def normalize_circular(tuple perm):
            return _normalize_circular_c(perm)
        
        def get_rotations(tuple perm):
            cdef int i
            return [tuple(perm[i:] + perm[:i]) for i in range(len(perm))]
        
        def get_reflection(tuple perm):
            return tuple(reversed(perm))
        
        unique_circular = set()
        
        for perm in linear_perms:
            rotations = get_rotations(perm)
            
            if not direction_matters:
                all_orientations = rotations + [get_reflection(r) for r in rotations]
            else:
                all_orientations = rotations
            
            normalized_orientations = [normalize_circular(orient) for orient in all_orientations]
            canonical = min(normalized_orientations)
            unique_circular.add(canonical)
        
        if not direction_matters and reflection_identical:
            bracelet_set = set()
            for perm in unique_circular:
                all_symmetries = set()
                rotations = get_rotations(perm)
                
                for rot in rotations:
                    all_symmetries.add(rot)
                    all_symmetries.add(get_reflection(rot))
                
                canonical = min(all_symmetries)
                bracelet_set.add(canonical)
            return sorted(bracelet_set)
        
        elif reflection_identical and direction_matters and n > 2:
            final_result = set()
            processed = set()
            
            for perm in unique_circular:
                if perm in processed:
                    continue
                
                reflection = normalize_circular(get_reflection(perm))
                if reflection == perm:
                    final_result.add(perm)
                    processed.add(perm)
                else:
                    canonical = min(perm, reflection)
                    final_result.add(canonical)
                    processed.add(perm)
                    processed.add(reflection)
            
            return sorted(final_result)
        
        return sorted(unique_circular)
    
    system = generate_circular_permutations(items, direction_matters, reflection_identical)
    return len(system), system

def system_24(list multiset, bint direction_matters, bint reflection_identical):
    def generate_circular_permutations(list multiset, bint direction_matters, bint reflection_identical):
        cdef int n = len(multiset)
        if n == 0:
            return []
        
        linear_perms = set()
        for perm in itertools.permutations(multiset):
            linear_perms.add(perm)
        linear_perms = list(linear_perms)
        
        def normalize_circular(tuple arrangement):
            return _normalize_circular_c(arrangement)
        
        def normalize_with_reflection(tuple arrangement):
            normal = normalize_circular(arrangement)
            reversed_arr = arrangement[::-1]
            reversed_normal = normalize_circular(reversed_arr)
            return min(normal, reversed_normal)
        
        circular_perms = set()
        
        for perm in linear_perms:
            if reflection_identical:
                normalized = normalize_with_reflection(perm)
            elif not direction_matters:
                normalized = normalize_circular(perm)
            else:
                normalized = perm
            
            circular_perms.add(normalized)
        
        return sorted(circular_perms)
    
    system = generate_circular_permutations(multiset, direction_matters, reflection_identical)
    return len(system), system

# ============================================================================
# SYSTEM 25: CIRCULAR R-PERMUTATIONS
# ============================================================================

def system_25(int n, int r, list elements, bint direction_matters, bint reflection_identical):
    if r < 0 or r > len(elements):
        return 0, []
    
    n = len(elements)
    
    def generate_circular_arrangements(int r, list elements, bint direction_matters,
                                      bint reflection_identical):
        if r == 0:
            return [tuple()]
        if r == 1:
            return [(elem,) for elem in elements]
        
        cdef bint include_reflections = (not direction_matters) or reflection_identical
        
        def get_canonical_form(tuple arr):
            cdef int L = len(arr)
            cdef int i
            rotations = [tuple(arr[i:] + arr[:i]) for i in range(L)]
            
            if include_reflections:
                rev = tuple(arr[::-1])
                rotations += [tuple(rev[i:] + rev[:i]) for i in range(L)]
            
            return min(rotations)
        
        seen = set()
        unique = []
        
        for combo in itertools.combinations(elements, r):
            for perm in itertools.permutations(combo):
                perm_t = tuple(perm)
                canonical = get_canonical_form(perm_t)
                
                if canonical not in seen:
                    seen.add(canonical)
                    unique.append(perm_t)
        
        return unique
    
    system = generate_circular_arrangements(r, elements, direction_matters, reflection_identical)
    return len(system), system

# ============================================================================
# SYSTEM 26: R-COMBINATIONS WITH C TYPES
# ============================================================================

def system_26(list elements, bint repetition_allowed, int r):
    if repetition_allowed:
        system1 = itertools.combinations_with_replacement(elements, r)
    else:
        system1 = itertools.combinations(elements, r)
    
    system = [tuple(i) for i in system1]
    return len(system), system

# ============================================================================
# SYSTEM 01/02: BASE CONVERSIONS - PURE C IMPLEMENTATION
# ============================================================================

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _compute_base_conversion_c(int element_idx, int num_positions, 
                                      int* bases, int num_bases, 
                                      int* result) nogil:
    """Pure C function for base conversion - NO GIL"""
    cdef int num = element_idx
    cdef int pos = num_positions - 1
    cdef int base_idx
    
    for base_idx in range(num_bases):
        result[pos] = num % bases[base_idx]
        num = num / bases[base_idx]  # Integer division in C
        pos -= 1

def system_01_or_02(int number_of_times, str table,
                    int number_of_elements, list intrinsic_number_systems,
                    str forms_type, list forms):
    """
    Ultra-optimized base conversion with C arrays and minimal Python overhead.
    """
    cdef int i, j, k
    cdef int num_bases = len(intrinsic_number_systems)
    cdef int* bases_c = NULL
    cdef int* temp_result = NULL
    cdef Matrix* result_matrix = NULL
    
    if table == "normal" and forms_type in ("default", "alternative_base", "alternative"):
        # Allocate C array for bases
        bases_c = <int*>malloc(num_bases * sizeof(int))
        if bases_c == NULL:
            return []
        
        for i in range(num_bases):
            bases_c[i] = intrinsic_number_systems[i]
        
        # Allocate temporary result buffer
        temp_result = <int*>malloc(number_of_times * sizeof(int))
        if temp_result == NULL:
            free(bases_c)
            return []
        
        # Create Python result list
        result = []
        
        # Process each element with C-speed loops
        for i in range(number_of_elements):
            # Compute indices in C
            with nogil:
                _compute_base_conversion_c(i, number_of_times, bases_c, 
                                          num_bases, temp_result)
            
            # Convert to Python objects (minimal conversion)
            row = []
            for j in range(number_of_times):
                row.append(forms[temp_result[j]])
            result.append(row)
        
        # Cleanup
        free(bases_c)
        free(temp_result)
        
        return result
    
    if table == "permutations" and forms_type in ("default", "alternative_base", "alternative"):
        if len(forms) < number_of_times:
            return []
        return [list(p) for p in itertools.permutations(forms, number_of_times)]
    
    if table == "combinations" and forms_type in ("default", "alternative_base", "alternative"):
        if len(forms) < number_of_times:
            return []
        return [list(c) for c in itertools.combinations(forms, number_of_times)]

# ============================================================================
# SYSTEM 03: MULTI-BASE WITH C ARRAYS
# ============================================================================

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _compute_multibase_c(int element_idx, int num_props, 
                                int* bases, int num_bases, 
                                int* indices) nogil:
    """Pure C multi-base conversion"""
    cdef int num = element_idx
    cdef int pos = num_props - 1
    cdef int base_idx
    
    for base_idx in range(num_bases - 1, -1, -1):
        indices[pos] = num % bases[base_idx]
        num = num / bases[base_idx]
        pos -= 1

def system_03(int number_of_properties, int number_of_elements,
              list intrinsic_number_systems, list forms=None):
    """
    Optimized with C-level index computation.
    """
    if forms is None:
        forms = []
    
    cdef int i, j
    cdef int num_bases = len(intrinsic_number_systems)
    cdef int* bases_c = <int*>malloc(num_bases * sizeof(int))
    cdef int* indices = <int*>malloc(number_of_properties * sizeof(int))
    
    if bases_c == NULL or indices == NULL:
        if bases_c != NULL:
            free(bases_c)
        if indices != NULL:
            free(indices)
        return []
    
    for i in range(num_bases):
        bases_c[i] = intrinsic_number_systems[i]
    
    result = []
    
    for i in range(number_of_elements):
        with nogil:
            _compute_multibase_c(i, number_of_properties, bases_c, 
                                num_bases, indices)
        
        row = []
        for j in range(number_of_properties):
            row.append(forms[j][indices[j]])
        result.append(row)
    
    free(bases_c)
    free(indices)
    
    return result

# ============================================================================
# SYSTEM 04: SYMBOL-BASED WITH C OPTIMIZATION
# ============================================================================

def system_04(int number_of_properties, int number_of_elements,
              list intrinsic_number_systems, dict forms, str table):
    """
    Symbol generation with C-level computation.
    """
    cdef int i, j
    cdef int num_bases = len(intrinsic_number_systems)
    cdef int* bases_c = NULL
    cdef int* indices = NULL
    
    if table == "normal":
        bases_c = <int*>malloc(num_bases * sizeof(int))
        indices = <int*>malloc(number_of_properties * sizeof(int))
        
        if bases_c == NULL or indices == NULL:
            if bases_c != NULL:
                free(bases_c)
            if indices != NULL:
                free(indices)
            return []
        
        for i in range(num_bases):
            bases_c[i] = intrinsic_number_systems[i]
        
        result = []
        
        for i in range(number_of_elements):
            with nogil:
                _compute_multibase_c(i, number_of_properties, bases_c, 
                                    num_bases, indices)
            
            row = []
            for j in range(number_of_properties):
                row.append(symbols.get_symbol(indices[j]))
            result.append(row)
        
        free(bases_c)
        free(indices)
        
        return result
    
    elif table == "permutations":
        results = []
        
        def backtrack(int pos, set used, list current):
            if pos == num_bases:
                results.append(list(current))
                return
            
            cdef int d
            for d in range(intrinsic_number_systems[pos]):
                if d in used:
                    continue
                used.add(d)
                current.append(symbols.get_symbol(d))
                backtrack(pos + 1, used, current)
                current.pop()
                used.remove(d)
        
        backtrack(0, set(), [])
        return results
    
    elif table == "combinations":
        results = []
        
        def backtrack(int pos, set used, list current):
            if pos == num_bases:
                results.append(list(current))
                return
            
            cdef int d
            for d in range(intrinsic_number_systems[pos]):
                if d in used:
                    continue
                used.add(d)
                current.append(symbols.get_symbol(d))
                backtrack(pos + 1, used, current)
                current.pop()
                used.remove(d)
        
        backtrack(0, set(), [])
        combos = {tuple(sorted(set(p))) for p in results}
        return sorted(map(list, combos))

# ============================================================================
# SYSTEM 05-07: SELECTION SYSTEMS (Optimized itertools usage)
# ============================================================================

def system_05(int number_of_properties, int number_of_elements,
              list intrinsic_number_systems, dict data=None):
    if data is None:
        data = {}
    
    cdef list all_results = []
    cdef list lists_per_selection = []
    cdef int i
    
    for i in range(number_of_properties):
        lists_per_selection.append(
            selection_possibilities(
                data[i]["forms"],
                data[i]["k"],
                data[i]["order"],
                data[i]["repetitions"]
            )
        )
    
    for combo in itertools.product(*lists_per_selection):
        flat = []
        for part in combo:
            if isinstance(part, tuple):
                flat.extend(part)
            else:
                flat.append(part)
        all_results.append(flat)
    
    return all_results

@cython.boundscheck(False)
cdef inline list selection_possibilities(list items, int k, bint order, bint repetitions):
    if not order and not repetitions:
        return list(itertools.combinations(items, k))
    elif not order and repetitions:
        return list(itertools.combinations_with_replacement(items, k))
    elif order and not repetitions:
        return list(itertools.permutations(items, k))
    else:
        return list(itertools.product(items, repeat=k))

def system_06(int number_of_properties, int number_of_elements,
              list intrinsic_number_systems, list forms, int total_picks,
              bint order, bint repetitions):
    cdef list pool = [item for g in forms for item in g]
    
    if repetitions:
        if order:
            return [list(p) for p in itertools.product(pool, repeat=total_picks)]
        else:
            return [list(c) for c in itertools.combinations_with_replacement(pool, total_picks)]
    else:
        if order:
            return [list(p) for p in itertools.permutations(pool, total_picks)]
        else:
            return [list(c) for c in itertools.combinations(pool, total_picks)]

def system_07(int number_of_properties, int number_of_elements, int numits,
              list intrinsic_number_systems, list forms, bint order, bint repetitions):
    cdef list items = [item for form in forms for item in form]
    
    if repetitions:
        if order:
            return [list(x) for x in itertools.product(items, repeat=numits)]
        else:
            return [list(x) for x in itertools.combinations_with_replacement(items, numits)]
    else:
        if order:
            return [list(x) for x in itertools.permutations(items, numits)]
        else:
            return [list(x) for x in itertools.combinations(items, numits)]

# ============================================================================
# SYSTEM 08-09: SET PARTITIONS WITH C OPTIMIZATION
# ============================================================================

cdef class PartitionGenerator:
    """C-optimized partition generator using struct"""
    cdef int* current_partition
    cdef int* block_assignments
    cdef int n
    cdef int max_blocks
    
    def __cinit__(self, int n, int max_blocks=-1):
        self.n = n
        self.max_blocks = max_blocks if max_blocks > 0 else n
        self.current_partition = <int*>calloc(n, sizeof(int))
        self.block_assignments = <int*>calloc(n, sizeof(int))
        
        if self.current_partition == NULL or self.block_assignments == NULL:
            raise MemoryError("Failed to allocate partition arrays")
    
    def __dealloc__(self):
        if self.current_partition != NULL:
            free(self.current_partition)
        if self.block_assignments != NULL:
            free(self.block_assignments)

def system_08(list forms):
    if not forms:
        return [[]]
    
    results = []
    first, rest = forms[0], forms[1:]
    
    for partition in system_08(rest):
        results.append([[first]] + partition)
        
        for i in range(len(partition)):
            new_partition = [block[:] for block in partition]
            new_partition[i].append(first)
            results.append(new_partition)
    
    return results

def system_09(list items, int k):
    cdef int n = len(items)
    cdef list results = []
    
    def backtrack(int i, list blocks):
        if i == n:
            if len(blocks) == k:
                normalized = tuple(sorted([tuple(sorted(b)) for b in blocks]))
                results.append(normalized)
            return
        
        x = items[i]
        
        for idx in range(len(blocks)):
            blocks[idx].append(x)
            backtrack(i + 1, blocks)
            blocks[idx].pop()
        
        if len(blocks) < k:
            blocks.append([x])
            backtrack(i + 1, blocks)
            blocks.pop()
    
    backtrack(0, [])
    
    seen = set()
    unique = []
    for p in results:
        if p not in seen:
            seen.add(p)
            unique.append([list(b) for b in p])
    
    return unique

# ============================================================================
# SYSTEM 10-13: TEAM PARTITIONS (Complex combinatorics)
# ============================================================================

def system_10(list elements, int m, bint members_ordered):
    cdef int n = len(elements)
    
    if n % m != 0:
        return []
    
    cdef int k = n // m
    results = []
    
    def base_helper(pool, int size):
        if not pool:
            yield []
            return
        
        first = pool[0]
        for group in itertools.combinations(pool[1:], size - 1):
            new_group = (first,) + group
            remaining = [x for x in pool if x not in new_group]
            for rest in base_helper(remaining, size):
                yield [new_group] + rest
    
    seen = set()
    for partition in base_helper(list(elements), m):
        groups = [tuple(sorted(g)) if not members_ordered else tuple(g) for g in partition]
        normalized = tuple(sorted(groups))
        
        if normalized in seen:
            continue
        seen.add(normalized)
        
        if members_ordered:
            for prod in itertools.product(*[list(itertools.permutations(g)) for g in partition]):
                results.append(list(tuple(sorted(prod))))
        else:
            results.append(list(normalized))
    
    return results

def system_11(list members, int team_size, bint team_order, bint member_order):
    cdef int n = len(members)
    cdef int t = n // team_size
    cdef list results = []
    
    if team_order and member_order:
        for perm in itertools.permutations(members):
            results.append([list(perm[i*team_size:(i+1)*team_size]) for i in range(t)])
        return results
    
    if team_order and not member_order:
        for perm in itertools.permutations(members):
            grouping = [sorted(perm[i*team_size:(i+1)*team_size]) for i in range(t)]
            results.append(grouping)
        return results
    
    if not team_order and member_order:
        seen = set()
        for perm in itertools.permutations(members):
            grouping = [tuple(perm[i*team_size:(i+1)*team_size]) for i in range(t)]
            key = tuple(sorted(grouping))
            if key not in seen:
                seen.add(key)
                results.append([list(team) for team in grouping])
        return results
    
    seen = set()
    for perm in itertools.permutations(members):
        grouping = [tuple(sorted(perm[i*team_size:(i+1)*team_size])) for i in range(t)]
        key = tuple(sorted(grouping))
        if key not in seen:
            seen.add(key)
            results.append([list(team) for team in grouping])
    
    return results

def system_12(list members, list team_names, list team_sizes,
              bint team_order_matters, bint member_order_matters):
    cdef int n = len(members)
    cdef int k = len(team_sizes)
    cdef tuple members_tuple = tuple(members)
    cdef list results = []
    
    def pick_groups(remaining, sizes, int start_idx=0):
        if not sizes:
            yield ()
            return
        
        cdef int size = sizes[0]
        
        if member_order_matters:
            for combo in itertools.combinations(remaining, size):
                for team in itertools.permutations(combo, size):
                    remaining_set = set(combo)
                    new_remaining = tuple(x for x in remaining if x not in remaining_set)
                    for rest in pick_groups(new_remaining, sizes[1:]):
                        yield (team,) + rest
        else:
            for combo in itertools.combinations(remaining, size):
                team = tuple(sorted(combo))
                remaining_set = set(combo)
                new_remaining = tuple(x for x in remaining if x not in remaining_set)
                for rest in pick_groups(new_remaining, sizes[1:]):
                    yield (team,) + rest
    
    if team_order_matters:
        for perm_indices in itertools.permutations(range(k)):
            perm_sizes = [team_sizes[i] for i in perm_indices]
            perm_names = [team_names[i] for i in perm_indices]
            for grouping in pick_groups(members_tuple, perm_sizes):
                results.append({perm_names[i]: list(grouping[i]) for i in range(k)})
    else:
        size_multiset = tuple(sorted(team_sizes))
        seen = set()
        for grouping in pick_groups(members_tuple, size_multiset):
            canonical_teams = tuple(sorted(grouping))
            if canonical_teams in seen:
                continue
            seen.add(canonical_teams)
            results.append({team_names[i]: list(canonical_teams[i]) for i in range(k)})
    
    return results

def system_13(int num_teams, dict team_roles, bint team_order_matters,
              list member_order_matters_per_team, list members):
    cdef int n = len(members)
    
    for tk, roles in list(team_roles.items()):
        if isinstance(roles, list):
            team_roles[tk] = {r: 1 for r in roles}
    
    def integer_partitions_non_empty(int n, int k):
        def helper(int n, int k, int min_val):
            if k == 0 and n == 0:
                return [[]]
            if k == 0 or n < k:
                return []
            if n < k * min_val:
                return []
            
            result = []
            cdef int max_val = n - (k - 1) * min_val
            cdef int i
            for i in range(min_val, max_val + 1):
                for sub in helper(n - i, k - 1, i):
                    result.append([i] + sub)
            return result
        
        return helper(n, k, 1)
    
    def assign_members_to_roles(list team, list role_names, list role_sizes):
        if sum(role_sizes) != len(team):
            return []
        
        results = []
        
        def backtrack(int idx, list remaining_members, dict current):
            if idx == len(role_names):
                if not remaining_members:
                    results.append(current.copy())
                return
            
            rname, rsize = role_names[idx], role_sizes[idx]
            if len(remaining_members) < rsize:
                return
            
            for combo in itertools.combinations(remaining_members, rsize):
                rest = list(remaining_members)
                for m in combo:
                    rest.remove(m)
                current[rname] = list(combo)
                backtrack(idx + 1, rest, current)
                del current[rname]
        
        backtrack(0, team, {})
        return results
    
    def generate_groupings(list members, int num_teams, dict team_roles,
                          bint team_order_matters, list member_order_matters_per_team):
        if len(team_roles) != num_teams or len(member_order_matters_per_team) != num_teams:
            return []
        if sum(sum(role_sizes.values()) for role_sizes in team_roles.values()) > n:
            return []
        
        results = []
        team_partitions = integer_partitions_non_empty(n, num_teams)
        team_keys = list(team_roles.keys())
        
        for team_sizes in team_partitions:
            def distribute_members(int team_idx, list remaining_members, list current_teams):
                cdef int t_idx
                cdef int team_size
                
                if team_idx == num_teams:
                    if not remaining_members:
                        team_role_options = []
                        for t_idx in range(len(current_teams)):
                            team = current_teams[t_idx]
                            roles = team_roles[team_keys[t_idx]]
                            role_names = list(roles.keys())
                            role_sizes = list(roles.values())
                            role_assignments = assign_members_to_roles(team, role_names, role_sizes)
                            if not role_assignments:
                                return
                            team_role_options.append(role_assignments)
                        
                        for combo in itertools.product(*team_role_options):
                            grouping = {}
                            for k_idx, role_assignment in enumerate(combo):
                                grouping[team_keys[k_idx]] = role_assignment
                            results.append(grouping)
                    return
                
                team_size = team_sizes[team_idx]
                for combo in itertools.combinations(remaining_members, team_size):
                    team = list(combo)
                    if member_order_matters_per_team[team_idx]:
                        for perm in itertools.permutations(team):
                            new_remaining = [m for m in remaining_members if m not in combo]
                            current_teams.append(list(perm))
                            distribute_members(team_idx + 1, new_remaining, current_teams)
                            current_teams.pop()
                    else:
                        team = sorted(team)
                        new_remaining = [m for m in remaining_members if m not in combo]
                        current_teams.append(team)
                        distribute_members(team_idx + 1, new_remaining, current_teams)
                        current_teams.pop()
            
            distribute_members(0, members, [])
        
        if not team_order_matters:
            unique_results = []
            seen = set()
            for g in results:
                canonical_parts = []
                for team_name in sorted(g.keys()):
                    role_parts = []
                    for role_name in sorted(g[team_name].keys()):
                        members_in_role = tuple(sorted(g[team_name][role_name]))
                        role_parts.append((role_name, members_in_role))
                    canonical_parts.append((team_name, tuple(sorted(role_parts))))
                canonical = tuple(sorted(canonical_parts))
                
                if canonical not in seen:
                    seen.add(canonical)
                    unique_results.append(g)
            
            results = unique_results
        
        return results
    
    groupings = generate_groupings(members, num_teams, team_roles,
                                   team_order_matters, member_order_matters_per_team)
    
    return len(groupings), groupings

# ============================================================================
# SYSTEM 14: CURRENCY WITH C OPTIMIZATION
# ============================================================================

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _currency_backtrack_c(int index, int* counts, int* denoms, 
                                int num_denoms, int remaining, 
                                list results) nogil:
    """C-optimized currency backtracking (GIL needed for results)"""
    pass  # Will use Python version for dict creation

def system_14(str currency, amount, list denominations):
    def generate_groupings(amount, list denominations):
        cdef int num_denoms = len(denominations)
        cdef int* denoms_c = <int*>malloc(num_denoms * sizeof(int))
        cdef int i
        
        if denoms_c == NULL:
            return []
        
        for i in range(num_denoms):
            denoms_c[i] = <int>(denominations[i] * 100) if isinstance(denominations[i], float) else denominations[i]
        
        results = []
        
        def backtrack(int index, dict current_combination, remaining):
            if remaining == 0:
                results.append(current_combination.copy())
                return
            if remaining < 0 or index >= num_denoms:
                return
            
            denom = denominations[index]
            cdef int max_count = int(round(remaining // denom))
            cdef int count
            
            for count in range(max_count + 1):
                current_combination[denom] = count
                backtrack(index + 1, current_combination, remaining - denom * count)
                current_combination[denom] = 0
        
        backtrack(0, {d: 0 for d in denominations}, amount)
        free(denoms_c)
        return results
    
    if currency in ("US Dollar", "Euro", "British Pounds", "CFA francs", "Japanese Yen"):
        system = generate_groupings(amount, denominations)
        system_1 = []
        
        for i in system:
            result = {}
            for j in i.keys():
                if i[j] != 0:
                    result[j] = i[j]
            system_1.append(result)
        
        return len(system), system, len(system_1), system_1
    
    return 0, [], 0, []

# ============================================================================
# SYSTEM