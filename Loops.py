# i=0

# while i>5:
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     i+=1

# no of iteration --> 
# i--> 0


# str1="Hello world"

# # print(str1[6])
# print(len(str1))

# For Loop 

# str1="Virat"

# for i in str1:
#     print(i)
#     print("------------------")

# i ---> 


# for i in range(4,15,3):
#     print(i)
#     print("-------------")

# i=0

# while i<100:
#     if i<=25:
#         break
#     print(i)
#     i+=1

# i = 0
# No of Iteration: 26

# for i in range(1,101):
#     print(i)
#     if i==40:
#         continue

# i=1
# while i<=10:
#     if i==5:
#         continue
#     print(i)
#     i+=1

# no of iteration: infinite, 1,2,3,4

# For 

# for i in range(1,101):
#     print(i)

# secret_number=33
# NotFound=True

# while NotFound:
#     inp=int(input("Enter the number: "))
#     if secret_number==inp:
#         print("You Won!")
#         NotFound=False
#     else:
#         print("Try again!")


# for i in range(1,6):
#     for j in range(1,6):
#         print("i=",i,'j=',j)


# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")

# for i in range(1,6):
#     print("* "*i)

# print("Hello"*4)

# print("Hello",end="")
# print("Hi",end="")
# print("World")

# print("* * * * ")
# print("*     * ")
# print("*     * ")
# print("* * * * ")

inp=int(input("Enter the length: ")) #-->5//2--->2+1

for i in range(1,inp+1):
    for j in range(1,inp+1):
        if j==1 or j==inp:
            print("* ",end='')
        elif i==j and i<=inp//2+1:
            print("* ",end='')
        elif j+i==inp+1 and i<=inp//2+1:
            print("* ",end='')
        else:
            print("  ",end='')
    print()

