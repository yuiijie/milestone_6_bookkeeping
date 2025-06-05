# encrypt
#key = 1
#message = 'The quick brown fox jumps over the lazy dog.'

def encrypt(msg: str, key: int) -> str:
  encrypted = ''

  for i in msg:
    if(i >= 'a' and i <= 'z'):
      encrypted += chr((ord(i) + key - ord('a')) % 26 + ord('a'))
#      print(encrypted)
    elif i >= 'A' and i <= 'Z':
      encrypted += chr((ord(i) + key - ord('A')) % 26 + ord('A'))
#      print(encrypted)
    else:
      encrypted += i
#      print(encrypted)
  return encrypted


print(encrypt(input('Enter the message: '), int(input('Enter the key: '))))

# Result: Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.