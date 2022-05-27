'''
소수 만들기

문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

입출력 예
nums	    result
[1,2,3,4]	 1
[1,2,7,6,4]	 4
'''

# 나의 풀이

from itertools import combinations

def solution(nums):
    # 서로 다른 3개 골라서 더하기
    three_list = list(combinations(nums,3))
    sum_list = [sum(three) for three in three_list]
        
    # 소수가 되는 경우의 수 구하기
    count = 0
    for num in sum_list:
        for i in range(2,int(num**0.5)+1): #에라토스테네스의 체
            if not num%i: #나누어 떨어지면 소수가 아니다.
                break
        else:
            count += 1
    return count

# 다른 풀이 -> 코드 간소화 버전
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer    