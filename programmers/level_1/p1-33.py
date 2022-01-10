'''
모의고사
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

입출력 예
answers	    return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
'''

# 나의 풀이
def solution(answers):
    # 패턴으로 문제수만큼 배열 만들기
    q, r = divmod(len(answers),5)
    first = [1,2,3,4,5]*q + [1,2,3,4,5][:r]
    
    q, r = divmod(len(answers),8)
    second = [2,1,2,3,2,4,2,5]*q + [2,1,2,3,2,4,2,5][:r]
    
    q, r = divmod(len(answers),10)
    third = [3,3,1,1,2,2,4,4,5,5]*q + [3,3,1,1,2,2,4,4,5,5][:r]
    # 점수 계산하기
    s1 = s2 = s3 = 0
    for i, v in enumerate(answers):
        if answers[i] == first[i]:
            s1 += 1
        if answers[i] == second[i]:
            s2 += 1
        if answers[i] == third[i]:
            s3 += 1
    # 최대점수에 해당하면 배열에 넣기
    answer = []
    max_score = max(s1,s2,s3)
    if max_score == s1:
        answer.append(1)
    if max_score == s2:
        answer.append(2)
    if max_score == s3:
        answer.append(3)
        
    return answer

# 다른 풀이 1
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []
    # 정답 인덱스를 패턴 순환주기로 나눈 나머지 연산을 이용한다.
    # 패턴마다 각각 일치여부를 확인하고 점수를 합산한다.
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


# 다른 풀이 2 -> 패턴을 제너레이터로 처리
from itertools import cycle # 리스트를 무한 반복하는 cycle 함수

def solution(answers):
    cycles = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    
    for num in answers:
        for i in range(3):
            if next(cycles[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]