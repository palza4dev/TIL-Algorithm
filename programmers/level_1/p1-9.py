'''
짝수와 홀수

정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.
'''

# 나의 풀이
def solution(num):
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

# 다른 사람의 풀이 1
def evenOrOdd(num):
    return "Even" if num%2 == 0 else "Odd"

# 다른 사람의 풀이 2
def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"