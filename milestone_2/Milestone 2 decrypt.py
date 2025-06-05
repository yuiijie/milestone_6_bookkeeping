#decrypt
#key = 1
#message = 'Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.'
def decrypt(msg: str, key: int) -> str:
  decrypted = ''

  for i in msg:
    if(i >= 'a' and i <= 'z'):
      decrypted += chr((ord(i) - key - ord('a')) % 26 + ord('a'))
    elif i >= 'A' and i <= 'Z':
      decrypted += chr((ord(i) - key - ord('A')) % 26 + ord('A'))
    else:
      decrypted += i

  return decrypted

print(decrypt(input('Enter the message: '), int(input('Enter the key: '))))

#Result: The quick brown fox jumps over the lazy dog.
     