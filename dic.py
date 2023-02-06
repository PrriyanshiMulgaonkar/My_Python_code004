dict={
    "mobile": "android",
    "spoon" : "object"
}

e2={
    "neckband": "device"
}
print(dict["mobile"])
print(dict.keys())

for key in dict.keys():
    print(f"The value to key {key} is {dict[key]}")


for key, value in dict.items():
  print(f"The value corresponding to the key {key} is {value}") 

# methods
dict.update(e2)
# del dict["mobile"]
dict.popitem() #del last item
# dict.clear()
# dict.pop(122)
print(dict)