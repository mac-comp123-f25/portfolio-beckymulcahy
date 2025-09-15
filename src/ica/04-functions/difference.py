def smallest_diff(x, y, z):
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    return min_diff
smallest_diff(3, 9, 5)

def smallest_diff(x, y, z):
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    return min_diff
smallest_diff(32, 43, 90)

''' Local Environment 
x  32
y  43
z  90 
diff1= abs(32-43)
diff2= abs(43-90)
diff3= abs(32-90)
'''