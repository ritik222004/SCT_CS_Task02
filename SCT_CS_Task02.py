from PIL import Image
import numpy as np
import secrets

# Generate a random encryption key
def generate_key(shape):
    return np.random.randint(0, 256, shape, dtype=np.uint8)

# Encrypt image using XOR operation
def encrypt_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    key = generate_key(img_array.shape)  # Random key same size ka
    encrypted_array = img_array ^ key  # XOR encryption

    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save("encrypted_image.png")
    encrypted_img.show()

    np.save("encryption_key.npy", key)  # Key ko securely save karna

# Decrypt image using same XOR operation
def decrypt_image(encrypted_path, key_path):
    encrypted_img = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_img)

    key = np.load(key_path)  # Saved key load karna
    decrypted_array = encrypted_array ^ key  # XOR decryption

    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save("decrypted_image.png")
    decrypted_img.show()

# Test Code
encrypt_image("input_image.png")  # Encrypt karega
decrypt_image("encrypted_image.png", "encryption_key.npy")  # Decrypt karega
