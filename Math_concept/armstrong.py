def armstrong(self,n):

  k = len(str(n))
  original = n
  total = 0

  while n > 0:
    ld = n % 10
    total += (ld ** k)
    n = n // 10
    
  if total == original:
    return True
  else:
    return False
   



