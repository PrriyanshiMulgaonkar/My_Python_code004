count=0
question = ["Q1. Capital of MP. \n a. Bhopal \n b. Indore \n c. Ujjain"]
print(question)
answer=input(" ")
if answer=="A" or answer=="a":
    print("Correct answer")
    count=count+1
else :
    print("Wrong answer")
question2= ["Q1. Capital of India. \n a. Bhopal \n b. Indore \n c. Delhi"]
print(question2)
answer=input(" ")
if answer=="C" or answer=="c":
    print("Correct answer")
    count=count+1
else :
    print("Wrong answer")
print("Your score: ",count)