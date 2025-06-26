N = 5
total = 0
prod = 1
min_val = float('inf')
max_val = -float('inf')
for _ in range(N):
    num = int(input('введите целое: '))
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
    total += num
    prod *= num

print(total, sep='\n')
print(total / N)
print(prod)
print(min_val, max_val)
