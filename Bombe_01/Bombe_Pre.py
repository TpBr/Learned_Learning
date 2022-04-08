"""
Implementation of Cryptanalytic Neural Network based on 'Research on Plaintext Restoration of AES Based on Neural Network'

Specifically the second experiment where the input is standard in of text files containing random digits

"""
import random
import pyAesCrypt
import tensorflow as tf
from tensorflow import keras
import numpy as np  
import matplotlib.pyplot as plt
from bitstring import ConstBitStream
import os

"""
Gather relevant data from the training set and format properly for the neural network while 
keeping input and correct output in-line
"""
def getData():
#128 to 256 to 256 to 128 layer dimensions
    cipherList = []
    messageList = []
    #gather data from files
    string0 = "m"
    string1 = "c"
    for i in range(0, 1000):
        stringTemp = str(i)
        fileName = string0 + stringTemp + ".txt"
        fileM = open(fileName, encoding ="utf8")
        for line in fileM:
            for char in line:
                messageList.append(ord(char))
        fileM.close()
        cipherName = string1 + stringTemp + ".txt.aes"
        byte = os.path.getsize(cipherName)
        fileC = open(cipherName, 'rb')
        #handling bitstream from encrypted data
        bitData = ConstBitStream(bytes = fileC.read(byte), length = byte*8)
        while(bitData.pos < byte*8):
            B = bitData.read(8).uint
            cipherList.append(B)
        fileC.close()
    #now have sets of bytes ready for training split up for training and testing phases
    tempC = (len(cipherList)//4) * 3
    tempM = (len(messageList)//4) * 3
    #output organized data to use in network
    aList = [cipherList[1:tempC],messageList[1:tempM],cipherList[tempC:-1],messageList[tempM:-1]]
    return aList  

#need also to organize bytes into bits since neural network is 128 bit input
def charMake128(aList):
    outputList = []
    finalList = []
    bList = []
    tempList = []
    counter = 0

    if(len(aList) % 16 != 0):
        while(len(aList) % 16 != 0):
            aList.pop()
  
    for elem in aList:
        if(counter != 15):         
            tempList += [elem]
            counter += 1
        else:
            counter = 0
            tempList += [elem]
            bList.append(tempList)
            tempList = []
        
    for l in bList: #16 elements
        for num in l:
            #break each num into list of bits
            temp = bin(num)[2:]
            if(len(temp)<8):
                while(len(temp)<8):
                    temp = "0" + temp #padding
            for char in temp:
                bit = int(char)
                bit = [bit]
                outputList += bit
        finalList.append(outputList)
        outputList = []

    return finalList
  

def breakAES(aList):
    #call helpers to organize data
    cipherData = charMake128(aList[0])
    cipher = cipherData[1:10000]
    messageData = charMake128(aList[1])
    mess = messageData[1:10000]
    testCipher = charMake128(aList[2])
    testC = testCipher[1:100]
    testMessage = charMake128(aList[3])
    testM = testMessage[1:100]
    #network architecture below
    model = keras.Sequential([
        keras.layers.Dense(256, input_shape=(128,), activation = "hard_sigmoid"),
        keras.layers.Dense(256, activation = "hard_sigmoid"),
        keras.layers.Dense(128, activation = "hard_sigmoid")
    ])
    #stochastic gradient descent, logistic calculation, MSE similarity metric
    sgd = keras.optimizers.SGD(lr=0.01)
    model.compile(optimizer = sgd, loss="mean_squared_error", metrics=["mse"])

    model.fit(cipher, mess, epochs=10)

    test_loss, test_acc = model.evaluate(testC, testM)

    a = model.predict(testC)
    print("predicted")
    print(a)
    print("was actualy")
    print(testM)

#below used for encrypting message data
def enc():
    string0 = "m"
    string1 = "c"
    bufferSize = 64 * 1024
    for i in range(0, 1000):
        stringTemp = str(i)
        fileName = string0 + stringTemp + ".txt"
        cipherName = string1 + stringTemp + ".txt.aes"

        pyAesCrypt.encryptFile(fileName, cipherName, "training", bufferSize)

#below used for making messages similarily in paper
def messageMaker():
    string0 = "m"

    for i in range(0, 1000):
        stringTemp = str(i)
        fileName = string0 + stringTemp + ".txt"
        theFile = open(fileName, "w")
        for i in range(0,16384):
            digit = random.randint(0,9)
            digit = str(digit)
            theFile.write(digit)

        theFile.close()
        

def main():
    data = getData()
    breakAES(data)
    
if __name__ == "__main__":
    main()