"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
def Encrypt(AnyString):
    newstr = ""
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in AnyString.lower():
        if i in vowels:
            newstr = Anystring.replace(i, "")
        return newstr
NoVowels = Encrypt(newstr)

print("Computer Science Makes the World go round but it doesn't make the world round itself!")




"""Write an encryption code that you make up and run it for the variable NoVowels"""
