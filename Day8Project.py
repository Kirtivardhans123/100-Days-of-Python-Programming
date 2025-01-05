def caesar_cipher(encryption_type, message, shift):
    result = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Ensure the shift stays within 0-25
    shift %= 26
    if encryption_type == "decode":
        shift *= -1

    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            position = alphabet.index(char.lower())
            new_position = (position + shift) % 26
            new_char = alphabet[new_position]
            # Convert back to uppercase if needed
            if is_upper:
                new_char = new_char.upper()
            result += new_char
        else:
            # Non-alphabetic characters stay unchanged
            result += char

    print(f"Here's the {encryption_type}d text: {result}")


# User inputs
print("Welcome to the Caesar Cipher!")
should_continue=True
while should_continue:
    encryption_type = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if encryption_type in ["encode", "decode"]:
        message = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        caesar_cipher(encryption_type, message, shift)
    else:
        print("You chose the wrong type of encryption.")
    restart = input("Type 'yes' to continue or 'no' to exit:\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")