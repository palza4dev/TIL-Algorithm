'''
이상한 문자 만들기

문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
'''

# 나의 풀이
def solution(s):
    words_list = s.split(" ")
    result = []
    
    for word in words_list:
        new = str()
        for i in range(len(word)):
            if i%2==0:
                new += word[i].upper()
            else:
                new += word[i].lower()
        result.append(new)

    return " ".join(result)

''' 해설
공백 기준으로 단어를 나눈 리스트 생성 -> words_list
단어를 순회하며 알파벳 인덱스를 순회한다.
알파벳 인덱스가 짝수이면 대문자, 홀수이면 소문자로 바꾸고
새로운 단어 변수에 담는다. -> 문자열은 불변객체이므로 새로 담아야한다.
result 리스트에 바꾼 단어를 넣고 join으로 합친다.
'''

# 다른 사람의 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

''' 해설
map은 리스트 요소마다 함수를 적용시킨다. ex) map(함수, 리스트)
enumerate는 인덱스 번호와 원소를 tuple 형태로 반환한다. -> 두 변수에 각각 담을 수 있다.
'''