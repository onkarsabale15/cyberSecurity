# Define two integers to encrypt
plaintext1 = 42
plaintext2 = 17

# Define a public modulus for encryption and addition
public_modulus = 101

# Encrypt the plaintexts
ciphertext1 = plaintext1 % public_modulus
ciphertext2 = plaintext2 % public_modulus

# Perform homomorphic addition on the ciphertexts
result_ciphertext = (ciphertext1 + ciphertext2) % public_modulus

# Decrypt the result to get the sum
result_plaintext = result_ciphertext

# Print the results
print(f"Plaintext1: {plaintext1}")
print(f"Plaintext2: {plaintext2}")
print(f"Sum: {result_plaintext}")
