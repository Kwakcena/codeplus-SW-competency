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
- [PR: 최대공약수와 최소공배수](https://github.com/Kwakcena/codeplus-SW-competency/pull/1)
- [PR: 최소공배수](https://github.com/Kwakcena/codeplus-SW-competency/pull/2)
- [PR: GCD 합](https://github.com/Kwakcena/codeplus-SW-competency/pull/3) : `itertools` 모듈 사용법

## 소수 찾기
어떤 숫자가 소수인지 판별하기
```python
def find_prime_number(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True
```

일정 범위 내의 숫자가 소수인지 판별하기 (에라토스 테네스의 체)
```python
def eratos(m):
    check = [False] * (m + 1)
    prime_numbers = []
    for i in range(2, m + 1):
        if not check[i]:
            prime_numbers.append(i)
            for j in range(i + i, m + 1, i):
                check[j] = True

    return [prime_numbers, check]
```
- [PR: 소수 찾기](https://github.com/Kwakcena/codeplus-SW-competency/pull/4)

## 골드바흐의 추측
```
- 2보다 큰 모든 짝수는 두 소수의 합으로 표현 가능하다
- 5보다 큰 모든 홀수는 세 소수의 합으로 표현 가능하다.
- 10^18 이하에서는 참인 것이 증명되어 있다.
```
- [PR: 골드바흐의 추측](https://github.com/Kwakcena/codeplus-SW-competency/pull/5)
