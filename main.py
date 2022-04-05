ALPHEBET = '0123456789abcdefghijklmnopqrstuvwxyz'
KEY = 300


def encode(plain_text, key):
    cipher = ''
    # Iterates through the given plain_text
    for i in plain_text:
        # Lower the letter
        lower_i = i.lower()
        # If letter does occur in the ALPHEBET,
        # Encryption will be proceeded
        if lower_i in ALPHEBET:
            ciphered = ''
            # When letter index is higher than 32,
            # Letter can't change position by the KEY
            # So the ciphered letter will be started by the beginning
            if ALPHEBET.find(lower_i) > len(ALPHEBET) - (KEY + 1):
                ciphered = ALPHEBET[(ALPHEBET.find(
                    lower_i) + KEY) % len(ALPHEBET)]
            else:
                ciphered = ALPHEBET[ALPHEBET.find(lower_i) + KEY]
            # If the letter is an uppercase,
            # cipher letter will be uppercased too
            if i.isupper():
                cipher += ciphered.upper()
            else:
                cipher += ciphered
        # If letter doesn't occur in the ALPHEBET,
        # the plain letter will be added to the cipher text
        else:
            cipher += i
    return cipher


print(encode("ds Ah@d59zyxwWXZ9", 1))
