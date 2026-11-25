def armstrong(num):
    digits=str(num)
    power=len(digits)
    total=sum(int(digit)**power for digit in digits)
    if total==num:
        return (f"{num} is Armstrong Number")
    else:
        return (f"{num} is not an Armstrong Number")

n=int(input("Enter a Number : "))
print(armstrong(n))
