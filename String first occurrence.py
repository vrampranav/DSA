def getIndex(st):
    d = {}
    for i in range(len(st)):
        if st[i] not in d:
            d[st[i]] = [1,i]
        else:
            d[st[i]][0] = d[st[i]][0]+1
    for k,v in d.items():
        if v[0]==1:
            return v[1]
    else:
        return -1
st = input()
print(getIndex(st))
