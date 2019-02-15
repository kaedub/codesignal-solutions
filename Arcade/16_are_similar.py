def areSimilar(a, b):
    count = 0
    list_a = []
    list_b = []
    for i in range(len(a)):
        if (a[i]!= b[i]):
            count +=1
            list_a.append(a[i])
            list_b.append(b[i])

    if (count ==0):
        return True 

    elif count ==2: 
        return set(list_a)==set(list_b)

    else:
        return False