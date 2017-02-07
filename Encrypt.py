"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
plaintxt = 'Computer Science Makes the World go round but it doesn/t make the world round itself!'
def Encrypt(AnyString):
    newstr = ""
    vowels = 'aeiou'
    for i in AnyString.lower():
        if i in vowels:
            newstr = newstr + ""
        else:
            newstr = newstr + i
    return newstr
NoVowels = Encrypt(plaintxt)
print(Encrypt(plaintxt))

"""Write an encryption code that you make up and run it for the variable NoVowels"""
