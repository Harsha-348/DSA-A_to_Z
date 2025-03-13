##Valid palindrome

def check_palindrome(n):
    left = 0
    right = len(n)- 1

    while left < right :
        
        if not n[left].isalnum():
            left += 1
        elif not n[right].isalnum():
            right -= 1
        elif n[left].lower() != n[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True

s = "A man, a plan, a canal: Panama"
print(check_palindrome(s))

