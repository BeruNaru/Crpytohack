from pwn import *

c = "label"

print("crypto{", end="")
for x in c:
  print(chr(ord(x) ^ 13), end="")
print("}")

#flag = crypto{aloha}