s = "1yEt5juom35MATrGy_UWq9w"
ans = ""
# for i in range (26):
#     for j in s:
#         if ord(j) == ord(' '):
#             ans += " "
#             continue
#         ans += chr((ord(j.upper())+i-ord('A'))%(26)+ord('A'))
#     print(ans)
#     ans = ""
#

for i in range(15) :
    temp= ""
    for j in s :
        j = chr(ord(j)-i)
        temp +=j
    print(temp)