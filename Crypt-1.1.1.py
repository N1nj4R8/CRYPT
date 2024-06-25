#!/usr/bin/env python3
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

from pprint import pprint
from modules import design, functions
from modules.crack import *
import sys


grn = "\x1b[0;32m"  # Green
red = "\x1b[0;31m"  # Red
wte = "\x1b[0;37m"  # White
ppl = "\x1b[0;35m"  # Purple (Magenta)
ylo = "\x1b[0;33m"  # Yellow
cyn = "\x1b[0;36m"  # Cyan
gry = "\x1b[0;90m"  # Grey (Light Black)
write_to_file = False

while True:
    try:
        functions.cl()
        print(design.Crypt_Logo(red, gry, grn))
        print(design.menu(ylo, ppl, wte))

        cmd_main = input(f"{grn}   CRYPT>{wte} ")

        if cmd_main == "1":  # Base16
            functions.cl()
            print(design.info_b16)
            try:
                b16_input = functions.get_input()
                mode = input(f"{grn}   [+] (E)ncrypt or (D)ecrypt?{wte} ").upper()
                if mode[0] == "E":
                    mode = "Encrypt"
                    results = functions.base16_encode(b16_input)
                    if write_to_file:
                        functions.fileWriter(b16_input, "Base16", results)
                elif mode[0] == "D":
                    mode = "Decrypt"
                    results = functions.base16_decode(b16_input)
                    if write_to_file:
                        functions.fileWriter(results, "Base16", b16_input)
                else:
                    raise Exception(f"Bad mode: {mode}; Mode must be 'E' or 'D'.")

                print(f"{cyn}   [+] {mode}ed:\n<<<\n{wte}{results}\n{cyn}>>>")
                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                input()

            except:
                raise

        elif cmd_main == "2":  # Base32
            functions.cl()
            print(design.info_b32)
            try:
                b32_input = functions.get_input()
                mode = input(f"{grn}   [+] (E)ncrypt or (D)ecrypt?{wte} ").upper()
                if mode[0] == "E":
                    mode = "Encrypt"
                    results = functions.base32_encode(b32_input)
                    if write_to_file:
                        functions.fileWriter(b32_input, "Base32", results)
                elif mode[0] == "D":
                    mode = "Decrypt"
                    results = functions.base32_decode(b32_input)
                    if write_to_file:
                        functions.fileWriter(results, "Base32", b32_input)
                else:
                    raise Exception(f"Bad mode: {mode}; Mode must be 'E' or 'D'.")

                print(f"{cyn}   [+] {mode}ed:\n<<<\n{wte}{results}\n{cyn}>>>")
                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                input()

            except:
                raise

        elif cmd_main == "3":  # Base64
            functions.cl()
            print(design.info_b64)
            try:
                b64_input = functions.get_input()
                mode = input(f"{grn}   [+] (E)ncrypt or (D)ecrypt?{wte} ").upper()
                if mode[0] == "E":
                    mode = "Encrypt"
                    results = functions.base64_encode(b64_input)
                    if write_to_file:
                        functions.fileWriter(b64_input, "Base64", results)
                elif mode[0] == "D":
                    mode = "Decrypt"
                    results = functions.base64_decode(b64_input)
                    if write_to_file:
                        functions.fileWriter(results, "Base64", b64_input)
                else:
                    raise Exception(f"Bad mode: {mode}; Mode must be 'E' or 'D'.")

                print(f"{cyn}   [+] {mode}ed:\n<<<\n{wte}{results}\n{cyn}>>>")
                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                input()

            except:
                raise

        elif cmd_main == "4":  # Caesar Cipher
            try:
                functions.cl()
                print(design.info_cc)
                cc_input = functions.get_input()
                print(
                    f'{ylo}\n\n   [!] "Key" is the number of letters to shift the message by.'
                    "\nEnter 0 for Brute forcing, a positive number (e.g 5) for encryption and a"
                    "\nnegative number (e.g -5) for decryption."
                )
                cc_key = int(input(f"{grn}   [+] Key: {wte}"))
                mode = results = "None"
                if cc_key > 0 or cc_key < 0:
                    mode = "Encrypt" if cc_key > 0 else "Decrypt"
                    results = functions.cc_cipher(cc_input, cc_key)
                elif cc_key == 0:
                    mode = "Brute-Forc"
                    results = functions.cc_brute_force(cc_input)

                print(f"\n\n{cyn}   [+] {mode}ed:{wte}")
                if mode == "Brute-Forc":
                    print(f"{cyn}<<<{wte}")
                    pprint(results, sort_dicts=False)
                    print(f"{cyn}>>>")
                else:
                    print(f"{cyn}<<<{wte}{results}{cyn}>>>")

                if mode == "Encrypt" and write_to_file:
                    functions.fileWriter(
                        cc_input, "Caesar Cipher", results, cc=True, cc_key=cc_key
                    )

                elif mode == "Decrypt" and write_to_file:
                    functions.fileWriter(
                        results, "Caesar Cipher", cc_input, cc=True, cc_key=cc_key
                    )
                elif mode == "Brute-Forc" and write_to_file:
                    functions.fileWriter(cc_input, "Caesar Cipher", results, cc=True)

                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                input()

            except:
                raise

        elif cmd_main == "5":  # Morse Code
            functions.cl()
            print(design.info_mc)
            try:
                mc_input = functions.get_input()
                mode = input(f"{grn}   [+] (E)ncrypt or (D)ecrypt?{wte} ").upper()
                if mode[0] == "E":
                    mode = "Encrypt"
                    results = functions.mc_encrypt(mc_input)
                    if write_to_file:
                        functions.fileWriter(mc_input, "Morse Code", results)
                elif mode[0] == "D":
                    mode = "Decrypt"
                    results = functions.mc_decrypt(mc_input)
                    if write_to_file:
                        functions.fileWriter(results, "Morse Code", mc_input)
                else:
                    raise Exception(f"Bad mode: {mode}; Mode must be 'E' or 'D'.")

                print(f"{cyn}   [+] {mode}ed:\n<<<\n{wte}{results}\n{cyn}>>>")
                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                input()

            except:
                raise

        elif cmd_main == "6":  # Base85
            functions.cl()
            print(design.info_b85)
            try:
                b85_input = functions.get_input()
                mode = input(f"{grn}   [+] (E)ncrypt or (D)ecrypt?{wte} ").upper()
                if mode[0] == "E":
                    mode = "Encrypt"
                    results = functions.base85_encode(b85_input)
                    if write_to_file:
                        functions.fileWriter(b85_input, "Base85", results)
                elif mode[0] == "D":
                    mode = "Decrypt"
                    results = functions.base85_decode(b85_input)
                    if write_to_file:
                        functions.fileWriter(results, "Base85", b85_input)
                else:
                    raise Exception(f"Bad mode: {mode}; Mode must be 'E' or 'D'.")

                print(f"{cyn}   [+] {mode}ed:\n<<<\n{wte}{results}\n{cyn}>>>")
                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                input()

            except:
                raise

        elif cmd_main == "7":  # Baconian Cipher
            functions.cl()
            print(design.info_bc)
            try:
                bacon_txt = functions.get_input()
                mode = input(f"{grn}   [+] (E)ncrypt or (D)ecrypt?{wte} ").upper()
                if mode[0] == "E":
                    mode = "Encrypt"
                    results = functions.bacon_encode(bacon_txt)
                    if write_to_file:
                        functions.fileWriter(bacon_txt, "Baconian Cipher", results)
                elif mode[0] == "D":
                    mode = "Decrypt"
                    results = functions.bacon_decode(bacon_txt)
                    if write_to_file:
                        functions.fileWriter(results, "Baconian Cipher", bacon_txt)
                else:
                    raise Exception(f"Bad mode: {mode}; Mode must be 'E' or 'D'.")

                print(f"{cyn}   [+] {mode}ed:\n<<<\n{wte}{results}\n{cyn}>>>")
                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                input()

            except:
                raise

        elif cmd_main == "8":  # Vigenère Cipher
            functions.cl()
            try:
                vig_input = functions.get_input()
                mode = input(f"{grn}   [+] (E)ncrypt or (D)ecrypt?{wte} ").upper()
                if mode not in ["E", "D"]:
                    raise Exception(f"Bad mode: {mode}; Mode must be 'E' or 'D'.")
                mode = "Encrypt" if mode[0] == "E" else "Decrypt"
                print(f"{cyn} [!] Key must be a word or any combination of letters.")
                key = input(f"{grn}   [+] Key to use:{wte} ")
                if key.isalpha():
                    key = key.upper()
                else:
                    raise Exception("Key must be a word or any combination of letters.")
                results = functions.vig_cipher(vig_input, key, mode.lower())
                if write_to_file:
                    if mode == "Encrypt":
                        functions.fileWriter(
                            vig_input,
                            "Vigenère Cipher",
                            results,
                            cc=True,
                            cc_key=key,
                        )
                    else:
                        functions.fileWriter(
                            results,
                            "Vigenère Cipher",
                            vig_input,
                            cc=True,
                            cc_key=key,
                        )

                print(f"{cyn}   [+] {mode}ed:\n<<<\n{wte}{results}\n{cyn}>>>")
                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                input()

            except:
                raise

        elif cmd_main == "9":  # MD5
            functions.cl()
            text_input = functions.get_input()

            results = functions.md5(text_input)
            print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")

            if write_to_file:
                functions.fileWriter(text_input, "MD5 Hash", results)

            print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
            input()

        elif cmd_main == "10":  # More
            while True:
                try:
                    functions.cl()
                    print(design.Crypt_Logo(red, gry, grn))
                    print(design.menu_more(ylo, ppl, wte))

                    cmd_more = input(f"{grn}   CRYPT> {wte}")

                    if cmd_more == "1":  # Md5 Crypt
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.md5_crypt(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "MD5 Crypt", results)
                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "2":  # SHA256
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.sha256(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "SHA256 Hash", results)

                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "3":  # SHA256 Crypt
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.sha256_crypt(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "SHA256 Crypt", results)
                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "4":  # SHA512
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.sha512(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "SHA512 Hash", results)

                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "5":  # SHA512 Crypt
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.sha512_crypt(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "SHA512 Crypt", results)
                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "6":  # NT Hash
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.nthash(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "NT Hash", results)
                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "7":  # BCrypt
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.bcrypt(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "BCrypt", results)
                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "8":  # Argon2
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.argon2(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "Argon2", results)
                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "9":  # PBKDF2-SHA256
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.pbkdf2_256(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "PBKDF2-SHA256", results)
                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "10":  # PBKDF2-SHA512
                        functions.cl()
                        text_input = functions.get_input()

                        results = functions.pbkdf2_512(text_input)

                        print(f"{cyn}   [+] Hash:\n<<<\n{wte}{results}\n{cyn}>>>")
                        if write_to_file:
                            functions.fileWriter(text_input, "PBKDF2-SHA512", results)
                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more == "11":  # Hash Crackers
                        while True:
                            cl()
                            print(design.menu_crackers())
                            cmd_cracker = input(f"{grn}   CRYPT>{wte} ")
                            if cmd_cracker == "1":  # Brute Force
                                cl()
                                hash_input = input(f"\n{grn}   [+] Hash:{wte} ")
                                length = int(input(f"{grn}   [+] Max Length:{wte} "))
                                print(
                                    f"\n{ylo}  [!] If 1, ramp up from start_length till length; Otherwise, iterate over current length values."
                                )
                                ramp = bool(
                                    int(input(f"{grn}   [+] Ramp? [1/0]:{wte} "))
                                )
                                start_length = int(
                                    input(f"{grn}   [+] Start length [0<=]:{wte} ")
                                )
                                have_letters = bool(
                                    int(
                                        input(
                                            f"{grn}   [+] Include Letters? [1/0]:{wte} "
                                        )
                                    )
                                )
                                have_symbols = bool(
                                    int(
                                        input(
                                            f"{grn}   [+] Include Symbols? [1/0]:{wte} "
                                        )
                                    )
                                )
                                have_numbers = bool(
                                    int(
                                        input(
                                            f"{grn}   [+] Include Numbers? [1/0]:{wte} "
                                        )
                                    )
                                )
                                hash_type = input(
                                    f"{grn}   [+] Hash Type [md5/sha256/sha512/other]:{wte} "
                                ).lower()
                                if (
                                    not hash_type in ["md5", "sha256", "sha512"]
                                    or not 3 <= len(hash_type) <= 6
                                ):
                                    hash_type = "other"
                                results = crackHash_BruteForce(
                                    hash_input,
                                    length,
                                    ramp,
                                    start_length,
                                    have_letters,
                                    have_symbols,
                                    have_numbers,
                                    hash_type,
                                )
                                print(
                                    f"{ylo}\n\nResults:\n<<<\n{wte}{results}\n{cyn}>>>"
                                )

                                if write_to_file:
                                    fileWriter(results, "Brute Forced", hash_input)
                                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                                input()

                            elif cmd_cracker == "2":  # Wordlist
                                cl()
                                hash_input = input(f"\n{grn}   [+] Hash:{wte} ")
                                file_path = input(f"{grn}   [+] Wordlist path:{wte} ")
                                hash_type = input(
                                    f"{grn}   [+] Hash Type [md5/sha256/sha512/other]:{wte} "
                                ).lower()
                                if (
                                    not hash_type in ["md5", "sha256", "sha512"]
                                    or not 3 <= len(hash_type) <= 6
                                ):
                                    hash_type = "other"
                                results = crackHash_WordList(
                                    hash_input, file_path, hash_type
                                )
                                print(
                                    f"{ylo}\n\nResults:\n<<<\n{wte}{results}\n{cyn}>>>"
                                )

                                if write_to_file:
                                    fileWriter(
                                        results,
                                        "Brute Forced (Wordlist)",
                                        hash_input,
                                    )

                                print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                                input()

                            elif cmd_cracker.upper() == "B":
                                break

                    elif cmd_more.upper() == "B":
                        break

                    elif cmd_more.upper() == "A":
                        functions.cl()
                        print(design.about(ylo, wte, grn, cyn))
                        print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
                        input()

                    elif cmd_more.upper() == "F":
                        file_write = input(
                            f"{gry}\n\t Current> {write_to_file}{grn}\n\t[?] Write results to file?[y/n]{wte} "
                        )
                        if file_write.lower() == "y":
                            write_to_file = True
                        elif file_write.lower() == "n":
                            write_to_file = False

                except KeyboardInterrupt:
                    continue

        elif cmd_main.upper() == "A":
            functions.cl()
            print(design.about(ylo, wte, grn, cyn))
            print(f"{gry}\n\n\t[!] {wte}Press ENTER to continue...")
            input()

        elif cmd_main.upper() == "F":
            file_write = input(
                f"{gry}\n\t Current> {write_to_file}{grn}\n\t[?] Write results to file?[y/n]{wte} "
            )
            if file_write.lower() == "y":
                write_to_file = True
            elif file_write.lower() == "n":
                write_to_file = False

        elif cmd_main.upper() == "E":
            sys.exit(0)

    except KeyboardInterrupt:
        continue

    except SystemExit:
        raise

    except:
        print(design.error_logo(red))
        print(f"{red}\n\t[!!] Unexpected Error Occurred!")
        error_choice = input(f"\n{ylo} Show error message?[y/N]:{wte} ").lower()
        if error_choice == "y":
            print(f"\n{ylo}[!] Error Message:{wte}")
            raise
        else:
            continue
