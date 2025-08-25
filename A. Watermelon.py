def can_divide_watermelon(w):
    if w % 2 == 0 and w > 2:
        return "YES"
    else:
        return "NO"
w = int(input())
if w < 1 or w > 100:
    exit()
print(can_divide_watermelon(w))