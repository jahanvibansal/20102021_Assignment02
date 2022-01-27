#QUESTION NO. 1

#Given string:
a="Python is a case sensitive language"

#a) Printing length of string:
print(len(a))

#b) Reversing the order of string:
print(a[::-1])

#c) Storing "a case sensitive" in a new string b: 
b=a[10:26]
print(b)

#d) Replacing "a case sensitive" with "object oriented"
print(a.replace("a case sensitive", "object oriented"))

#e) Finding index of substring "a":
print(a.find("a"))

#f) Removing white spaces from the string given:
print(a.replace(" ",""))
___________________________________________________________________________________________________

#QUESTION NO. 2:-

#Storing details in different variables:
name="Jahanvi"
SID=int(20102021)
dep="Civil"
CGPA=float(7)

#Using string formatting for printing the above variables: 
print("""Hey, %s Here!
My SID is %d 
I am from %s department and my CGPA is %f""" %(name, SID, dep, CGPA))
___________________________________________________________________________________________________

#QUESTION NO. 3:-

#Calculating the following for a=56 and b=10
a=56
b=10

#a) Calculating a&b  
print(a&b)

#b) Calculating a|b
print(a|b)

#c) Calculating a^b
print(a^b)

#d) Calculating left shift of both a and b with 2 bits
print(a<<2, b<<2)

#e) Calculating right shift of a with 2 bits and b with 4 bits
print(a>>2,b>>4)
___________________________________________________________________________________________________

#QUESTION NO. 4:-

#Taking 3 inputs from user as integer values
a=int(input("Enter First number "))
b=int(input("Enter Second number "))
c=int(input("Enter Third number "))

#Placing the integers in a list
arr=[a,b,c]
#Using max function
print("the greatest of three numbers entered is: ",max(arr))
___________________________________________________________________________________________________

#QUESTION NO. 5:-

#Taking input from the user
a=str(input("Enter a word to check "))

#Using in function
if "name" in a:
	print("Yes")
else:
 	print("No")

___________________________________________________________________________________________________


#QUESTION 6:-

#Taking input from the user:
a=int(input("Enter length of first side "))
b=int(input("Enter length of second side "))
c=int(input("Enter length of third side "))
#Applying condition for possibility of a triangle
#If any of the three lengths is greater than the sum of the other two,
#then you cannot form a triangle.
if(a+b>c and b+c>a and c+a>b):
	print("Yes")
else:
	print("No")
___________________________________________________________________________________________________

#OUTPUTS TO THE CODES PROVIDED ABOVE :-

---------------------------------------------------------------------------------------------------
C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\calculator.py"
35
egaugnal evitisnes esac a si nohtyP
a case sensitive
Python is object oriented language
10
Pythonisacasesensitivelanguage
>>>
---------------------------------------------------------------------------------------------------

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\calculator.py"
Hey, Jahanvi Here!
My SID is 20102021
I am from Civil department and my CGPA is 7.000000
>>>
---------------------------------------------------------------------------------------------------

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\calculator.py"
8
58
50
224 40
14 0
>>>
---------------------------------------------------------------------------------------------------

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\calculator.py"
Enter First number 52
Enter Second number 96
Enter Third number 45
the greatest of three numbers entered is:  96
>>>
---------------------------------------------------------------------------------------------------

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\calculator.py"
Enter a word to check namespace
Yes

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\calculator.py"
Enter a word to check jahanvi
No
>>>
---------------------------------------------------------------------------------------------------

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\calculator.py"
Enter length of first side 45
Enter length of second side 62
Enter length of third side 41
Yes

C:\Users\bansa>python "C:\Users\bansa\Desktop\hello world\calculator.py"
Enter length of first side 48
Enter length of second side 85
Enter length of third side 2
No
>>>
---------------------------------------------------------------------------------------------------