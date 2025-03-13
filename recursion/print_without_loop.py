##Recursion

#Print 1 To N Without Loop

def without_loop(n):
    if n == 0:
        return None
    without_loop(n-1)
    print(n,end=" ")

a = int(input("enter the number: "))
without_loop(a)