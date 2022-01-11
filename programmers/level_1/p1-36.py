'''
두 개 뽑아서 더하기

문제 설명
정수 배열 numbers가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.

입출력 예
numbers	    result
[2,1,3,4,1]	[2,3,4,5,6,7]
[5,0,2,7]	[2,5,7,9,12]
'''

# 나의 풀이
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):   # 마지막 요소는 더해줄 다음 값이 없다. -1 없어도 결과는 동일
      for j in range(i+1,len(numbers)):
                answer.append(numbers[i]+numbers[j])
                
    return sorted(set(answer))


# 다른 풀이
from itertools import combinations

def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2)) #순서를 고려하지 않고 중복없이 뽑는다.

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer