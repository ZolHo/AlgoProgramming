from Crypto import Util
import Crypto.Util.number
def b2l (input) :
    return Util.number.bytes_to_long(input)

def l2b (input):
    return Util.number.long_to_bytes(input)

if __name__ == '__main__':
    print(l2b(11515195063862318899931685488813747395775516287289682636499965282714637259206269))