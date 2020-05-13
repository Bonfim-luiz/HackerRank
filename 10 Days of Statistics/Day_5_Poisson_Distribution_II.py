# Day 5: Poisson Distribution II
# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

x, y = [float(num) for num in input().split(" ")]

custo_x = 160 + 40*(x + x**2)
custo_y = 128 + 40*(y + y**2)

print(round(custo_x, 3))
print(round(custo_y, 3))
