from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util import Counter
import sys



def main():
    #labeling of the args
    key_size = int(sys.argv[1]) #always equal to 128 for block size in bit units
    key_file = sys.argv[2]
    mode = sys.argv[5] #encrypt or decrypt

    if(mode == "encrypt"):

        Plaintext_file = sys.argv[3]
        Ciphertext_file = sys.argv[4]

        keyObject = open(key_file, "rb")

        bytesKey = keyObject.read()

        keyObject.close()

        plainObject = open(Plaintext_file, "rb")

        bytesPlain = plainObject.read()

        plainObject.close()
        #need to make intial vector and send with ciphertext
        IV = get_random_bytes(16)

        counter = Counter.new(128, initial_value = int.from_bytes(IV, "big"))

        ciphObject = AES.new(bytesKey, AES.MODE_CTR, counter = counter)

        cipher_bytes = ciphObject.encrypt(bytesPlain)

        cipherObject = open(Ciphertext_file, "wb")

        cipherObject.write(IV)
        cipherObject.write(cipher_bytes)

        cipherObject.close()
    #decrypt mode
    else:
        Ciphertext_file = sys.argv[3]
        Plaintext_file = sys.argv[4] #your output
        #file IO
        keyObject = open(key_file, "rb")

        bytesKey = keyObject.read()

        keyObject.close()

        ciphObject = open(Ciphertext_file, "rb")
        #IV
        IV = ciphObject.read(16)
        bytesCiph = ciphObject.read()

        counter = Counter.new(128, initial_value = int.from_bytes(IV, "big"))

        ciphObject.close()

        plainObject = AES.new(bytesKey, AES.MODE_CTR, counter=counter)

        plaintext_bytes = plainObject.decrypt(bytesCiph)

        plainObjectFile = open(Plaintext_file, "wb")

        plainObjectFile.write(plaintext_bytes)

        plainObjectFile.close()

if __name__ == '__main__':
    main()