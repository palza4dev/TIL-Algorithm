'''
자연수 뒤집어 배열로 만들기

문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
'''

# 나의 풀이 -> list 객체의 reverse() 메소드 사용
def solution(n):
    num_list = list(str(n))
    num_list.reverse()
    result = list(map(int, num_list))
    return result

# 다른 사람의 풀이 1 -> 파이썬 내장함수 reversed() 사용 - reversed 객체를 반환한다.
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

# 다른 사람의 풀이 2 -> [::-1]로 맨뒤의 요소부터 list에 담기
def digit_reverse(n):
    return list(map(int, list(str(n))[::-1]))
