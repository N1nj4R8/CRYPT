# -*- coding: UTF-8 -*-
"""
    CRYPT Brute Forcer, Password Hash Brute Forcing Tool
    Copyright (C) 2022  Ninja Left

    CRYPT Brute Forcer is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    CRYPT Brute Forcer is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with CRYPT Brute Forcer.  If not, see <https://www.gnu.org/licenses/>.
"""

import subprocess
import sys
import os
import hashlib
from passlib.context import CryptContext
from pathlib import Path
from tqdm import tqdm

# Colors
grn = "\x1b[0;32m"  # Green
red = "\x1b[0;31m"  # Red
wte = "\x1b[0;37m"  # White
ppl = "\x1b[0;35m"  # Purple (Magenta)
ylo = "\x1b[0;36m"  # Yellow
blu = "\x1b[0;36m"  # Blue
cyn = "\x1b[0;36m"  # Cyan
gry = "\x1b[0;90m"  # Grey (Light Black)

default_path = f".{os.sep}Results{os.sep}Results.txt"


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


def cl():
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform == "linux":
        os.system("clear")


def md5(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def sha512(text: str) -> str:
    return hashlib.sha512(text.encode()).hexdigest()


def crackHash_BruteForce(
    hash_input: str,
    length: int,
    ramp: bool,
    start_length: int = 1,
    have_letters: bool = True,
    have_symbols: bool = True,
    have_numbers: bool = True,
    hash_type: str = "other",
):
    """
    ----
    Parameters
    ----------
    * hash: Hash to crack.
    * length: Length of string to iterate through.
    * ramp: If true, ramp up from start_length till length; Otherwise, iterate over current length values.
    * have_letters: Include uppercase & lowercase letters; default: True.
    * have_symbols: Include symbols; default: True.
    * have_numbers: Include 0-9 digit; default: Trues.
    * start_length: The length of the string to begin ramping through; default: 1.
    * hash_type: Type of hash trying to crack.
    """
    from brute import brute

    bar = tqdm(leave=True)
    results = "Not found"
    ctx = CryptContext(
        [
            "md5_crypt",
            "ldap_salted_md5",
            "sha256_crypt",
            "ldap_salted_sha256",
            "sha512_crypt",
            "ldap_salted_sha512",
            "bcrypt",
            "argon2",
            "nthash",
            "pbkdf2_sha256",
            "pbkdf2_sha512",
        ]
    )
    for password in brute(
        start_length=start_length,
        length=length,
        letters=have_letters,
        symbols=have_symbols,
        numbers=have_numbers,
        ramp=ramp,
    ):
        bar.set_description_str(f"Testing '{password}'")
        if hash_type == "md5":
            check = md5(password)
        elif hash_type == "sha256":
            check = sha256(password)
        elif hash_type == "sha512":
            check = sha512(password)
        else:
            check = ctx.verify(password, hash_input)

        if check == hash_input:
            bar.set_description(f"Matched '{password}'")
            results = password
            break

        bar.update()
    bar.close()

    return results


def crackHash_WordList(hash_input: str, file_path: str, hash_type: str = "other"):
    """
    ----
    Parameters
    ----------
    * hash_input: Hash to crack.
    * file_path: Path to wordlist.
    * hash_type: Type of hash trying to crack.
    """
    ctx = CryptContext(
        [
            "md5_crypt",
            "ldap_salted_md5",
            "sha256_crypt",
            "ldap_salted_sha256",
            "sha512_crypt",
            "ldap_salted_sha512",
            "bcrypt",
            "argon2",
            "nthash",
            "pbkdf2_sha256",
            "pbkdf2_sha512",
        ]
    )
    results = "Not found"
    if sys.platform == "linux":
        file_size = (
            subprocess.check_output(["wc", "-l", file_path])
            .decode("utf-8")
            .split(" ")[0]
            .replace("L", "")
        )
    else:
        file_size = (
            subprocess.check_output(["find", "/c", "/v", "", file_path])
            .decode()
            .split(" ")[-1]
        )
    file_size = int(file_size)

    bar = tqdm(total=file_size, unit="Lines", leave=True)
    with open(file_path, "r", encoding="UTF-8") as file_obj:
        for password in file_obj:
            password = password.strip()
            bar.set_description(f"Testing '{password}'")
            if hash_type == "md5":
                check = md5(password)
            elif hash_type == "sha256":
                check = sha256(password)
            elif hash_type == "sha512":
                check = sha512(password)
            else:
                check = ctx.verify(password, hash_input)

            if check == hash_input:
                bar.colour = "green"
                bar.set_description(f"Matched '{password}'")
                results = password
                break

            bar.update(1)
    bar.close()

    return results
