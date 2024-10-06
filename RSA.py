import secrets
import sympy
import math

class RSA:
    def __init__(self, key_size: int = 1024):
        self.key_size = key_size
        self.bit_length = key_size // 2

    def generate_prime(self) -> int:
        while True:
            random_int = secrets.randbits(self.bit_length)
            if sympy.isprime(random_int):
                return random_int

    def key(self, p: int, q: int) -> Tuple[int,int]:
        n = p * q
        phi = (p - 1) * (q - 1)
        e = secrets.randbelow(phi - 2) + 2
        while math.gcd(e, phi) != 1:
            e += 1
        d = pow(e, -1, phi)

        public_key = (n, e)
        private_key = (n, d)

        return public_key, private_key

    def encryption(self, public_key: tuple, msg: str) -> str:
        n, e = public_key
        max_bytes = (self.key_size - 1) // 8

        msg_bytes = msg.encode("utf-8")
        encrypted = ""

        for i in range(0, len(msg_bytes), max_bytes):
            msg_part = msg_bytes[i:i+max_bytes]
            msg_int = int.from_bytes(msg_part, "big")

            enc_int = pow(msg_int, e, n)

            enc_hex = hex(enc_int)[2:].zfill(self.key_size // 4)
            encrypted += enc_hex

        return encrypted

    def decryption(self, private_key: tuple, encrypted_msg: str) -> str:
        n, d = private_key
        decrypted = ""

        chunk_size = self.key_size // 4

        for i in range(0, len(encrypted_msg), chunk_size):
            enc_part_hex = encrypted_msg[i:i+chunk_size]
            enc_int = int(enc_part_hex, 16)

            dec_int = pow(enc_int, d, n)

            byte_length = (dec_int.bit_length() + 7) // 8
            dec_bytes = dec_int.to_bytes(byte_length, byteorder="big")


            dec_str = dec_bytes.decode("utf-8")
            decrypted += dec_str

        return decrypted

# Sample Usage
rsa = RSA(1024)
p = rsa.generate_prime()
q = rsa.generate_prime()

key = rsa.key(p, q)

public_k = key[0]
private_k = key[1]

msg = "Mustafa Kemal Atatürk was the founder and first president of the Republic of Turkey, leading the Turkish nation to freedom."

enc = rsa.encryption(public_k, msg)
print("Encrypted:", enc)

dec = rsa.decryption(private_k, enc)
print("Decrypted:", dec)
