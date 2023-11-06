import random

# Publicly agreed upon parameters
p = 23  # Prime number
g = 5   # Primitive root of p

# Alice's private key
private_key_a = random.randint(1, p - 1)

# Bob's private key
private_key_b = random.randint(1, p - 1)

# Calculate public keys
public_key_a = (g ** private_key_a) % p
public_key_b = (g ** private_key_b) % p

# Exchange public keys (over a secure channel)
# In a real-world scenario, this would be done securely.

# Calculate shared secret
shared_secret_a = (public_key_b ** private_key_a) % p
shared_secret_b = (public_key_a ** private_key_b) % p

# Both Alice and Bob now have the same shared secret
print("Alice's private key:", private_key_a)
print("Bob's private key:", private_key_b)
print("Public key generated by Alice:", public_key_a)
print("Public key generated by Bob:", public_key_b)
print("Shared secret calculated by Alice:", shared_secret_a)
print("Shared secret calculated by Bob:", shared_secret_b)
