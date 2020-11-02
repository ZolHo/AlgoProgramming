s = "XKRKGYK GTTUATIK XUZGZK HXOYQ"
ans = ""
for i in range (26):
    for j in s:
        if ord(j) == ord(' '):
            ans += " "
            continue
        ans += chr((ord(j.upper())+i-ord('A'))%(26)+ord('A'))
    print(ans)
    ans = ""
