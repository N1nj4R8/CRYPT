# -*- coding: UTF-8 -*-

"""
    CRYPT, Encryption/Decryption Tool
    Copyright (C) 2022  Ninja Left

    CRYPT is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    CRYPT is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with CRYPT.  If not, see <https://www.gnu.org/licenses/>.
"""

from __future__ import annotations
import os
import sys
import time
import base64
import hashlib
from re import search
from pathlib import Path
import passlib.hash as passlibHash
from string import ascii_letters, ascii_uppercase
from tqdm import tqdm

from colorama import Fore

grn = Fore.GREEN
wte = Fore.WHITE
ylo = Fore.YELLOW

default_path = f".{os.sep}Results{os.sep}Results.txt"


def cl():
    os.system("cls" if sys.platform == "win32" else "clear")


def fileWriter(
    txt: str | dict[str, str],
    cipher: str,
    result: str | dict[str, str],
    path: str = default_path,
    cc: bool = False,
    cc_key: int | str = "Unknown",
):
    """
    Parameters:
    ---
    - txt: The input text.
    - cipher: The cipher name; 'Base64', 'Caesar Cipher', and ...
    - type: "encrypt" or "decrypt"; used for file naming.
    - result: The function's result that encrypts/decrypts the text;

    Optional:
    - path: The path to write the file; If not set, default will be used.
    - cc: checks if it's Caesar Cipher; Default is False.
    - cc_key: The key used to shift the text.
    - is_hash: Set to true if it's a hash; Default is False.
    """
    ruler = "#" * 50
    template = f"{ruler}\n\n Plain Text: {txt}\n\n {cipher}: {result}\n\n{ruler}\n"
    if cc:
        template = f"{ruler}\n\n Plain text: {txt}\n key: {cc_key}\n\n {cipher}: {result}\n\n{ruler}\n"
    path_dir = path.split(os.sep)
    path_dir.pop(-1)
    save_dir = Path(os.sep.join(path_dir))
    if not save_dir.exists():
        save_dir.mkdir(parents=True)
    with open(path, "a+") as file:
        file.write(template)


def base16_encode(txt: str) -> str:
    return base64.b16encode(txt.encode("utf-8")).decode("utf-8")


def base16_decode(b16encoded: str) -> str:
    return base64.b16decode(b16encoded.encode("utf-8")).decode("utf-8")


def base32_encode(string: str) -> str:
    return base64.b32encode(string.encode("utf-8")).decode("utf-8")


def base32_decode(encoded_bytes: str) -> str:
    return base64.b32decode(encoded_bytes.encode("utf-8")).decode("utf-8")


def base85_encode(string: str) -> str:
    return base64.b85encode(string.encode("utf-8")).decode("utf-8")


def base85_decode(a85encoded: str) -> str:
    return base64.b85decode(a85encoded.encode("utf-8")).decode("utf-8")


