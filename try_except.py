# t=(input("Enter number: "))
# try:
#     for i in range(1,11):
#         print(f"{int(t)} X {i}= {int(t)*i}")
# except:
#     print("Invalid input")
# print("hii")

try:
    num=int(input("Enter: "))
    a=[4,5]
    print(a[num])
except ValueError:
    print("number is not valid")
except IndexError:
    print("Index error")