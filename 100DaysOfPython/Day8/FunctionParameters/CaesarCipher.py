# In this python project we are going to build a program - Caesar's Cipher

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Please type 'encode' for encoding the message and 'decode' for decoding the message: ").lower()
shift = int(input("Type a number of your choice: "))
message = input("Enter the message you want to encode: ").lower()


def encrypt(message, shift):
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
                newIndex -= 26
                encodedMessage += alphabets[newIndex]
            else:
                encodedMessage += alphabets[newIndex]
    return encodedMessage


def decrypt(message, shift):
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
    return decodedMessage


encodedMessage = encrypt(message=message, shift=shift)
decodedMessage = decrypt(message=encodedMessage, shift=shift)
print(encodedMessage)
print(decodedMessage)
