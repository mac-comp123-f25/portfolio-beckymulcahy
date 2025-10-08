def every_other (list) :
    result = []
    for i in range (0, len(list), 2) :
        result.append(list[i])
    return result
print(every_other([1, 2, 3]))