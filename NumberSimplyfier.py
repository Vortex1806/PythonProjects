def Remover(List):
    unique = []
    for num in List:
        if num not in unique:
            unique.append(num)
    return unique
