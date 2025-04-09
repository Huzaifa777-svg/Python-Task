# 001 Ask for the user’s first name and display the output message Hello [First Name] .
'''I=input("Enter Your Name: ")
print("Hello",I)
print(f"Hello{I}")'''
#002 Ask for the user’s first name and then ask for  surname and display the output message Hello [First Name] [Surname]. 
'''I=input("Enter Your Name: ")
J=input("Enter Your SureName: ")
print(f"Hello {I} {J}")
print("Hello",I,J)'''
#003  Write code that will display the joke “What do you call a bear with no teeth?” and on the next line display the answer “A gummy bear!” Try to create it using only one line of code. 
'''print("What do you call a bear with no teeth?\nA gummy bear!")'''
#004  Ask the user to enter two numbers. Add them together and display the answer as The total is [answer].
'''A=int(input("enter a number: "))
B=int(input("Enter a Number: "))
s=A+B
print("The Total Answer is",s)'''
#005  Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as The answer is [answer]. 
'''a=int(input("Enter Nubmer: "))
b=int(input("Enter Nubmer: "))
c=int(input("Enter Nubmer: "))
print("The Answer is:",(a+b)*c)'''
#006 Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a userfriendly format. 
'''a=int(input("how many slices of pizza the you started 😍:"))
b=int(input("how many slices they have eaten😡 : "))
c=a-b
print(c)'''
#007  Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be [new age]. 
'''a=int(input("Enter Your Age: "))
b=input("Enter Your Name: ")
c=a+1
print(f"{b} next birthday you will be {c}")'''
#008 Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.
'''a=int(input("Enter Total Price: "))
b=int(input("How many dinner there are: "))
c=a/b
print(f"person must pay {c}")'''
#009 Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days. 
'''a=int(input("Enter Number Of Days: "))
min="60 Minutes"
ho="24 hours"
sec="60 seconds"
print(f"{ho}, {min} and {sec} are in that number of days {a}")'''
#0010There are 2,204 pounds in a kilogram. Ask theuser to enter a weight in kilograms and convert it to pounds.  
'''a=float(input("Enter a Weight in kg: "))
p=a*2.204
print("The pound is:",p)'''
#011  Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.
'''a=int(input("Enter a Number Greater Then 100: "))
b=int(input("Enter A Number Less Than 10: "))
c=a//b
print("The answer is: ",c)'''
#012 Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.
'''a=int(input("Enter Your First Number: "))
b=int(input("Enter Your Second Number: "))
if a>b:
    print(f"The order Number is {b} , {a}")
elif a<b:
    print(f"The order Number is {a} , {b}")
else:
    print("both number are equal")  '''

#013  Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”. 
'''a=int(input("Enter a Number Under 20: "))
if a>20:
    print("Too High")
else:
    print("Thank You")'''
#014Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”. 
'''a=int(input("Enter a Number Between 10 to 20: "))
if a>=10 and a<=20:
    print("Thank you")
else:
    print("Incorrect")'''
#015 Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”. 
'''a=input("Enter your favourite colour : ")
if a=="Red" or a=='RED' or a=='ReD' or a=='red':
    print("I like red too")
else:
    print(f"I don’t like {a}")'''
#016 Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not answer yes to the first question, display the answer “Enjoy your day”. 
'''a=input("It Is Raining: ")
a=str.lower(a)
if a=="yes":  
 
    b=input("it is windly?")
    b=str.lower(b)
    if b=="yes":
        print("It is too windy for an umbrella")
    else:
        print("“Take an umbrella”")
else:
    print("Enjoy your day!")'''
#017 Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”. 
'''a=int(input("Enter A Number 1,2 or 3: "))
if(a==1):
    print("Thank you")
elif a==2:
    print("well done")
elif a==3:
    print("correct")
else:
    print("Error Message")'''
#020  Ask the user to enter their first name and then display the length of their name.
'''a=input("Enter your first name: ")
print(len(a))'''
#021 Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of whole name. 
'''a=input("Enter Your First Name: ")
b=input("Enter Your Sure Name: ")
n=a+" "+b
print(len(n))'''
#022  Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result. 
'''a=input("Enter Your First Name: ").lower()
b=input("Enter Your Sure Name: ").lower()
a=a.title()
b=b.title()
c=a+" "+b
print(c)'''
#023  Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1). 
