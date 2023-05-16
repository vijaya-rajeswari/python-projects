num=int(input("enter:"))
def sum_digits(num):
    s=0
    while num>0:
        s=s+num%10
        num//=10
        
