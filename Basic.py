#print("Hello,Python!")
# Number=12
# print(Number)
# Number="Ali"
# print(Number)
# Number=12.90
# print(Number)
# Number='G'
# print(Number)
# Number=["Ali",23,"Bilal",25,12.90]
# print(Number)
# Number=("Kinza","Nimra",14,89,30.78,'S')
# print(Number)
# Number={12,13,14,7,9,10}
# print(Number)
# a=12
# b=13
# print(a+b)
# print(a-b)
# print(a/b)
# print(a%b)
# print(a*b)
# print(a and b)
# print(a or b)
# print(not b)
# print(a&b)
# print(a^b)
# print(a|b)
# Age=int(input("Please Enter Your Age:",))
# if Age>=18:
#     print("Ap vote den sakte hain")
# elif Age==17:
#     print("Agle saal vote dena")
# else:
#     print("chote ghar ja or so ja")
# for count in range(10):
#     print(count)
# count=1 
# while count<100:
#     print(count) 
#     count+=1  
# def khaz(name):
#     return"Hello",name
# print(khaz("huzaifa"))
# try:
#    x=int(input("Please Enter a Value",))
#    y=10/x
# except ZeroDivisionError:
#    print("Abe saale zero se divide nhi ho ga ")
# except ValueError:
#    print("Saale Number daal")   
# kinza=open("k.txt","r")
# cont=kinza.read()
# print(cont)
# kinza.close()
# class student:
#     Name=input("Enter Your Name: ",)
# s1=student()
# s2=student()
# print(s1.Name)    
# print(s2.Name)
# class student:
#     def __init__(self,fulname):
#         self.name=fulname
# s1=student(input("Enter Your Name:",))
# print(s1.name)
# s2=student(input("Enter your Sec Name: ",))
# print(s2.name)

# import vlc
# import time  # For delay

# # Media player object
# p = vlc.MediaPlayer("k.mp3")  # Yahan apni MP3 file ka naam likho

# p.play()  # Music start

# time.sleep(10)  # 10 seconds ke liye wait karo taake music chale

# Optional: Agar stop karna ho
# p.stop()
# import random

# print(random.randint(1, 10))  # Random number between 1 and 10
# print(random.choice(["Apple", "Banana", "Cherry"]))  # Random fruit
# set={1,2,4,5,3}
# print(set)
# x, y = map(int, input("Enter two ages: ").split())  
# print(f"Ali Age is {x} and Huzaifa Age is {y}")

# print("Hello")
# m="hello"
# k=m.removeprefix("he")
# print(k)

# m=" hello "
# k=m.rstrip()
# print(k)
# import this
# num=list(range(1,100001))
# for i in num:
#     {   
#         print(i)
# #     }
# li=list(range(1,100001))
# print(min(li))
# print(max(li))
# print(sum(li))
# q7
# p_a=float(input("Enter Your Amount In $: "))
# if p_a>100:
#     dis=p_a*0.10
#     final=p_a-dis
#     print(f"Your Amount After Discount is ${final}")
# elif p_a>200:
#     dis=p_a*0.20
#     final=p_a-dis
#     print(f"Your Amount After Discount is ${final}")  
# else:
#     print(f"Your Amount  is ${p_a}")

# #q 8
# n1=int(input("Enter A Number 1: "))
# n2=int (input("Enter A Number 2: "))
# n3=int(input("Enter A Number 3: "))
# n4=max(n1,n2,n3)

# if n4:
#     print("The Number largest is ",n4)
# else:
#     print("Invalid Number")

a_n=input("Enter: ")
if a_n==65-90:
    print("Alpha")
elif a_n==97-122:
    print("small")
elif a_n ==49-57:
    print("num")
else:
    print("Invalid")    