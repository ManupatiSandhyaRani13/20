def is_palindrome(string):
    string1=string[::-1]
    return string1
string=input("Enter a string : ")
res=is_palindrome(string)
if res==string:
    print("Palindrome")
else:
    print("Not palindrome")