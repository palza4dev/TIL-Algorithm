'''
2016년

문제 설명
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다.
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

제한 조건
2016년은 윤년입니다.
2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

입출력 예
a	b	result
5	24	"TUE"
'''

# 나의 풀이
def solution(a, b):
    days = int()
    weekdays = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    monthdays = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    days = sum(monthdays[:a-1]) + b

    return weekdays[(days-1)%7]  # days는 1부터 시작하고 인덱스는 0부터 시작. days%7 - 1 과 동일하다. 
    
    # 날짜를 365일 중 몇일인지로 바꾸고, 7로 나눈 나머지로 요일 계산
    # 1월31일은? 31
    # 2월1일은? 32

# 개선된 풀이
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    return days[(sum(months[:a-1])+b-1)%7]


# 다른 풀이 -> 연도가 바뀌면 now 값만 바꿔주면 된다.
def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    dayLen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    now = 5
    for i in range(0, a - 1) :
        now += dayLen[i]

    answer = (now + b - 1) % 7

    return days[answer]