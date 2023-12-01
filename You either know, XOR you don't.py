from pwn import xor

c = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
key = 'myXORkey'
flag = xor(c, key)

print(flag)

#1단계 키:myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f
#flag = crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}


#참고 사이트  https://mokpo.tistory.com/610