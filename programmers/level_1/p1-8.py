'''
최대공약수와 최소공배수

문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.
'''

# 나의 풀이
def solution(n, m):
    for i in range(1,n+1):
        if n % i == 0:
            if m % i == 0:
                g = i
        if g == 1:
            l = n * m
        else:
            l = g * (n/g) * (m/g)

    return [g, l]

# 다른 사람의 풀이 (유클리드 호제법)
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

'''
유클리드 호제법 (https://codingpractices.tistory.com/34)
a, b의 최대공약수 == b와 a%b의 최대공약수
 -> GCD(a, b) = GCD(b, a%b)
a%b가 0이 될 경우의 b가 최대공약수이다.

ex) GCD(24, 18) = GCD(18, 6) = GCD(6, 0)
마지막에 a%b가 0이 되었기 때문에 24와 18의 GCD는 6이다.

LCM(a, b) = GCD * (a/GCD) * (b/GCD) 

GCD (Greatest Common Divisor)
LCM (Least Common Multiple)
'''

# math 모듈로 최대공약수 구하기
from math import gcd