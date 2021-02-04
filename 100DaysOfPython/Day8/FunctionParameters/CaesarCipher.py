# In this python project we are going to build a program - Caesar's Cipher

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def caesar():
    direction = input("Type 'encode' for encypting the message. Type 'decode' for decrypting the message: ")
    shift = int(input("Enter a number between 1 and 25: "))

    if direction == "encode":
        message = input("Enter the message you want to encrypt: ").lower()
        encodedMessage = ""
        for i in range(len(message)):
            if message[i] == " ":
                encodedMessage += " "
            elif message[i] not in alphabets:
                encodedMessage += message[i]
            else:
                index = alphabets.index(message[i])
                newIndex = index + shift
                if newIndex > 25:
                    newIndex -= len(alphabets)
                    encodedMessage += alphabets[newIndex]
                else:
                    encodedMessage += alphabets[newIndex]
        print("Your encrypted message is {}".format(encodedMessage))
    elif direction == "decode":
        message = input("Enter the message you want to decrypt: ").lower()
        decodedMessage = ""
        for i in range(len(message)):
            if message[i] == " ":
                decodedMessage += " "
            elif message[i] not in alphabets:
                decodedMessage += message[i]
            else:
                index = alphabets.index(message[i])
                newIndex = index - shift
                decodedMessage += alphabets[newIndex]
        print("Your decrypted message is {}".format(decodedMessage))
    else:
        print("Invalid Option! Please try again!")


isTrue = True

while(isTrue):
    caesar()
    choice = input("Do you want to try again? Type 'yes' or 'no': ").lower()
    if choice == "yes":
        caesar()
    else:
        print("Thank you for using Caesar's Cipher!")
        isTrue = False