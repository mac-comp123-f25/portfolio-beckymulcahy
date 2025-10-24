def every_other (list) :
    result = []
    for i in range (0, len(list), 2) :
        result.append(list[i])
    return result
print(every_other([1, 2, 3]))

def sum_positive (numbers)  :
    total = 0
    for num in numbers :
        if num > 0 :
            total += num
        return total

print(sum_positive([1, 2, 3, -5, -10]))