B64_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_encode(text: str) -> str:
    """Encodes data according to RFC4648.
    The data is first transformed to binary and appended with binary digits so that its
    length becomes a multiple of 6, then each 6 binary digits will match a character in
    the B64_CHARSET string. The number of appended binary digits would later determine
    how many "=" signs should be added, the padding.
    For every 2 binary digits added, a "=" sign is added in the output.
    We can add any binary digits to make it a multiple of 6, for instance, consider the
    following example:
    "AA" -> 0010100100101001 -> 001010 010010 1001
    As can be seen above, 2 more binary digits should be added, so there's 4
    possibilities here: 00, 01, 10 or 11.
    That being said, Base64 encoding can be used in Steganography to hide data in these
    appended digits.
    """
    data = text.encode()
    binary_stream = "".join(bin(byte)[2:].zfill(8) for byte in data)

    padding_needed = len(binary_stream) % 6 != 0

    if padding_needed:
        # The padding that will be added later
        padding = b"=" * ((6 - len(binary_stream) % 6) // 2)

        # Append binary_stream with arbitrary binary digits (0's by default) to make its
        # length a multiple of 6.
        binary_stream += "0" * (6 - len(binary_stream) % 6)
    else:
        padding = b""

    # Encode every 6 binary digits to their corresponding Base64 character
    return (
        "".join(
            B64_CHARSET[int(binary_stream[index : index + 6], 2)]
            for index in range(0, len(binary_stream), 6)
        ).encode()
        + padding
    ).decode()


def base64_decode(encoded_data: str) -> str:
    """Decodes data according to RFC4648.
    This does the reverse operation of base64_encode.
    We first transform the encoded data back to a binary stream, take off the
    previously appended binary digits according to the padding, at this point we
    would have a binary stream whose length is multiple of 8, the last step is
    to convert every 8 bits to a byte.
    """

    # In case encoded_data is a bytes-like object, make sure it contains only
    # ASCII characters so we convert it to a string object
    if isinstance(encoded_data, bytes):
        try:
            encoded_data = encoded_data.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError("base64 encoded data should only contain ASCII characters")

    padding = encoded_data.count("=")

    if padding:  # Check if the encoded string contains non base64 characters
        assert all(
            char in B64_CHARSET for char in encoded_data[:-padding]
        ), "Invalid base64 character(s) found."
    else:
        assert all(
            char in B64_CHARSET for char in encoded_data
        ), "Invalid base64 character(s) found."

    # check padding
    assert len(encoded_data) % 4 == 0 and padding < 3, "Incorrect padding"
    if padding:  # Remove padding if there is one
        encoded_data = encoded_data[:-padding]
        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )[: -padding * 2]
    else:
        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )
    data = [
        int(binary_stream[index : index + 8], 2)
        for index in range(0, len(binary_stream), 8)
    ]
    return bytes(data).decode()


# Caesar Cipher
def cc_cipher(input_string: str, key: int, alphabet: str | None = None) -> str:
    """
    Parameters:
    -----------
    *   input_string: the plain-text that needs to be encoded
    *   key: the number of letters to shift the message by

    Optional:
    *   alphabet (None): the alphabet used to encode the cipher, if not
        specified, the standard english alphabet with upper and lowercase
        letters is used
    * change [alphabet: None] to [alphabet: str]
    """

    # Set default alphabet to lower and upper case english chars
    alpha = alphabet or ascii_letters

    # The final result string
    result = ""

    for character in input_string:
        if character not in alpha:
            result += character
        else:
            # Get the index of the new key and make sure it isn't too large
            new_key = (alpha.index(character) + key) % len(alpha)

            # Append the encoded character to the alphabet
            result += alpha[new_key]

    return result


def cc_brute_force(input_string: str, alphabet: str | None = None) -> dict[str, str]:
    """
    Parameters:
    -----------
    *   input_string: the cipher-text that needs to be used during brute-force

    Optional:
    *   alphabet:  (None): the alphabet used to decode the cipher, if not
        specified, the standard english alphabet with upper and lowercase
        letters is used
    """

    alpha = alphabet or ascii_letters
    brute_force_data = dict()
    bar = tqdm(total=len(alpha) + 1, leave=False)
    for key in range(1, len(alpha) + 1):
        key *= -1
        keyMatch = cc_cipher(input_string, key, alpha)
        bar.set_description_str(f"{abs(key)}={keyMatch}")
        brute_force_data[f"Key {abs(key)}"] = keyMatch
        time.sleep(0.05)
        bar.update(1)
    bar.close()

    return brute_force_data


# Morse Code
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "&": ".-...",
    "@": ".--.-.",
    ":": "---...",
    ",": "--..--",
    ".": ".-.-.-",
    "'": ".----.",
    '"': ".-..-.",
    "_": "..--.-",
    "$": "...-..-",
    "?": "..--..",
    "/": "-..-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    "!": "-.-.--",
    " ": "/",
    "\n": "[NL]",
}  # Exclamation mark is not in ITU-R recommendation
MORSE_REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def mc_encrypt(message: str) -> str:
    encoded = ""
    for char in message.upper():
        if char in MORSE_CODE_DICT.keys():
            encoded += MORSE_CODE_DICT[char] + " "
        else:
            encoded += char + " "
    return encoded


