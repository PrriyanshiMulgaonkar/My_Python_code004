marks=[10,20,30,20,34,56,78]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Awesome")
#     index=index+1

for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("awesome")
