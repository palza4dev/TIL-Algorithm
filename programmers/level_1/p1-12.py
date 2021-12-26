'''
정수 내림차순으로 배치하기

문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
'''

# 나의 풀이
def solution(n):
    str_num = str(n)
    list = [i for i in str_num]
    list.sort(reverse = True)
    return int(''.join(list))


# 다른 사람의 풀이 1
def solution(n):
    num_list = list(str(n))
    num_list.sort(reverse = True)
    return int("".join(num_list))


# 다른 사람의 풀이 2 -> sorted는 정렬된 리스트를 새로 반환한다.
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))