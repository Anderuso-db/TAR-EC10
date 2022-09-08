
import random

def gcd(p,q):
# mdc entre dois números inteiros.
    while q != 0:
        p, q = q, p%q
    return p

#multiplicador inverso
def multiplicativeInverse(e,r):
    for i in range(r):
        if((e*i)%r == 1):
            return i

def encrypt(privateKey, message):
    key, n = privateKey
    cipher = [(ord(char) ** key) % n for char in message]
    return cipher

def decrypt(publicKey, ciphertext):
    key, n = publicKey
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

msg = 'The information security is of significant importance to ensure the privacy of communications'

#números primos p e q
p = 83
q = 89

#n = p * q
n = p * q

#função totiene phi(n) = (p - 1)(q - 1)
phi = (p - 1) * (q - 1)
print('phi', phi)

#numero "e" onde ' 1 < e < phi(n) | "e" e phi(n) devem ser primos entre si
e = random.randrange(1, phi)

g = gcd(e, phi)

while g != 1:
    print('e', e)
    e = random.randrange(1, phi)  
    g = gcd(e, phi)

# d = inverso multiplicativo de "e"
d = multiplicativeInverse(e,phi)
print ('d', d)

privateKey = (e, n)
publicKey = (d, n)

# Criptografando a mensagem
messageEncrypted = encrypt(privateKey, msg)
print('messageEncrypted ', messageEncrypted)

# Decriptografando a mensagem
messageDecrypted = decrypt(publicKey, messageEncrypted)
print('messageDecrypted ', messageDecrypted)