'''
약수의 개수와 덧셈

두 정수 left와 right가 매개변수로 주어집니다.
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000

입출력 예
left	right	result
13	    17	    43
24	    27	    52
'''

# 나의 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if len([j for j in range(1,i+1) if not i%j]) % 2: #약수의 개수가 홀수개
            answer -= i
        else:
            answer += i

    return answer


# 다른 풀이 -> 약수가 홀수개인 모든 수는 제곱수이다.
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer