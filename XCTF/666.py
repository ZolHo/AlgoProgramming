target = "izwhroz\"\"w\"v.K\".Ni"
ans = ""
for i in range(18):
    for j in range(200):
        p = i%3
        if( p==0):
            if (ord(target[i]) == 18 ^ (j+6)):
                ans+=chr(j)
                break
        if p==1:
            if ord(target[i])==(j-6) ^ 18:
                ans+=chr(j)
                break
        if p==2:
            if ord(target[i])==j^6^18 :
                ans += chr(j)
                break
print(ans)

