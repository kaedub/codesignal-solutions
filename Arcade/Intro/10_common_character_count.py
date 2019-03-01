def commonCharacterCount(s1, s2):
    common = 0
    st1 = s1
    st2 = list(s2)
    for c1 in st1:
        for c2 in st2:
            if c1 == c2:
                common += 1
                st2.remove(c2)
                break
    return common
                    