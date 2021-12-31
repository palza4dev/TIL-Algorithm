'''
시저 암호

문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
'''

# 나의 풀이
import string

def solution(s, n):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    answer = ""
    
    for i in s:
        if i == " ":
            answer += " "
        
        elif i in lower:
            answer += lower[(lower.index(i) + n)%26]
            
        elif i in upper:
            answer += upper[(upper.index(i) + n)%26]
            
    return answer

''' 해설
1. string 모듈로 알파벳을 모두 가져온다.
2. 반환 값을 담기위한 빈문자열 변수를 만든다.
3. 단어를 순회하며 알파벳에 하나씩 접근한다.
4. 공백일땐 공백을 추가한다.
5. 대소문자를 구별해 인덱스 값을 구하고 n만큼 더한다.
6. 26을 나눈 나머지가 새로운 알파벳의 인덱스가 된다.

- 알파벳은 26개가 있고 z나 Z의 인덱스는 25이다.
- a 나 A를 출력하려면 나머지가 0이 되어야 한다.
'''

# 다른 사람의 풀이
def caesar(s, n):
    s = list(s)
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n)%26 + ord('A'))
            
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n)%26 + ord('a'))

    return "".join(s)

''' 해설
1. 문자열을 쪼개기 위해 리스트로 만든다.
2. 요소 하나씩 대소문자를 구분한다.
3. 알파벳을 ord(문자열) 메서드로 아스키 코드로 변환한다.
4. A 혹은 a의 아스키 값만큼 빼고 n만큼 더한다.
5. 26을 나눈 나머지 값에 다시 A 혹은 a의 아스키 값을 더한다.
6. chr(아스키코드)로 다시 알파벳으로 변환한다.
7. 공백은 그대로 두면되니까 무시한다.
'''