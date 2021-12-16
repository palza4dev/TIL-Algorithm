'''
직사각형 별찍기

문제 설명
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

제한 조건
n과 m은 각각 1000 이하인 자연수입니다.
'''
# 빈칸을 기준으로 두 정수를 각각 가져온다. n번 만큼 별을 찍고 개행하는 것을 m번 만큼 실행한다.

# 나의 풀이
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print('')
    
# 다른 사람 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)