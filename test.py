# cython: language_level=3
import itertools
from typing import List

def system_01_or_02(int number_of_times, str table, int number_of_elements,
                    List[int] intrinsic_number_systems, str forms_type,
                    List forms) -> List:
    cdef int i, j, num, num1, ans
    cdef list number_system = []

    if table == "normal" and forms_type in ("default", "alternative_base", "alternative"):
        for i in range(number_of_elements):
            row = [None] * number_of_times
            num = i
            num1 = number_of_times
            for j in intrinsic_number_systems:
                ans = num % j
                row[num1 - 1] = forms[ans]
                num = num // j
                num1 -= 1
            number_system.append(row)
        return number_system

    elif table == "permutations" and forms_type in ("default", "alternative_base", "alternative"):
        if len(forms) < number_of_times:
            return []
        return [list(p) for p in itertools.permutations(forms, number_of_times)]

    elif table == "combinations" and forms_type in ("default", "alternative_base", "alternative"):
        if len(forms) < number_of_times:
            return []
        return [list(c) for c in itertools.combinations(forms, number_of_times)]

    return []