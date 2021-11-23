numbers = [2,2,3,4,6,3,4,6,1]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)
