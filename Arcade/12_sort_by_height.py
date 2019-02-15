tree = -1
def sort_people(li):
    people = []
    for item in li:
        if item != tree:
            people.append(item)
    return sorted(people)

def sortByHeight(a):
    p = sort_people(a)
    for i in range(len(a)):
        if a[i] != tree:
            a[i] = p[0]
            p.pop(0)
    return a
