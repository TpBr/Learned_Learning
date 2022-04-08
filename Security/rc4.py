import sys


#helper function to assist in permutations
def Swap(S, i, j):
    tempI = S[i]
    tempJ = S[j]

    S[i] = tempJ
    S[j] = tempI
    return S

def IP(S, byteArrKey, key_size):
    j = 0
    for i in range( 0, 256 ):
        j = (j + S[i] + byteArrKey[i % key_size]) % 256
        S = Swap(S, i, j)
    
    return S

def Stream(byteArrPlain, S):
    
    Cipher = []
    i = 0
    j = 0

    for k in range(0, 3072):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S = Swap(S, i, j)
        t = (S[i] + S[j]) % 256
        k = S[t]

    for m in range(0, len(byteArrPlain)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S = Swap(S, i, j)
        t = (S[i] + S[j]) % 256
        k = S[t] #each k is an element of the 'keystream'
        
        ciph = k ^ byteArrPlain[m]
        Cipher.append(ciph)

    return Cipher

def main():
    #labeling of the args
    key_size = int(sys.argv[1])
    key_size = key_size//8
    key_file = sys.argv[2]
    Plaintext_file = sys.argv[3]
    Ciphertext_file = sys.argv[4]

    # read through data and make S and key

    #read through the plaintext file and store for xoring
    plainObject = open(Plaintext_file, "rb")

    byteArrPlain = list(plainObject.read())

    plainObject.close()

    #read through the key file and store for xoring
    keyObject = open(key_file, "rb")

    byteArrKey = list(keyObject.read())

    keyObject.close()

    S = []
    for i in range(0, 256):
        S.append(i)


    S = IP(S, byteArrKey, key_size)
    #perform stream cipher
    ans = Stream(byteArrPlain, S)

    bytearr = bytearray(ans)

    #writing to output file
    cipherObject = open(Ciphertext_file, "wb")

    cipherObject.write(bytearr)

    cipherObject.close()


if __name__ == '__main__':
    main()