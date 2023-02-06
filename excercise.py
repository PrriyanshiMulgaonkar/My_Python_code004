import string    
import random  
S =3   
ran1 = ''.join(random.choices(string.ascii_lowercase, k = S))  
ran2 = ''.join(random.choices(string.ascii_lowercase, k = S))

# Func for encoding
def encoding():
  word=input("Enter word to encode: ")
  if(len(word)<3):
    return word[::-1]
  else:
    return (str(ran1)+word[1:] + word[0]+str (ran2))

# func() for decoding
def decoding():
  word=input(("Enter word to decode: "))
  if(len(word)<3):
    return word[::-1]
  else:
    return word[-4]+word[3:-4]
   

choice=input("Press 1 to ENCODE\n\nPress 2 to DECODE\n")
choice=int(choice)
if(choice==1):
  encodedWord=encoding()
  print(encodedWord)
else:
    decodedWord=decoding()
    print(decodedWord)