def mc_decrypt(message: str) -> str:
    decoded = ""
    for char in message.split():
        if char in MORSE_REVERSE_DICT.keys():
            decoded += MORSE_REVERSE_DICT[char]
        else:
            decoded += char

    return decoded.capitalize()


# Baconian Cipher
encode_dict = {
    "a": "AAAAA",
    "b": "AAAAB",
    "c": "AAABA",
    "d": "AAABB",
    "e": "AABAA",
    "f": "AABAB",
    "g": "AABBA",
    "h": "AABBB",
    "i": "ABAAA",
    "j": "BBBAA",
    "k": "ABAAB",
    "l": "ABABA",
    "m": "ABABB",
    "n": "ABBAA",
    "o": "ABBAB",
    "p": "ABBBA",
    "q": "ABBBB",
    "r": "BAAAA",
    "s": "BAAAB",
    "t": "BAABA",
    "u": "BAABB",
    "v": "BBBAB",
    "w": "BABAA",
    "x": "BABAB",
    "y": "BABBA",
    "z": "BABBB",
    " ": " ",
}
decode_dict = {value: key for key, value in encode_dict.items()}


def bacon_encode(word: str) -> str:
    encoded = ""
    for letter in word.lower():
        if letter.isalpha() or letter == " ":
            encoded += encode_dict[letter]
        else:
            encoded += letter
    return encoded


def bacon_decode(coded: str) -> str:
    decoded = ""
    pattern = r"[\d\._\-&!@?]+"
    for word in coded.split():
        while len(word) != 0:
            if word[:5].isalpha():
                decoded += decode_dict[word[:5]]
                word = word[5:]
            else:
                s = search(pattern, word)
                if s:
                    decoded += word[s.start() : s.end()]
                    word = word.replace(word[s.start() : s.end()], "")
                else:
                    raise BadCharacter(f"Bad characters in {word}; Bad:{s.group()}")
        decoded += " "
    return decoded.strip().capitalize()


# Vigenère Cipher
def vig_cipher(text: str, key: str, mode: str = "encrypt" or "decrypt") -> str:
    results = ""
    keyIndex = 0
    Letters = ascii_uppercase

    for char in text:
        i = Letters.find(char.upper())
        if i != -1:
            if mode == "encrypt":
                i += Letters.find(key[keyIndex])
            else:
                i -= Letters.find(key[keyIndex])
            i %= len(Letters)

            if char.isupper():
                results += Letters[i]
            else:
                results += Letters[i].lower()
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            results += char

    return results


# Hashes
def md5(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def md5_crypt(text: str) -> str:
    return passlibHash.md5_crypt.hash(text)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def sha256_crypt(text: str) -> str:
    return passlibHash.sha256_crypt.hash(text)


def sha512(text: str) -> str:
    return hashlib.sha512(text.encode()).hexdigest()


def sha512_crypt(text: str) -> str:
    return passlibHash.sha512_crypt.hash(text)


def bcrypt(text: str) -> str:
    return passlibHash.bcrypt.hash(text)


def argon2(text: str) -> str:
    return passlibHash.argon2.hash(text)


def nthash(text: str) -> str:
    return passlibHash.nthash.hash(text)


def pbkdf2_256(text: str) -> str:
    return passlibHash.pbkdf2_sha256.hash(text)


def pbkdf2_512(text: str) -> str:
    return passlibHash.pbkdf2_sha512.hash(text)


def get_input() -> str:
    lines = []
    print(
        f"{ylo}  [!] To stop taking inputs, use 'CTRL+D' (linux) or 'CTRL+Z+Enter' (windows)."
    )
    print(f"\n{grn}   [+] Data:{wte} ", end="")

    while True:
        try:
            text = input()
            if text:
                lines.append(text)

        except EOFError:
            if len(lines) >= 1:
                return "\n".join(lines)

        except:
            raise
