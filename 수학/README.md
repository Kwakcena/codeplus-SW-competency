# 수학

## 나머지 연산
```
(A + B) % C === ((A % C) + (B % C)) % C
(A * B) % C === ((A % C) * (B % C)) % C
(A - B) % C === ((A % C) - (B % C) + C) % C
나누기의 경우 성립하지 않음.
```

## 최대공약수와 최소공배수
최대공약수와 최소공배수 구하기 - 유클리드 호제법
```python
def GCD(n, m):
    return n if m == 0 else GCD(m, n%m)

def LCM(gcd, n, m):
    return (n * m) // gcd
```
[PR: 최대공약수와 최소공배수](https://github.com/Kwakcena/codeplus-SW-competency/pull/1)
