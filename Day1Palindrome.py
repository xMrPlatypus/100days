#best version
def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]

#better version
def plaindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

#not so good version
def plaindrome(x):
    x = str(x)
    container = x[::-1]
    if x == container:
        return True
    else:
        return False