# Overall CRYPT Development & Features Roadmap
1. Implement a configuration system
    - Using a config file maybe
    - A menu entry for editing the file
2. Changing the default (english) alphabet
    - Editing current alphabet
    - Typing new alphabet
    - Reverting to default alphabet
    - Setting the default alphabet (using the config system?)
3. Implement the following functions:
    - Enigma Machine
    - Affine Cipher
    - A1Z26
    - Rail fence cipher
    - Polybius square
    - Bifid cipher
    - Nihilist cipher
    - RC4
    - HMAC
    - Different Compression algorithms
4. Implement a plugin system
    - Use `pluginlib`
    - Define 3 parents: Encoder, Decoder, Bruteforcer
        ```python3
        import pluginlib
        @pluginlib.Parent('encoder')
        class Encoder(object):
            @pluginlib.abstractmethod
            def encode(self, string):
                # encode function
                return "encoded"
        ```
#### Last update: 2024-06-21

