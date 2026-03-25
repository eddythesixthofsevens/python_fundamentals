# def only_ints(a, b):
#     if type(a) == int and type(b) == int:
#         return(True)
#     else:
#         return(False)
# print(only_ints("a", 4))

# false_test = only_ints("3", 3)
# true_test = only_ints(3, 3)
# print(f"True case (3, 3): {true_test}\nFalse case ('3', 3): {false_test}")

# def clamp(val, min, max):
#     if val >= min and val <= max:
#         return val
#     elif val < min:
#         return min
#     elif val > max:
#         return max
# print(clamp(5, 5, 10))

def all_equal(list):
    num = list[0]
    print(num)
    for i in range(0, len(list)):
        if i == num:
            print("Yes")
            continue
        else:
            return False
    return True

nums = [1, 1, 1, 1, 1]
all_equal(nums)
