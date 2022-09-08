
import random

def gcd(p,q):
# mdc entre dois números inteiros.
    while q != 0:
        p, q = q, p%q
    return p

#verificar se dois numeros sao primos entre si
def isCoprime(x, y):
    return gcd(x, y) == 1

#multiplicador inverso
def multiplicativeInverse(e,r):
    for i in range(r):
        if((e*i)%r == 1):
            return i

def encrypt(privateKey, message):
    #Unpack the key into it's components
    key, n = privateKey
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in message]
    #Return the array of bytes
    return cipher

def decrypt(publicKey, ciphertext):
    #Unpack the key into its components
    key, n = publicKey
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

msg = 'The information security is of significant importance to ensure the privacy of communications'
#msg = 'banana'

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

messageEncrypted = encrypt(privateKey, msg)
print('messageEncrypted ', messageEncrypted)

messageDecrypted = decrypt(publicKey, messageEncrypted)
print('messageDecrypted ', messageDecrypted)


