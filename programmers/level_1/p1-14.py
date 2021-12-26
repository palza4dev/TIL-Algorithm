'''
자릿수 더하기

문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수
'''

# 나의 풀이
def solution(n):
    sum = 0
    num_list = list(map(int, str(n)))
    for i in num_list:
        sum += i
    return sum

# 다른 사람의 풀이 1 -> sum() : numeric한 iterable 자료형의 합
def solution(n):
    return sum(map(int, str(n)))

# 다른 사람의 풀이 2 -> 재귀함수 이용
def solution(number):
    if number < 10:
        return number;
    return (number % 10) + solution(number // 10)
# number % 10 : 1의 자리 수 구하기
# number // 10 : 10, 100,,, 자리수 구하기