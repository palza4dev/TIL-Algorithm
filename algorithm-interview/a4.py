'''
가장 흔한 단어

금지 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지않고 마침표, 쉼표 등은 무시한다.

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
'''

# 나의 풀이
from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]):
        # 데이터 전처리 -> 단어 문자열이 아니면 모두 공백으로 처리, 금지단어가 아니면 소문자로 변환 후 공백 기준으로 분리
        re_paragraph = re.sub(r'[^\w]', ' ', paragraph)
        words = [word for word in re_paragraph.lower().split() if word not in banned]
        
        # 단어별 등장횟수 카운팅 -> 새로운 단어라면 초기값 0으로 설정
        counter = {}
        for word in words:
            if word not in counter:
                counter[word] = 0
            counter[word] += 1
            
        # 카운팅이 최대값인 단어 반환
        return max(counter, key=counter.get)
    '''
    value 최대값이 여러개라면?
    [k for k,v in counter.items() if max(counter.values) == v]
    '''

# 다른 풀이 -> Counter 모듈의 most_common 메서드 활용
from collections import Counter
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]):
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
        # [('ball', 2)]에서 ball을 가져온다.
    
    # 더 간소화된 풀이
    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return Counter(w for w in words if w not in ban).most_common(1)[0][0]