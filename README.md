# RSA-Cryptosystem
RSA (Rivest-Shamir-Adleman) cryptosystem is a widely-used public-key encryption algorithm that enables secure data transmission and digital signatures by utilizing the mathematical properties of large prime numbers and modular arithmetic.

1. Key Generation:
   + Choose two large prime numbers, p and q.
   + Calculate n = p * q
   + Calculate φ(n) = (p-1) * (q-1)
   + Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
   + Calculate d such that d * e ≡ 1 (mod φ(n))
   + Public key is (n, e), private key is (n, d)

2. Encryption:
   + Given a message m, compute ciphertext c = m^e mod n

3. Decryption:
   + Given ciphertext c, compute message m = c^d mod n
