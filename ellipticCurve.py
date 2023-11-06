import cryptography.hazmat.backends
import cryptography.hazmat.primitives.asymmetric.ec
import cryptography.hazmat.primitives.hashes
import cryptography.exceptions

def sign(private_key, message):
    """Signs the message using the private key."""
    signature = private_key.sign(
        message,
        cryptography.hazmat.primitives.asymmetric.ec.ECDSA(cryptography.hazmat.primitives.hashes.SHA256())
    )
    return signature

def verify(public_key, message, signature):
    """Verifies the signature for the message using the public key."""
    try:
        public_key.verify(
            signature,
            message,
            cryptography.hazmat.primitives.asymmetric.ec.ECDSA(cryptography.hazmat.primitives.hashes.SHA256())
        )
        return True
    except cryptography.exceptions.InvalidSignature:
        return False

def generate_key_pair():
    """Generates an ECDSA key pair."""
    private_key = cryptography.hazmat.primitives.asymmetric.ec.generate_private_key(
        curve=cryptography.hazmat.primitives.asymmetric.ec.SECP256K1(),
        backend=cryptography.hazmat.backends.default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    # Generate a key pair
    private_key, public_key = generate_key_pair()

    # Sign a message
    message = b"This is the message to sign"
    signature = sign(private_key, message)

    # Verify the signature
    if verify(public_key, message, signature):
        print("Signature is valid")
    else:
        print("Signature is invalid")

if __name__ == "__main__":
    main()