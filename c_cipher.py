alphabets=['a' ,'b' ,'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    chiper_text=""
    for char in plain_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            chiper_text +=alphabets[new_position]
        else:
            chiper_text+=char
    print("cipher text is : ",chiper_text)

def decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabets[new_position]
        else:
            plain_text +=char
    print("Plain text is : ", plain_text)

while True:
    a = input("Type 'e' for encryption and 'd' for decryption or 'exit' to stop : ")
    if a.lower() == "exit":
        break
    text = input("Enter the text: ")
    key = int(input("Enter the shift key: "))
    if a == "e":
        encryption(plain_text=text, shift_key=key)
    elif a == "d":
        decryption(cipher_text=text, shift_key=key)

