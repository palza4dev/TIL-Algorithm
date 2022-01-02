'''
나누어 떨어지는 숫자 배열

문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.
'''

# 나의 풀이
def solution(arr, divisor):
    answer = []

    for n in arr:
        if n % divisor == 0:
            answer.append(n)
    else:
        if len(answer) == 0:
            return [-1]

    return sorted(answer)

# 다른 풀이 1
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];
    arr.sort();
    return arr if len(arr) != 0 else [-1];

# 다른 풀이 2
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

''' 해설
1. or 앞이 True이면 해당 값까지만 호출한다.
2. 빈배열인 경우 False이다.
3. or 앞이 False이면 뒤에 것을 호출한다. 
'''