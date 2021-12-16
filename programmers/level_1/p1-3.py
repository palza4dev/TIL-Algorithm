'''
행렬의 덧셈

문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
'''

# 이미 주어진 중첩 리스트를 사용하지 않고 새로 만든다. 

# 나의 풀이
def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        sum_list = []
        for j in range(len(arr1[i])):
            sum_list.append(arr1[i][j] + arr2[i][j])
        answer.append(sum_list)    
    return answer

# 다른 사람의 풀이 1 -> 리스트 컴프리헨션으로 변경 가능
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A

# 다른 사람의 풀이 2 -> 병렬적으로 처리할 수 있는 zip 메서드 활용 / 각 원소를 짝지어 튜플로 반환
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer