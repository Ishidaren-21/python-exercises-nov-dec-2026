def primecheck(num):
    if num<=1:
        return "Not a Prime Number"
    else:
        for i in range(2,num):
            if num%i==0:
                return "Not a Prime Number"
        else:
                return "Prime Number"

n=int(input("Enter a Number : "))
print(primecheck(n))
