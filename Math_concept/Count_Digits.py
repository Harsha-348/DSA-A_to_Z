#Count Digits

def count_digit(n):
    count = 0
    original = n

    while n > 0:
        ld = n % 10

        if ld != 0 and original % ld == 0:
            count += 1

        n = n // 10

    return count
    
a = 23
print(count_digit(a))



#2nd method
class Solution:
    def countDigits(self, n):
    #  code here 
    
        count = 0
        original = n
    
        while n > 0:
            ld = n % 10
        
            if ld >= 0:
                count += 1
            
            n = n // 10
    
        return count
