import uuid
import systems
from math import perm, comb, factorial
from functools import lru_cache
import itertools
from math import trunc
from collections.abc import Iterable
        
class Id01():
    def __init__(self, number_of_forms: int, number_of_times: int, table: str, forms_type: str, properties_names: list, forms: list = []):
        self.object_type_id = "01"
        self.properties_names = properties_names
        self.number_of_elements = 0
        if table == "normal":
            self.number_of_elements = pow(number_of_forms, number_of_times)
        elif table == "permutations":
            self.number_of_elements = perm(number_of_forms, number_of_times)
        elif table == "combinations":
            self.number_of_elements = comb(number_of_forms, number_of_times)
        intrinsic_number_systems = []
        for i in range(number_of_times):
            intrinsic_number_systems.append(number_of_forms)
        self.number_system = systems.system_01_or_02(number_of_times, table, self.number_of_elements, intrinsic_number_systems, forms_type, forms)
        
class Id02():
    def __init__(self, number_of_forms: int, number_of_times: int, table: str, forms_type: str, properties_names: list, forms: list):
        self.object_type_id = "02"
        self.properties_names = properties_names
        intrinsic_number_systems = []
        x = number_of_forms
        for i in range(number_of_times):
            intrinsic_number_systems.append(x)
            x -= 1
        self.number_of_elements = 1
        if table == "normal":
            for i in intrinsic_number_systems:
                self.number_of_elements *= i
        elif table == "permutations":
            self.number_of_elements = perm(number_of_forms, number_of_times)
        elif table == "combinations":
            self.number_of_elements = comb(number_of_forms, number_of_times)
        self.number_system = systems.system_01_or_02(number_of_times, table, self.number_of_elements, intrinsic_number_systems, forms_type, forms)
        
        del self.number_system[0]
    
class Id03():
    def __init__(self, nop: int, data: dict, properties_names: list):
        self.object_type_id = "03"
        intrinsic_number_systems = []
        self.properties_names = properties_names
        forms = []
        #print(self.properties_data)
        for i in data.values():
            intrinsic_number_systems.append(i["nof"])
            forms.append(i["forms"])
        self.number_of_elements = 1
        for i in data.values():
            self.number_of_elements *= i["nof"]
        self.number_system = systems.system_03(nop, self.number_of_elements, intrinsic_number_systems, forms)
        
class Id04():
    def __init__(self, nop: int, data: dict, table: str, properties_names: list):
        self.object_type_id = "04"
        intrinsic_number_systems = []
        self.properties_names = properties_names
        is_valid = all(data[i]["nof"] == data[0]["nof"] for i in range(len(data)))
        if is_valid == True:
            forms = []
            for i in range(data[0]["nof"]):
                forms.append(i)
            for i in range(nop):
                intrinsic_number_systems.append(data[i]["nof"])
            self.number_of_elements = 0
            if table == "normal":
                self.number_of_elements = pow(data[0]["nof"], nop)
            elif table == "permutations":
                self.number_of_elements = perm(data[0]["nof"], nop)
            elif table == "combinations":
                self.number_of_elements = comb(data[0]["nof"], nop)
            self.number_system = systems.system_01_or_02(nop, table, number_of_elements, intrinsic_number_systems, "alternative", forms)
        else:
            forms = {}
            for i in range(nop):
                forms[i] = []
                for j in range(data[i]["nof"]):
                    forms[i].append(j)
            for i in range(nop):
                intrinsic_number_systems.append(data[i]["nof"])
            number_of_elements = 1
            for i in range(nop):
                number_of_elements *= data[i]["nof"]
            self.number_system = systems.system_04(nop, number_of_elements, intrinsic_number_systems, forms, table)
        
        del self.number_system[0]
            
