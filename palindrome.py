#palindrome using function
def isPalindrome(s):
    # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are
    if (s == rev):
        return True
    return False
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")