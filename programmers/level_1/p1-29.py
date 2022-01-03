'''
가운데 글자 가져오기

단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
'''

# 나의 풀이 -> int안쓰고 // 가능
def solution(s):
    answer = ''

    if len(s)%2==0:
        answer = s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        answer = s[int(len(s)/2)]

    return answer

# 다른 풀이
def solution(s):
    
    return s[(len(s)-1)//2:len(s)//2+1] # 인덱스가 소수점이면 에러 -> //로 정수화