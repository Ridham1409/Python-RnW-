# Way 1

print("Enter a Value 1 = ")
val1 = int(input())
print("Enter a Value 2 = ")
val2 = int(input())
print("Enter a Value 3 = ")
val3 = int(input())

if (val1 > val2):
    if (val1 > val3):
        print(f"{val1} is biggest")
elif (val2 > val1):
    if (val2 > val3):
        print(f"{val2} is biggest")
else:
    print("There is more than one biggest number")
    
#or Way 2....
    
# if (val1 > val2 and val1 > val3): print(f"{val1} is biggest")
# elif (val2 > val1 and val2 > val3): print(f"{val2} is biggest")
# else: print("Value is zero")