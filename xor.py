import base64
def xorcipher(text, key):
    encoded = []
      
    for i in range(0, len(text)):
        encoded.append(text[i] ^ key[i % len(key)])
    return bytes(encoded)

# Driver Code
def main():
    with open('msg.txt', 'r') as f:
        plain_text = f.read().replace('\n', ' ')
    plain_text = bytearray(plain_text, "utf8")
    #plain_text = b'wstep'
    key = b'test'
    sec_key = b'tes'
    print("Plain text: ", plain_text)
    enc = xorcipher(plain_text, key)
    print("Encrypted as: ", enc.hex())
    dec = xorcipher(enc, key)
    print("Decrypted as: ", dec)
    dec2 = xorcipher(enc, sec_key)
    print("Tried decryption with another key: ", dec2)
  
if __name__ == '__main__':
    main()