class Id05():
    def __init__(self, nop: int, p_names: list, data: dict):
        super().__init__()
        self.object_type_id = "05"
        number_of_properties = nop
        self.properties_names = p_names
        properties_data = data
        intrinsic_number_systems = []
        forms = []
        print(properties_data)
        for i in properties_data.values():
            intrinsic_number_systems.append(i["nof"])
            forms.append(i["forms"])
        sub_number_of_elements = []
        for i in range(nop):
            order = properties_data[str(i)]["order"]
            repetitions = properties_data[str(i)]["repetitions"]
            n = properties_data[str(i)]["nof"]
            k = properties_data[str(i)]["numits"]
            if not order and not repetitions:
                sub_number_of_elements.append(comb(n, k))
            elif not order and repetitions:
                sub_number_of_elements.append(comb(n + k - 1, k))
            elif order and not repetitions:
                sub_number_of_elements.append(perm(n, k))
            elif order and repetitions:
                sub_number_of_elements.append(n**k)
        self.number_of_elements = 1
        for i in sub_number_of_elements:
            self.number_of_elements *= i
        data = {}
        for i in range(nop):
            data[i] = {}
            data[i]["forms"] = forms[i]
            data[i]["order"] = properties_data[str(i)]["order"]
            data[i]["repetitions"] = properties_data[str(i)]["repetitions"]
            data[i]["k"] = properties_data[str(i)]["numits"]
        self.number_system = systems.system_05(number_of_properties, self.number_of_elements, intrinsic_number_systems, data)

class Id06():
    def __init__(self, nop: int, order: bool, repetitions: bool, p_names: list, data: dict):
        super().__init__()
        self.object_type_id = "06"
        number_of_properties = nop
        self.properties_names = p_names
        properties_data = data
        order = order
        repetitions = repetitions
        intrinsic_number_systems = []
        forms = [[]]
        for i in properties_data.values():
            intrinsic_number_systems.append(i["nof"])
            forms.append(i["forms"])
        picks = []
        for i in properties_data.values():
            picks.append(i["numits"])
        self.number_of_elements = 1
        total_pool_size = sum(len(g) for g in forms)
        total_picks = sum(picks)
        if repetitions:
            if order:
                self.number_of_elements = total_pool_size ** total_picks
            else:
                self.number_of_elements = comb(total_pool_size + total_picks - 1, total_picks)
        else:
            if order:
                self.number_of_elements = perm(total_pool_size, total_picks)
            else:
                self.number_of_elements = comb(total_pool_size, total_picks)
        self.number_system = systems.system_06(number_of_properties, self.number_of_elements, intrinsic_number_systems, forms, total_picks, order, repetitions)
        
class Id07():
    def __init__(self, nop: int, numits: int, order: bool, repetitions: bool, p_names: list, data: dict):
        super().__init__()
        
        self.object_type_id = "07"
        number_of_properties = nop
        number_of_items_to_select = numits
        self.properties_names = p_names
        properties_data = data
        repetitions = repetitions
        intrinsic_number_systems = []
        forms = []
        for i in properties_data.values():
            intrinsic_number_systems.append(i["nof"])
            forms.append(i["forms"])
        self.number_of_elements = 1
        total_pool_size = sum(len(g) for g in self.forms)
        if repetitions:
            if order:
                self.number_of_elements = total_pool_size ** number_of_items_to_select
            else:
                self.number_of_elements = comb(total_pool_size + number_of_items_to_select - 1, number_of_items_to_select)
        else:
            if order:
                self.number_of_elements = perm(total_pool_size, number_of_items_to_select)
            else:
                self.number_of_elements = comb(total_pool_size, number_of_items_to_select)
        self.number_system = systems.system_07(number_of_properties, self.number_of_elements, number_of_items_to_select, intrinsic_number_systems, self.forms, order, repetitions)
        
class Id08():
    def __init__(self, number_of_forms: int, form: str, forms: list):
        super().__init__()
        
        self.object_type_id = "08"
        number_of_forms = number_of_forms
        self.number_of_elements = self.bell_number(number_of_forms)
        number_system_preview = systems.system_08(forms)
        self.number_system = []
        for p in number_system_preview:
            self.number_system.append(p)
        
    @lru_cache(maxsize=None)
    def stirling_second_kind(self, n, k):
        if n == 0 or k == 0:
            return 0
        return k * self.stirling_second_kind(n-1, k) + self.stirling_second_kind(n-1, k-1)
    
    def bell_number(self, n):
        return sum(self.stirling_second_kind(n, k) for k in range(1, n+1))
    
