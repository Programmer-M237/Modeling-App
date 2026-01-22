from itertools import permutations

def system_01(int number_of_elements, intrinsic_number_systems, forms, bint repetition_allowed):
    """
    Generate a number system representation.
    
    Args:
        number_of_elements: Number of elements to generate
        intrinsic_number_systems: List of bases for each position
        forms: List of symbols/forms to use
        repetition_allowed: If True, use mixed-radix; if False, use permutations
    
    Returns:
        List of lists representing the number system
    """
    cdef int length = len(intrinsic_number_systems)
    cdef int i, j, remainder, num, divisor
    cdef list systems_list = list(intrinsic_number_systems)
    cdef list number_system
    
    if repetition_allowed:
        number_system = [[None for _ in range(length)] for _ in range(number_of_elements)]

        for i in range(number_of_elements):
            num = i
            
            for j in range(length - 1, -1, -1):
                divisor = systems_list[j]
                remainder = num % divisor
                number_system[i][j] = forms[remainder]
                num = num // divisor
                
        return number_system
    else:
        # Convert permutations iterator to list, then convert tuples to lists
        perms = list(permutations(forms, length))
        return [list(perm) for perm in perms]


def tuples_to_lists(data):
    """
    Converts all tuples to lists while preserving the nested structure.
    
    Args:
        data: Any combination of nested lists, tuples, or individual elements
        
    Returns:
        list: Structure with all tuples converted to lists
    """
    if isinstance(data, tuple):
        return [tuples_to_lists(item) for item in data]
    elif isinstance(data, list):
        return [tuples_to_lists(item) for item in data]
    else:
        return data