from toolkit import B2A
def hex (input) :

    m = 0xff
    tmp = []
    while(input>0):
        tmp.insert(0, m&input)
        input = input >> 8

    return B2A.b2a(tmp)

if __name__ == '__main__':
    a = 0x424954534354467b683164335f316e5f706c34316e5f353137337d
    print(hex(a))
