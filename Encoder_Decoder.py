alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
flag = True
while flag:
    ask = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:")).lower()
    message = str(input("Enter the message :")).lower()
    shift = int(input("Enter the shift digit :"))

    def main(type):
        encoded_message = ""
        decoded_message = ""
        if type == 'encode':
            for i in message:
                loc = alphabet.index(i)
                en_list.append(alphabet[(loc + shift)])
            for i in en_list:
                encoded_message += i
            print(f"Encoded message: {encoded_message}")
        else:
            for i in message:
                loc = alphabet.index(i)
                de_list.append(alphabet[(loc - shift)])
            for i in de_list:
                decoded_message += i
            print(f"Decoded message: {decoded_message}")

    if ask == 'encode':
        en_list = []
        main("encode")

    elif ask == 'decode':
        de_list = []
        main("decode")

    else:
        print("Please enter a valid input")
    cont = str(input("Type yes or no for further continuing\n")).lower()
    if cont == 'no':
        flag = False
    elif cont == 'yes':
        flag = True
    else:
        print("Please enter a valid input")