class Id09():
    def __init__(self, number_of_forms: int, number_of_groups: int, form: str, forms: list):
        super().__init__()
        self.object_type_id = "09"
        form_type = form
        self.number_of_elements = self.stirling_second(number_of_forms, number_of_groups)
        number_system_preview = systems.system_09(forms, number_of_groups)
        self.number_system = []
        for p in number_system_preview:
            self.number_system.append(p)
        
    def stirling_second(self, n: int, k: int) -> int:
        if k < 0 or k > n:
            return 0
        s = [[0] * (k + 1) for _ in range(n + 1)]
        s[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                s[i][j] = j * s[i - 1][j] + s[i - 1][j- 1]
        return s[n][k]
    
class Id10():
    def __init__(self, number_of_forms: int, number_of_members: int, number_of_groups: int, forms: list, order_matters: bool):
        super().__init__()
        self.object_type_id = "10"
        self.number_of_elements = self.count(number_of_forms, number_of_groups, order_matters)
        number_system_preview = list(systems.system_10(forms, trunc(number_of_forms/number_of_groups), order_matters))
        self.number_system = deep_to_list(number_system_preview)
        
    def count(self, number_of_forms: int, number_of_groups: int, order_matters: bool):
        if not order_matters:
            return factorial(number_of_forms) // (factorial(trunc(number_of_forms/number_of_groups)) ** number_of_groups * factorial(number_of_groups))
        else:
            return factorial(number_of_forms)
        
class Id11():
    def __init__(self, number_of_members: int, forms: list, team_order: bool, members_order: bool, teams_list: list):
        super().__init__()
        
        self.object_type_id = "11"
        number_system_preview = systems.system_11(forms, number_of_members, team_order, members_order)
        number_system_preview1 = []
        for p in number_system_preview:
            number_system_preview1.append(p)
        # self.number_system = [{teams_list[j]: self.number_system_preview1[i][j] for j in range(number_of_teams)} for i in range(number_of_teams)]
        self.number_of_elements = self.count_teams(forms, number_of_members, team_order, members_order)
        self.number_system = []
        for i in range(len(number_system_preview1)):
            #print("Hello")
            team_dict = {}
            #print(teams_list)
            for j in range(len(teams_list)):
                #print("World")
                key = teams_list[j]
                #print(key)
                value = number_system_preview1[i][j]
                #print(value)
                team_dict[key] = value
            self.number_system.append(team_dict)
        
    def count_teams(self, forms: list, number_of_members: int, team_order: bool, members_order: bool):
        return sum(1 for _ in systems.system_11(forms, number_of_members, team_order, members_order))
    
class Id12():
    def __init__(self, forms: list, team_order: bool, members_order: bool, teams_list: list, teams_sizes: list):
        super().__init__()
        self.object_type_id = "12"
        number_system1 = systems.system_12(forms, teams_list, teams_sizes, team_order, members_order)
        self.number_system = []
        for i in number_system1:
            self.number_system.append(i)
        self.number_of_elements = len(self.number_system)
        
class Id13():
    def __init__(self, number_of_teams: int, forms: list, team_order: bool, members_order_list: list, teams_roles: dict):
        super().__init__()
        self.object_type_id = "13"
        teams_roles = dict(teams_roles)
        self.number_of_elements, self.number_system = systems.system_13(number_of_teams, teams_roles, team_order, members_order_list, forms)
        
class Id14():
    def __init__(self, currency: str, amount: int, denominations: list):
        super().__init__()
        
        self.object_type_id = "14"
        self.number_of_elements_all, self.number_system_all, self.number_of_elements, self.number_system = systems.system_14(currency, amount, denominations)
    
class Id15():
    def __init__(self, limit_of_sum: int, sums: str, repetition: bool):
        super().__init__()
        
        self.object_type_id = "15"
        if sums == "Ordered":
            order = True
        else:
            order = False
        self.number_system_gen = systems.system_15(limit_of_sum, order, repetition)
        self.number_system = []
        for i in self.number_system_gen:
            self.number_system.append(i)
        self.number_of_elements = len(self.number_system)
        
class Id16():
    def __init__(self, limit_of_sum: int, sums: str):
        super().__init__()
        
        self.object_type_id = "16"
        self.limit_of_sum = limit_of_sum
        self.sums_type = sums
        if sums == "Ordered":
            order = True
        else:
            order = False
        print(order)
        self.number_of_elements, self.number_system = systems.system_16(limit_of_sum, order)
        # for i in self.number_system_gen:
        #     self.number_system.append(i)
        # self.number_of_elements = len(self.number_system)
        
class Id17():
    def __init__(self, limit_of_sum: int, k: int, sums: str, repetition: bool):
        super().__init__()
        
        self.object_type_id = "17"
        self.limit_of_sum = limit_of_sum
        self.k = k
        self.sums_type = sums
        self.repetition = repetition
        if sums == "Ordered":
            order = True
        else:
            order = False
        #print(order)
        self.number_of_elements, self.number_system = systems.system_17(limit_of_sum, k, order, repetition)
        
class Id18():
    def __init__(self, limit_of_sum: int, k: int, sums: str, repetition: bool):
        super().__init__()
        
        self.object_type_id = "18"
        self.limit_of_sum = limit_of_sum
        self.k = k
        self.sums_type = sums
        self.repetition = repetition
        if sums == "Ordered":
            order = True
        else:
            order = False
        #print(order)
        self.number_of_elements, self.number_system = systems.system_18(limit_of_sum, k, order, repetition)

class Id19():
    def __init__(self, limit_of_sum: int, sums: str, repetition: bool):
        super().__init__()
        
        self.object_type_id = "19"
        self.limit_of_sum = limit_of_sum
        self.sums_type = sums
        self.repetition = repetition
        if sums == "Ordered":
            order = True
        else:
            order = False
        self.number_of_elements, self.number_system = systems.system_19(limit_of_sum, order, repetition)
        
class Id20():
    def __init__(self, limit_of_sum: int, sums: str, repetition: bool):
        super().__init__()
        
        self.object_type_id = "20"
        self.limit_of_sum = limit_of_sum
        self.sums_type = sums
        self.repetition = repetition
        if sums == "Ordered":
            order = True
        else:
            order = False
        self.number_of_elements, self.number_system = systems.system_20(limit_of_sum, order, repetition)
        
class Id21():
    def __init__(self, number_of_forms: int, r: int, forms: list):
        super().__init__()
        
        self.object_type_id = "21"
        self.number_of_forms = number_of_forms
        self.forms = forms
        self.r = r
        self.number_of_elements, self.number_system = systems.system_21(forms, r)
        self.number_system = deep_to_list(self.number_system)
        
class Id22():
    def __init__(self, number_of_forms: int, r: int, forms: list):
        super().__init__()
        
        self.object_type_id = "22"
        self.number_of_forms = number_of_forms
        self.forms = forms
        self.r = r
        self.number_of_elements, self.number_system = systems.system_22(forms, r)
        
class Id23():
    def __init__(self, number_of_items: int, forms: list, direction_matters: bool, reflection: str):
        super().__init__()
        
        self.object_type_id = "23"
        self.number_of_items = number_of_items
        self.forms = forms
        self.direction_matters = direction_matters
        self.reflection = reflection
        #print(self.reflection)
        reflection_bool = True
        if self.reflection == "identical":
            reflection_bool = True
        elif self.reflection == "distinct":
            #print("What is finally the problem?")
            reflection_bool = False
        #print(reflection_bool)
        self.number_of_elements, self.number_system = systems.system_23(forms, direction_matters, reflection_bool)
        
class Id24():
    def __init__(self, number_of_items: int, forms: list, direction_matters: bool, reflection_identical: bool):
        super().__init__()
        
        self.object_type_id = "23"
        self.number_of_items = number_of_items
        self.forms = forms
        self.direction_matters = direction_matters
        self.reflection_identical = reflection_identical
        self.number_of_elements, self.number_system = systems.system_24(forms, direction_matters, reflection_identical)
        self.number_system = deep_to_list(self.number_system)
        
class Id25():
    def __init__(self, number_of_items: int, number_of_items_to_select: int, forms: list, direction_matters: bool, reflection: str):
        super().__init__()
        
        self.object_type_id = "25"
        self.number_of_items = number_of_items
        self.number_of_items_to_select = number_of_items_to_select
        self.forms = forms
        self.direction_matters = direction_matters
        self.reflection = reflection
        reflection_bool = True
        if self.reflection == "identical":
            reflection_bool = True
        elif self.reflection == "distinct":
            reflection_bool = False
        self.number_of_elements, self.number_system = systems.system_25(number_of_items, number_of_items_to_select, forms, direction_matters, reflection_bool)
        self.number_system = deep_to_list(self.number_system)
        
class Id26():
    def __init__(self, number_of_items: int, forms: list, repetition_allowed: bool, r: int):
        super().__init__()
        
        self.object_type_id = "26"
        self.number_of_items = number_of_items
        self.forms = forms
        self.repetition_allowed = repetition_allowed
        self.r = r
        self.number_of_elements, self.number_system = systems.system_26(forms, repetition_allowed, r)
        self.number_system = deep_to_list(self.number_system)
    
#=================================HELPER FUNCTION====================================================
def deep_to_list(obj): # To convert multi dimensional tuples to multi dimensional lists
    if isinstance(obj, (str, bytes, bytearray)):
        return obj
    if isinstance(obj, Iterable):
        return [deep_to_list(i) for i in obj]
    return obj