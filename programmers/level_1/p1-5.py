'''
하샤드 수

양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고,
18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

제한 조건
x는 1 이상, 10000 이하인 정수입니다.
'''

# x는 여러자리 수가 될 수 있다.
#TODO: 앞으로 for문을 사용한다면 리스트 컴프리헨션으로 바꿔보자!

# 나의 풀이
def solution(x):
    x = str(x)
    sum = 0

    for i in x:
        sum += int(i)
        
    return int(x) % sum == 0

# 다른 사람의 풀이 -> numeric iterable의 합을 구하는 sum
def harshad(x):

    return x % sum([int(x) for x in str(x)]) == 0
