def Is_pallindrome (x):
    if x == x[::-1]:
        print("Yes its a pallindrome")
    else:
        print("Its not a pallindrome")

word = input("Enter a word to check if its a pallindrome or not : ")
Is_pallindrome(word)