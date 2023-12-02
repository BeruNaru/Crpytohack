p = 29
ints = [14, 6, 11]

for a in range(29):
    b = pow(a, 2, 29)
    if b in ints:
        print(b, a)



# pow()함수는 제곱
#https://velog.io/@comibear/MODULAR-ARITHMETIC-2-fjpgp0a0 참고 블로그
#그런데, 왜 print 가 2번이나 될까?? 그 이유는 mod 의 성질에 기인한다.
#mod p 에서 -a 와 a 는 제곱했을 때 같은 a^2 의 값을 가지기에 항상 quadratic residue 는 2개씩 제곱근을 가진다.
#( 이 성질 때문에 quadratic residue 와 non-quadratic residue 는 개수가 같다. )

