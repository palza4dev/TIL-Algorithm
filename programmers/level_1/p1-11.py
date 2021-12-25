'''
정수의 제곱근 판별

문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.
'''

# 나의 풀이
def solution(n):
    for x in range(1,n+1):

        if (x*x) == n:
            return (x+1)*(x+1)

        if (x*x) > n:
            return -1

# 다른 사람의 풀이 1 -> n ** (1/2)로 제곱근 구하기 
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    
    return -1

# 다른 사람의 풀이 2 -> Square Root 메소드 : math.sqrt()
from math import sqrt

def solution(n):

    if sqrt(n) % 1 == 0:
        return int(sqrt(n) + 1) ** 2
    
    return -1
