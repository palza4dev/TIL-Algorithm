'''
유효한 팰린드롬

주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

# 나의 풀이
class Solution:
    def isPalindrome(self, s: str):
        forward = []
        for str in s:
            if str.isalnum():
                forward.append(str.lower())
        if forward == forward[::-1]:
            return True
        else:
            return False

# 다른 풀이 1
class Solution:
    def isPalindrome(self, s: str):
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별 -> 맨 앞과 맨 뒤를 비교해간다
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():  # 리스트의 pop(0)은 O(n)
                return False

        return True

# 다른 풀이 2 -> 데크 자료형 활용
from collections import deque

class Solution:
    def isPalindrome(self, s: str):
        # 데크 자료형으로 선언
        strs = deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop(): # 데크의 popleft는 O(1)
                return False

        return True

# 다른 풀이 3 -> 정규표현식
import re

class Solution:
    def isPalindrome(self, s: str):
        s = s.lower()
        # 불필요한 문자를 교체해서 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