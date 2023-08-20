#     BY USE OF BREAK
#Q7 Write a Program to print all prime numbers that fall between two numbers include both
        #(accept two number from the user)
# ###########break used huga
num1=int(input("enter your 1st number\n"))
num2=int(input("enter your 2nd number\n"))

for num in range(num1,num2+1):   #yaha num =i variable leliya hai taki wuh useer input ki 
    if num>1:                       #ki range me aajae ,fir  i=ivarible se ek or range linge
        for i in range(2,num):   #num ku +1 nhi linge same logic 
            if num%i==0:
                break
        else:
            print(num,",",end="")
