import random, string
import hashlib

inputString = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
inputString = "DAN"
hash_object = hashlib.sha1(inputString)
hex_dig = hash_object.hexdigest()
length = len(inputString)
myWordHash = hex_dig[:5]
print "My word is ", inputString
print "My word hashed is ", myWordHash


myList = []
void = []
i = 0
randomWordHash = ""
wordGenerate = ""
while (myWordHash != randomWordHash):

    if (wordGenerate == inputString):
        wordGenerate = ''.join(random.choice(string.ascii_uppercase) for i in range(3))
        
        inputs = wordGenerate
        hash_object = hashlib.sha1(inputs)
        hex_dig = hash_object.hexdigest()
        #length = len(inputString)
        randomWordHash = hex_dig[:5]
        print wordGenerate
        
    else:
         print wordGenerate

    
    
    
    
    
      
# '2591e5f46'
print inputString + " is equal to " + inputs  
print "Fin"



