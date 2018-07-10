#1
def fibonacci(n, m):
    '''
    возвращает ряд фибоначчи
    от n до m включительно
    '''
    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)
    return res

fibonacci(1,5)

#2
def sort_to_max(origin_list):
    print (origin_list)
    lst = []
    while len(origin_list) > 0 :
        a = origin_list[0]
        for i in origin_list :
            if i <= a :
                a = i
        origin_list.remove(a)
        lst.append(a)
    return lst

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
#3
def alt_filter(func, itr):
    '''
    реализация функции filter
    '''
    new_itr = [elem for elem in itr if func(elem)]
    if type(itr) is tuple:
        new_itr = tuple(new_itr)
    if type(itr) is set:
        new_itr = set(new_itr)
    if type(itr) is str:
        new_itr = ''.join(new_itr)
    print(new_itr)
    return new_itr
alt_filter(lambda x: x > 5, {2, 10, -12, 2.5, 20, -11, 4, 4, 0})





