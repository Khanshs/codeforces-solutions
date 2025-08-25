def is_lucky(num):
    if num == 0:
        return False
    str_num = str(num)
    return all(c in ('4', '7') for c in str_num)

n = int(input())

temp_end = 0
for i in range(1, n + 1):
    if is_lucky(n):
        temp_end = 1
        break

    elif n % 4 == 0 or n % 7 == 0 or (is_lucky(i) and n%i== 0):
        temp_end = 1
        break

if temp_end == 1:
    print('YES')
else:
    print('NO')


