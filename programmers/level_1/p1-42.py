'''
3진법 뒤집기

자연수 n이 매개변수로 주어집니다.
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.

입출력 예
n	result
45	7
125	229
'''

# 나의 풀이
def solution(n):
    # 3진법으로 변환 -> 앞뒤가 바뀐 상태로 두기
    n_3 = ''
    
    while n > 0:
        n, r = divmod(n,3)
        n_3 += str(r)

    return int(n_3,3) # 3진법을 10진법으로 변환

# 다른 풀이 -> 원리는 같다.
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3) # 나머지
        n = n // 3        # 몫

    answer = int(tmp, 3)
    return answer
