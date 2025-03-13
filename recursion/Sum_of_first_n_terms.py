##Recursion
##Sum of first n terms

def first_terms(n):
    if n == 0:
        return 0
    else: 
        return n ** 3 + first_terms(n-1)

a = int(input("enter the number:"))
print(first_terms(a))
