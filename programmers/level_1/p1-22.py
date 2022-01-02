'''
문자열 다루기 기본

문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
'''
# 문자열.isdigit()

# 나의 풀이
def solution(s):
    return s.isdigit() and (len(s)==4 or len(s)==6) # 또는 len(s) in (4,6)

# 다른 풀이 1
def solution(s):
    try:
        int(s)
        return len(s) == 4 or len(s) == 6
    except:
        return False
    
# 다른 풀이 2
def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))

''' 해설
1. ^와 $는 문자열의 처음과 끝을 의미
2. \d는 숫자를 의미
3. {4}|{6}은 숫자가 4번 혹은 6번 반복되는 것을 찾는 것
4. 결과를 불리언으로 반환
'''
