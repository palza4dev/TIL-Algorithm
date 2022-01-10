'''
완주하지 못한 선수

문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

EX:
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
'''

# 나의 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # 마지막 요소가 완주하지 못한 경우만 따로 처리
    return participant[-1]

''' 또는 같은 인덱스끼리 짝지어주는 zip 함수 활용
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
'''


# 다른 풀이 1 -> Counter 객체 활용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    # keys() 메서드로 키만 가져오고 리스트로 변환 후 첫번째 요소 반환하기
    return list(answer.keys())[0]


# 다른 풀이 2 -> 해시함수
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    # 해시 값을 키로 하는 딕셔너리 만들기 -> 참가자의 해시값 합계
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    # 완주자의 해시값을 제외하기
    for com in completion:
        temp -= hash(com)
    # 남은 해시값을 키로하는 참가자 가져오기
    answer = dic[temp]

    return answer
