from typing import List
# t = 1
# for i in range(26):
#     print("'"+chr(ord('a') + i)+"':"+str(2**i)+"," ,end="")
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        char_dic = {'a':1,'b':2,'c':4,'d':8,'e':16,'f':32,'g':64,'h':128,'i':256,'j':512,'k':1024,'l':2048,'m':4096,'n':8192,'o':16384,'p':32768,'q':65536,'r':131072,'s':262144,'t':524288,'u':1048576,'v':2097152,'w':4194304,'x':8388608,'y':16777216,'z':33554432}
        jiyi = {}
        def digui(sone, stwo) :
            if (sone,stwo) in jiyi :
                return jiyi[(sone, stwo)]
            if sone == stwo:
                return True
            if len(sone) == 1:
                return False

            one_qianzhui, two_qianzhui, two_houzhui = [char_dic[i] for i in sone], [char_dic[i] for i in stwo], [char_dic[i] for i in stwo]
            for i in range(1,len(sone)) :
                one_qianzhui[i] += one_qianzhui[i-1]
                two_qianzhui[i] += two_qianzhui[i-1]
            if one_qianzhui[-1] != two_qianzhui[-1]:
                return False
            if (sone, stwo) in jiyi:
                print(jiyi[(sone, stwo)])
            for i in range(len(sone)-1)[::-1]:
                two_houzhui[i] += two_houzhui[i +1]

            two_houzhui = two_houzhui[::-1]
            stwo_ni = stwo[::-1]
            for i in range(len(sone)-1) :
                if one_qianzhui[i] == two_qianzhui[i] :
                    flag = digui(sone[:i+1], stwo[:i+1]) and digui(sone[i+1:], stwo[i+1:])
                    if flag:
                        jiyi[(sone, stwo)] = True
                        return True
                if one_qianzhui[i] == two_houzhui[i] :
                    flag = digui(sone[:i + 1], stwo_ni[:i+1]) and digui(sone[i + 1:], stwo_ni[i+1:])
                    if flag:
                        jiyi[(sone, stwo)] = True
                        return True
            jiyi[(sone, stwo)] = False
            return False
        return digui(s1,s2)

so = Solution()
print(so.isScramble("eebaacbcbcadaaedceaaacadccd",
"eadcaacabaddaceacbceaabeccd"))