import codecs

def rot13(message):
    return codecs.encode(message, 'rot_13')


# Test the function
sample_text = "Hello, World! 123"
encrypted_text = rot13(sample_text)
print(f"Original: {sample_text}")
print(f"Encrypted: {encrypted_text}")




