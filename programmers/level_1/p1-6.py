'''
평균 구하기
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
'''

# numeric iterable의 합을 구하는 sum 활용
# arr의 길이가 1 이상이라서 0인 경우 예외처리 안해도된다.

# 나의 풀이
def solution(arr):
    return sum(arr)/len(arr)