# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("Step4")
#     print("Step5")

# printSteps()
# printSteps()
# printSteps()

# print()

# def printSum(a,b):
#     print("The value of a is:",a)
#     print("The value of b is:",b)

# printSum(10,20)
# printSum(b=100,a=200)

# def mulNum(a,b=50):
#     print(a*b)

# mulNum(45,20)

# def printMul(*a):
#     total = 1
#     for i in a:
#         total = total * i
#     print(total)
 
# printMul(4, 3, 5, 3, 32, 4, 23, 54, 3, 65)
 
# def sayHello(name):
#     print("Hello",name)

# def sayMorning(x,y):
#     print("Good morning")
#     x(y)

# sayMorning(sayHello,"Priyanka")


# def outer():
#     def inner():
#         print("hello from inner!")
#     inner()

# outer()
# inner()

# a=10

# def func1():
#     a=15
#     print("The value of a is:",a)

# func1()
# print(a)

# def dummy():
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     return 55
#     print("Step4")
#     print("Step5")

# a=dummy()
# print(a)

# def printMul(a,b):
#     return a*b 

# print(printMul(3,printMul(4,printMul(2,printMul(5,5)))))

# a=input()
# print(a)

# print(78)

# l1=[1,2,3,4,5,4,3,2,1]

# print(l1[::-1])
# l1.reverse()
# print(l1)

# if l1==l1[::-1]:
#     print("Pal")
# else:
#     print("No Pal")