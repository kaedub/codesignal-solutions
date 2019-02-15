def addBorder(picture):
    hf = "*" * (len(picture[0])+2)
    newpic = [hf]
    for i in range(len(picture)):
        s = "*"+picture[i]+"*"
        newpic.append(s)
    newpic.append(hf)
    return newpic
