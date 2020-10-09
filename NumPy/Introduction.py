def countCharacterType(str):
    # Declare the variable vowels,
    # consonant, digit and special
    # characters
    vowels = 0
    consonant = 0
    words=0

    # str.length() function to count
    # number of character in given string.
    for i in range(0, len(str)):

        ch = str[i]

        if ((ch >= 'a' and ch <= 'z') or
                (ch >= 'A' and ch <= 'Z')):

            # To handle upper case letters
            ch = ch.lower()

            if (ch == 'a' or ch == 'e' or ch == 'i'
                    or ch == 'o' or ch == 'u'):
                vowels += 1
            else:
                consonant += 1

        else:
            data = str.read()
            words = data.split()

    print("Vowels:", vowels)
    print("Consonant:", consonant)
    print("words:", len(words))


# Driver function.
file1 = open("E:\data.txt", "rt")
str = file1.read()
countCharacterType(str)