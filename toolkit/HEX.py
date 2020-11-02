from toolkit import B2A
def hex (input) :

    m = 0xff
    tmp = []
    while(input>0):
        tmp.insert(0, m&input)
        input = input >> 8

    return B2A.b2a(tmp)

if __name__ == '__main__':
    input = 0x73796e636f706174696f6e5f7072657474795f73696c766572736d69746873
    print(hex(input))