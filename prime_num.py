#ajit kerle
#given number is prime or not
num=int(input("Enter the number:"))
if num>1:
    for i in range(2,int(num/2)+1):
        if (num%1)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number") 
else:
    print(num,"is not a prime number")           