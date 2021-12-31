'''
문자열을 정수로 바꾸기

문제 설명
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 "0"으로 시작하지 않습니다.

입출력 예
예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.
'''

# 나의 풀이
def solution(s):
    
    if s[0] == "-":
        return -int(s[1:])
    else:
        return int(s)
    
# 다른 사람의 풀이 1
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result

''' 해설
1. 결과값을 더해가며 만들기 위해 result=0을 선언한다.
2. 예시로 "-1234"는 str[::-1]에 의해 "4321-"가 된다.
3. enumerate로 한자리씩 인덱스와 값을 가져온다.
4. -가 나오기 전까지 10진법으로 계산해서 result에 더한다.
5. 예시로 4 * (10 ** 0) + 3 * (10 ** 1) + 2 * (10 **2) + 1 * (10 ** 3)
6. -가 나오면 -1을 곱해서 음수로 만든다.
'''

# 다른 사람의 풀이 2
def strToInt(str):
    a = int(str)
    return a
