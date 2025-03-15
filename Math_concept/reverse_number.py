#Reverse a number
def reverse_num(x):

  rev = 0

  if x < 0:
    rev = int(str(x)[1:][::-1]) * -1
  else:
    rev = int(str(x)[::-1]) 

  if rev < -2**31 or rev > 2 ** 31 - 1 : 
    return 0

  return rev

a = 123456789
print(reverse_num(a))





