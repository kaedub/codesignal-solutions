def makeArrayConsecutive2(statues):
    statues.sort()
    next_value = min(statues)
    need = 0
    
    for i in range(1, len(statues)):
        diff = statues[i] - statues[i-1]
        
        if diff > 1:
            need += diff - 1
    return need