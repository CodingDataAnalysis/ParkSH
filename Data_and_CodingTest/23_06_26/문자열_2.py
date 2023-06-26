strA = 'EUVersusUAEOnSoccerRN'
k = list(strA)
a = list()
b = list()
a.append(k[0])
b.append(k.pop(0))
print(b)
while k != []:
    if b[-1].isupper() == True:
        if k[0].isupper() == True:
            b.append(k.pop(0))
            print(b)
        else :
            a.append(b[-1])
            b.append(k.pop(0))
            print(f'a : {a}')
    else :
        if k[0].isupper() == True:
            b.append(k[0])
            a.append(k.pop(0))
        else :
            b.append(k.pop(0))

print(a)
#%%
