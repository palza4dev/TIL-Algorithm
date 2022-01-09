'''
로그 파일 재정렬

1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output:       ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
'''

# 나의 풀이
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]):
        digits, letters = [], []
        
        for log in logs:
            if log.split()[1].isdigit(): # 식별자 다음 항목이 숫자인지 문자인지 판단.
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0])) # 식별자를 제외한 부분을 먼저 비교하고, 동일하면 식별자로 비교.
        
        return letters + digits  # 리스트를 합치는 연산자