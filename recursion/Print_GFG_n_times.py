##Recursion

def gfg(n):
    if n == 0:
        return
    gfg(n-1)
    print("GFG",end =" ")


a = int(input("enter the number:"))
gfg(a)





