def isLucky(n):
    num = str(n)
    first = num[0:len(num)//2]
    second = num[len(num)//2:]
    sum1 = 0
    sum2 = 0
    for i in range(len(num)//2):
        sum1 += int(first[i])
        sum2 += int(second[i])
    
    if sum1 == sum2:
        return True
    return False