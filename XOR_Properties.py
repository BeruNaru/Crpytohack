from Crypto.Util.number import *

key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
key23 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
flag_key123 = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

key123 = key23 ^ key1
flag = flag_key123 ^ key123

print(long2str(flag))
#flag = crypto{x0r_i5_ass0c1at1v3}
