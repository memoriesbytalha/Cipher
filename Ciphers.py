import art 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

def caesar(text, shift, action):
    result = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if action == "encrypt":
                new_position = (position + shift) % len(alphabet)
            elif action == "decrypt":
                new_position = (position - shift) % len(alphabet)
            new_letter = alphabet[new_position]
            result += new_letter
    return result

direction = input("What do you want to do? Encrypt (e)/ Decrypt (d): ").lower()
text = input("Type your message: ")
shift = int(input("Enter the shift you want to take: "))

if direction == "e":
    encrypted_message = caesar(text, shift, "encrypt")
    print("Encrypted message:", encrypted_message)
elif direction == "d":
    decrypted_message = caesar(text, shift, "decrypt")
    print("Decrypted message:", decrypted_message)
else:
    print("Please enter the correct command.")
