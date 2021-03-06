'''
약수의 합

문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
'''

# 나의 풀이
def solution(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum += i
    return sum

# 다른 사람의 풀이
def sumDivisor(num):

    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

''' 해설
2로 나누고 내림한 정수까지만 확인하면된다. -> sum으로 더하기
입력 정수를 더해준다.
'''