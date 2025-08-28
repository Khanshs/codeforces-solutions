def min_cost(n, m, a, b):

    cost1 = n*a #option1 mua single-ticket
    cost2 = (n//m)*b + (n%m)*a #option 2 kết hợp mua multi-ticket và singl-ticket
    cost3 = (n//m + 1)*b #option 3 mua multi-ticket dù dư nhưng có thể multi-ticket này vẫn rẽ hơn single-ticket

    return min(cost1, cost2, cost3)

n, m, a, b = map(int, input().split())
print(min_cost(n, m, a, b))