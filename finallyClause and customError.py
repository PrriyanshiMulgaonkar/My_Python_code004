# def clause():
#     try:
#         t=[1,2,3,4]
#         i=int(input("Enter index: "))
#         print(t[i])
#         return 1
#     except:
#         print("Some error occured")
#         return 0

#     finally:
#         print("I am always executed")
# a=clause()
# print(a)


# custom error
a=(input("Enter num btw 9 and 12 or quit: "))
try:
    if (int(a)<9 or int(a)>12):
        raise ValueError("Value should be btw 9 and 12")
except:
    if (a!="quit"):
        raise ValueError("Enter wrong string")