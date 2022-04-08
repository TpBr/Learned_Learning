import sys

def main():
	#labeling of the args
    key_size = sys.argv[1]
    key_file = sys.argv[2]
    Plaintext_file = sys.argv[3]
    Ciphertext_file = sys.argv[4]
    #read through the key file and store for xoring
    keyObject = open(key_file, "rb")

    byteArrKey = list(keyObject.read())

    keyObject.close()
   
    #read through the plaintext file and store for xoring
    plainObject = open(Plaintext_file, "rb")

    byteArrPlain = list(plainObject.read())

    plainObject.close()

    #xor the bytes together
    bytearr = []
    for i in range(0, len(byteArrKey)):
    	bytearr += [(byteArrKey[i] ^ byteArrPlain[i])]

    bytearr = bytearray(bytearr)

    cipherObject = open(Ciphertext_file, "wb")

    cipherObject.write(bytearr)

    cipherObject.close()

if __name__ == '__main__':
    main()