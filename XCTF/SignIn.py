import math

v5 = 65537
v4 = 103461035900816914121390101299049044413950405173712170434161686539878160984549
two = 0xad939ff59f6e70bcbfad406f2494993757eee98b91bc244184a377520d06fc35

def sub_96A(input):
    v3 = 0
    xulie = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102]
    a2 = [0 for i in range(2*len(input))]
    result = len(input)
    for i in range(200)[::2]:
        if v3>=result :
            break
        a2[i] = xulie[ord(input[v3])>>4]
        a2[i+1] = xulie[ord(input[v3]) & 0xF]
        v3 += 1
    return a2

# for i in range(20):
#     print(i, [chr(j) for j in sub_96A(chr(i))])
#
# shuru = 0
# one = sub_96A(shuru)
one = 2

# while True:
#     p = one
#     for i in range(65536):
#         p = p*one%v4
#
#     if two == p:
#         print(one)
#         break
#     one +=1

p = 282164587459512124844245113950593348271
q = 366669102002966856876605669837014229419
fn = (p-1)*(q-1)
# print(fn)
for i in range(10000000000):
    if (91646299298871237857836940212608056141193465208586711901499120163393577626813*65537)%fn ==1 :
        print(i)
        break
