a = 1
if a < 2:
    print('既不是素数也不是合数')
elif a == 2:
    print('是素数')
else:
    flag = False
    for i in range(2, a):
        if a % i == 0:
            flag = True
            break
    if flag:
        print('是合数')
    else:
        print('是素数')