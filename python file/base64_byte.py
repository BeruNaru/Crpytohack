import base64

c = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf' #해결해야하는 값
c1 = bytes.fromhex(c)

c2 = base64.b64encode(c1)

print(c2)

#flag = crypto/Base+64+Encoding+is+Web+Safe/
