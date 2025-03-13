##Recursion
##Print N to 1 using recursion

def print_rev(n):
    if n == 0:
        return None
    print(n,end =" ")
    print_rev(n-1)

a = int(input("enter the number: "))
print_rev(a)