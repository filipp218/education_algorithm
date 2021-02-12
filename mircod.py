"""
Задача 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом.
"""
def unique_numbers(first, second):
    Blist = set(second)
    return [ numb for numb in first if numb not in Blist]
  
  
  
 
"""
Задача 2. Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.
"""
def drop_zero(digits):
    n= 0
    for i in range(len(digits) - 1):
        if digits[i - n] == 0:
            digits.pop(i - n)
            n += 1
            i -= 1
    if digits[len(digits) - 1] == 0:
        digits.pop(len(digits) - 1)
    return digits
      
