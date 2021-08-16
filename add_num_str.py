def func(num1, num2):
    nums= {"0":0, "1":1, "2":2, "3":3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9":9}
    counter = 1
    n1 = 0
    for i in range(len(num1)-1,-1,-1):
        n1 += nums[num1[i]] * counter
        counter *= 10
    counter = 1
    n2 = 0
    for i in range(len(num2)-1,-1,-1):
        n2 += nums[num2[i]] * counter
        counter *= 10
    return n1 + n2
    
def with_float(num1, num2):
    list_num1 = num1.split('.')
    list_num2 = num2.split('.')
    ful_inter = str(func(list_num1[0], list_num2[0]))
    if len(list_num1) > 1 and len(list_num2) > 1:
        ful_floats = str(func(list_num1[1], list_num2[1]))
    elif len(list_num1) > 1:
        ful_floats = list_num1[1]
    elif len(list_num2) > 1:
        ful_floats = list_num2[1]
    result = [ful_inter, ful_floats]
    return ".".join(result)
    
    
print(with_float('123', '321.11'))
