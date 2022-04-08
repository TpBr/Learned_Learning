
#https://www.quantamagazine.org/how-godels-incompleteness-theorems-work-20200714/
#by Ernest Nagel and James Newman in their 1958 book, "Gödel’s Proof"

def godelCalc(logicalStatements, tokenList):

   #to do: need to generalize into prime number generator
   listOPrimes = [2, 3, 5, 7, 11, 13, 17, 
   19, 23, 29, 31, 37, 41, 43, 47, 53, 
   59, 61, 67, 71, 73, 79, 83, 89, 97,
   101, 103, 107, 109, 113, 127, 131, 137, 
   139, 149, 151, 157, 163, 167, 173, 179, 
   181, 191, 193, 197, 199,
   211, 223, 227, 229, 233, 239, 241, 251, 
   257, 263, 269, 271, 277, 281, 283, 293]

   runningSum = 1

   prop = ""

   flag = False

   for i in range(0, len(logicalStatements)):

      if not (logicalStatements[i] in (tokenList.keys())):
         flag = True
         break
      else:
         runningSum *= (listOPrimes[i] ** tokenList[logicalStatements[i]])
         prop += logicalStatements[i]

   if prop not in tokenList.keys():
      tokenList[prop] = runningSum

   if flag:
      return("error")
   return([ runningSum, tokenList ] )


def cleanHelp(aList, tokenList):
   
   newList = []

   for i in aList:
      if not (i.isspace()):
         newList.append(i)
   return newList
         
def main():

   tokenList = {"not" : 1, "or" : 2 , "->" : 3, "exists" : 4,
   "=" : 5, "0" : 6, "s" : 7, "(" : 8, ")" : 9, "," : 10, "+" : 11, "*" : 12,
   "x" : 13, "y" : 17, "z" : 19, "x1" : 23, "y1" : 29, "z1" : 31, "x2" : 37, 
   "y2" : 41, "z2" : 43, "x3" : 47, "y3" : 53, "z3" : 59, "x4" : 61, "y4" : 71,
   "z4" : 73, "x5" : 79, "y6" : 83, "z6" : 89, "x7" : 97}

   exitVar = False

   while not exitVar : 

      rawInput = input("Godel Calculator!!!!!!\nInput Below!\n")

      if rawInput == "stop":

         exitVar = True
         break
      
      cleanedInput = rawInput.split()

      cleanedInput = cleanHelp(cleanedInput, tokenList)

      godelNum = godelCalc(cleanedInput, tokenList)[0]

      tokenList = godelCalc(cleanedInput, tokenList)[1]

      print()
      print(cleanedInput)
      print()
      
      if type(godelNum) == int:
         print(godelNum)
      else:
         print("error")



if __name__ == "__main__":
   main()
