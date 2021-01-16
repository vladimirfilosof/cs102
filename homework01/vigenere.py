def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    ABC_length = 26
    shift = 0

    if keyword != "" and keyword.lower() != "a":
        for i in range(0, len(plaintext)):
            shift = ord(keyword[i % len(keyword)].lower()) - ord("a")
            ch = plaintext[i]
            if "a" <= ch <= "z":
                ch = chr(ord(ch) + shift)
                if not ("a" <= ch <= "z"):
                    ch = chr(ord(ch) - ord("z") + ord("a") - 1)
            elif "A" <= ch <= "Z":
                ch = chr(ord(ch) + shift)
                if not ("A" <= ch <= "Z"):
                    ch = chr(ord(ch) - ord("Z") + ord("A") - 1)
            ciphertext += ch
    else:
        return plaintext

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    shift = 0

    if keyword != "" and keyword.lower() != "a":
        for i in range(0, len(ciphertext)):
            shift = ord(keyword[i % len(keyword)].lower()) - ord("a")
            ch = ciphertext[i]
            if "a" <= ch <= "z":
                ch = chr(ord(ch) - shift)
                if not ("a" <= ch <= "z"):
                    ch = chr(ord(ch) + ord("z") - ord("a") + 1)
            elif "A" <= ch <= "Z":
                ch = chr(ord(ch) - shift)
                if not ("A" <= ch <= "Z"):
                    ch = chr(ord(ch) + ord("Z") - ord("A") + 1)
            plaintext += ch
    else:
        return ciphertext

    return plaintext
