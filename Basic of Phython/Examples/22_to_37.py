# 22. Define two string variables and initialize and print it. 
sval1 = "Girish" 
sval2 = "Chaudhary" 
print("Hello", sval1, sval2)  
print(f"Hello {sval1} {sval2}") 
# OR 
# OR 
print("Hello {sval1} {sval2}".format(sval1 = "Girish", sval2 = 
"Chaudhary")) 
# OR 
print("Hello {0} {1}".format(sval1, sval2)) 
print("Hello {} {}".format(sval1, sval2)) 
print("Hello %s %s" % (sval1, sval2))      
# OR 
# OR 
# Old style 

# 23. Define string variable and initialize a value and print it's ASCII value. 

ch = 'A' 
print(f"ASCII value of {ch} is {ord(ch)}"); 

# 24. Define integer print it ASCII character value using. Range must be 0 to 255. 
val = 65 
print(f"ASCII character is {chr(val)}"); 

# 25. Accept a boolean value and print it. 
bval = True 
print(f"value is {bval}") 

#26. Accept a string value and print it. 
sval = input("Enter your name = ") 
print(f"Hello, {sval}") 

#27. Accept an integer value and print it. 
ival = int(input("Enter integer value = ")) 
print(f"Value is {ival}") 

#28. Accept a float value and print it. 
fval = float(input("Enter float value = ")) 
print(f"Value is {fval}") 

#29. Accept a two values and store in thried variable and print addition of them. 
val1 = int(input("Enter 1st value = ")) 
val2 = int(input("Enter 2nd value = ")) 
sum = val1 + val2; 
print(f"Sum of {val1} and {val2} = {sum}") 

#30. Accept a two values print addition of them without third variable. 
val1 = int(input("Enter 1st value = ")) 
val2 = int(input("Enter 2nd value = ")) 
print(f"Sum of {val1} and {val2} = {val1 + val2}") 

#31. Accept an integer value and print the last digit. 
val = int(input("Enter a value = ")) 
ld = val % 10 
print(f"Last digit of {val} is {ld}") 

#32. Accept an integer value and print the second last digit. 
val = int(input("Enter a value = ")) 
val = val // 10 
sld = val % 10 
print(f"Second Last digit is {sld}") 

#33. Accept a float value and print the digits after decimal point.  
# Ex: 35.567  --> Result: 0.567 
fval = float(input("Enter a float value = ")) 
ival = int(fval) 
print(f"Avleu after decimal point is {fval - ival}") 

#34. Accept three characters and print the in a reverse way.    
# Ex: 'A'    'B'     'C'  --> Result: 'C'    'B'     'A' 
ch1 = input("Enter 1st character = ") 
ch2 = input("Enter 2nd character = ") 
ch3 = input("Enter 3rd character = ") 
print(f"{ch3} {ch2} {ch1}")