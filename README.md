# CRYPT, an encryption/decryption tool
![head](./modules/images/head.png)

<div align=center>
  <a href="https://github.com/ninja-left/CRYPT/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ninja-left/CRYPT">
  </a>
  <a href="https://github.com/ninja-left/CRYPT">
    <img src="https://img.shields.io/github/commit-activity/m/ninja-left/CRYPT">
  </a>

![Latest version](https://img.shields.io/github/v/tag/ninja-left/CRYPT?label=Version&color=black) ![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)

</div>


## What?
CRYPT is a tool that allows you to encrypt or decrypt texts.

## Why?
The main reason I wrote this program was having access to common encodings and hash
functions in one place. Later I added more functions and ciphers. All releases have
a script named `CryptB.py` which takes 2 files as input and output and encodes or
decodes the input file line by line while writing to output file.

## What encodings, ciphers, and hashes are supported?
1. Encodings:
   - Base16
   - Base32
   - Base64
   - Base85

2. Ciphers:
   - Caesar Cipher
   - Morse Code
   - Baconian Cipher
   - Vigenère Cipher

3. Hashes:
   - MD5
   - Md5 Crypt
   - SHA256 & SHA512
   - SHA256 & SHA512 Crypt
   - NT
   - BCrypt
   - Argon2
   - PBKDF2+SHA256 & PBKDF2+SHA512
   - Hash Cracking with a wordlist or by Bruteforcing

## Usage
Run main app using
```shell
python Crypt-?.?.?.py
```
or
```shell
./Crypt-?.?.?.py
```
Where `?.?.?` is the version.

---

Running `CryptB.py` is same way as above, except that `CryptB.py` is a CLI tool
and accept arguments and options.
You can see all options for `CryptB.py` using `--help` option:

```shell
./CryptB.py --help
```

```
Usage: CryptB.py [OPTIONS]

Options:
  -F, --file FILENAME             File containing plain text for encryption.
  -O, --out PATH                  Path/File to write the encrypted text to.
  -M, --method [md5|md5-brute|...|baconian-e|baconian-d]
                                  Method to use for encryption.
  -K, --key INTEGER               Encryption/decryption key for ciphers that support it.
                                  Positive integer for encryption, Negative
                                  integer for decryption.
  --about, --copyright            Show About & Copyright
  --help                          Show this message and exit.
```

## Support
If you encounter any issues or bugs, feel free to open an issue about it on this repo and I'll try to help.

## License
This project is licensed under GPL v3.0. See [LICENSE] for details.

## Contributing
Thanks in advance for considering to help me on this project.
You can read [CONTRIBUTING.md] for details on contributing to the project.

## Roadmap
See [ROADMAP.md] for details.

[LICENSE]: ./LICENSE
[CONTRIBUTING.md]: ./CONTRIBUTING.md
[ROADMAP.md]: ./ROADMAP.md
