'''
x만큼 간격이 있는 n개의 숫자

함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.
'''
# 핵심은 등차수열, n번 만큼 반복하며 횟수와 x 값을 곱해준다. n == 0 인 경우를 주의한다. 

# 나의 풀이
def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer

# 다른 사람의 풀이
def number_generator(x, n):
    return [i * x + x for i in range(n)]