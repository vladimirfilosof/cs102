import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    shift = shift % 26
    if shift != 0:
        for ch in plaintext:
            if 'a' <= ch <= 'z':
                ch = chr(ord(ch) + shift)
                if not ('a' <= ch <= 'z'):
                    ch = chr(ord(ch) - ord('z') + ord('a') - 1)
            elif 'A' <= ch <= 'Z':
                ch = chr(ord(ch) + shift)
                if not ('A' <= ch <= 'Z'):
                    ch = chr(ord(ch) - ord('Z') + ord('A') - 1)
            ciphertext += ch
    else:
        return plaintext
            
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    shift = shift % 26
    if shift != 0:
        for ch in ciphertext:
            if 'a' <= ch <= 'z':
                ch = chr(ord(ch) - shift)
                if not ('a' <= ch <= 'z'):
                    ch = chr(ord(ch) + ord('z') - ord('a') + 1)
            elif 'A' <= ch <= 'Z':
                ch = chr(ord(ch) - shift)
                if not ('A' <= ch <= 'Z'):
                    ch = chr(ord(ch) + ord('Z') - ord('A') + 1)
            plaintext += ch
    else:
        return ciphertext
            
    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    
    for i in range(1, 26):
        if decrypt_caesar(ciphertext, i) in dictionary:
            best_shift = i;

    return best_shift

