numbers = list(map(int, input().split()))
print(sum(num for num in numbers if num > 0))