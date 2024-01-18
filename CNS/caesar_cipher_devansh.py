def shift(x: str, s):
    if x.isupper():
        return chr(ord('A') + (ord(x) - ord('A') + s) % 26)
    elif x.islower():
        return chr(ord('a') + (ord(x) - ord('a') + s) % 26)
    else:
        return x


def caesar(message, s):
    return ''.join([shift(x, s) for x in list(message)])


def encrypt(message, s):
    print('Encrypted Message:', caesar(message, s))


def decrypt(message, s):

    print('Decrypted Message:', caesar(message, -s))


def decipher(cipher):
    print('\nBrute Force Decrypt:')
    for i in range(26):
        print('Shift:', i, ': Message:', caesar(cipher, -i))


def main():
    while True:
        print('1. Encrypt')
        print('2. Decrypt with key')
        print('3. Decrypt by Brute Force')
        print('4. Exit')
        option = int(input("Choice: "))

        match (option):
            case 1:
                message = input("Enter message to encrypt... ")
                s = int(input("Enter amount of shift... ")) % 26
                encrypt(message, s)
            case 2:
                message = input("Enter encrypted message... ")
                s = int(input("Enter amount of shift... ")) % 26
                decrypt(message, s)
            case 3:
                message = input("Enter encrypted message... ")
                decipher(message)
            case 4:
                return

        print('-'*20)


if __name__ == '__main__':
    main()
