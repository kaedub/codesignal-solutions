# Problem: find the number of times you would have to add 1 to each item
# to create an increasing array
# 
# Strategy: starting at 2nd number, 
# if it is <= the previous number
#   then add to it the differnce between the previous number plus one
#   and add amount to a counter
# set previous for next value every time

def arrayChange(arr):
    totalCount = 0
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] <= prev:
            count = prev - arr[i] + 1
            arr[i] = arr[i] + count
            totalCount += count
        prev = arr[i]
    return totalCount
        
