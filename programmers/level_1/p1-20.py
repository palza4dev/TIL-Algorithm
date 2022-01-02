'''
소수 찾기

문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
'''

# 나의 풀이 -> 시간초과
def solution(n):
    count = 0
    for n in range(2, n+1):   # 2부터 n까지 모든 수를 하나씩 확인
        for i in range(2, n): # n의 값마다 소수인지 확인 -> 2부터 n-1까지 (자신은 어차피 나누어 떨어짐)
            if n%i == 0:
                break         # 해당 n이 소수가 아니면 반복문 종료 
        else:    
            count += 1        # n이 소수라면 카운트 추가
    return count

# 다른 풀이 -> '에라토스테네스의 체(Sieve of Eratosthenes)'
def solution(n):
    num = set(range(2,n+1))
    
    for i in range(2,int(n**0.5)+1):
        if i in num:
            num -= set(range(i*i, n+1, i))
 
    return len(num)

''' 해설
소수인지 판별하고 싶은 수의 제곱근 까지의 배수를 제외시켜주는 방법
즉, 10을 판별하고 싶으면 10의 제곱근은 3.xxx이므로 [2 : 10] 에서 2, 3의 배수를 제외

1. 2부터 n까지 모든 수를 set에 담는다.
2. 2부터 n의 제곱근 정수 i까지 하나씩 배수를 제거한다. 
3. i 본인은 제거하지 않는다. 따라서 i*i부터 n까지 i만큼 건너 뛴다.
4. set의 차집합을 이용해 num에서 배수들을 모두 제거한다.
5. num의 길이를 반환한다.
'''