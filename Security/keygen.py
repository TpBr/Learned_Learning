from Cryptodome.Random import get_random_bytes
import sys

def main():
    key_size = int(sys.argv[1])
    output_file_name = sys.argv[2]

    outObject = open(output_file_name, "wb")
    #need to divide into bytes for the library's generator
    key_size2 = key_size//8 

    key = get_random_bytes(key_size2)
    
    outObject.write(key)

    outObject.close()

if __name__ == '__main__':
	main()