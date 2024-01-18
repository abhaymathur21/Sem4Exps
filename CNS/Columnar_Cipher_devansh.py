import numpy as np

message = input("Enter message to encrypt: ").upper()
key = input("Enter key for encryption: ").upper()


def encrypt(message, key):
    k = len(key)
    r = len(message) % k

    padded_message = "_".join(message.split()) + "_" * (k - r if r != 0 else 0)

    s_key = sorted(key)
    key_order = [s_key.index(x) for x in list(key)]
    message_mat = np.transpose(
        [list(padded_message[x : x + k]) for x in range(0, len(padded_message), k)]
    ).tolist()

    encrypted_mat = sorted(zip(key_order, message_mat))
    encrypted_message = "".join(["".join(m) for o, m in encrypted_mat])

    return encrypted_message


encrypted_message = encrypt(encrypt(message, key), key)
print("Encrypted Message:", encrypted_message)


def decrypt(message, key):
    k = len(key)
    d = len(message) // k

    if len(message) % k != 0:
        print("Invalid Key")
        return

    s_key = sorted(key)
    key_order = [s_key.index(x) for x in list(key)]
    message_mat = [list(message[x : x + d]) for x in range(0, len(message), d)]
    dec_mat = np.transpose([message_mat[i] for i in key_order]).tolist()

    decrypted_message = "".join(["".join(m) for m in dec_mat])

    return decrypted_message


decrypted_message = decrypt(decrypt(encrypted_message, key), key).replace("_", " ")
print("Decrypted Message:", decrypted_message)
