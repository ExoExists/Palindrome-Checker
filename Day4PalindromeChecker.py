print("-~-~-Welcome to palindrome checker-~-~-")
userWord = input("Enter the word to check for a palindrome: ")

def checkPalindrome(word):

    wordLowered=word.lower()
    length=len(word) -1 
    
    #normal word without spaces
    j=0
    normalWord=''
    while j<=length:
       if wordLowered[j]!=" ":
        normalWord=normalWord+wordLowered[j]
        j+=1
       else:
        normalWord=normalWord
        j+=1

    #reverse word without spaces
    reverseWord=''
    i = length
    while i<=length and i!=-1:
       if wordLowered[i]!=" ":
        reverseWord=reverseWord+wordLowered[i]
        i-=1
       else:
        reverseWord=reverseWord
        i-=1

    #check for palindrome
    if reverseWord==normalWord:
        return(word + " is a palindrome!")
    else:
        return(word + " is not a palindrome!")

print(checkPalindrome(userWord))