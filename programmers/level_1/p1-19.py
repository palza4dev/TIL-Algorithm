'''
수박수박수박수박수박수?

문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
'''

# 나의 풀이
def solution(n):
    word_list = [] 
    for i in range(n):
        if i % 2 == 0:
            word_list.append('수')
        else:
            word_list.append('박')

    return "".join(word_list)

# 다른 사람의 풀이 -> 필요한 만큼만 만들어내기
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)

# 다른 사람의 풀이 2 -> 필요없는 것도 만든 다음 잘라내서 비효율적
def water_melon(n):
    s = "수박" * n
    return s[:n]