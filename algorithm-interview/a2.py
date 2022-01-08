'''
문자열 뒤집기

문자열을 뒤집는 함수를 작성하라.
입력값은 문자 배열이며, 리턴없이 리스트 내부를 직접 조작하라.
'''
from typing import List

# 나의 풀이 -> 투 포인터 스왑
class Solution:
    def reverseString(self, s: List[str]):

        left, right = 0, len(s)-1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
# 다른 풀이 -> reverse()
class Solution:
    def reverseString(self, s: List[str]):
        s.reverse() # 또는 s[::-1] 가능하지만 리트코드 시간복잡도 제한으로 s[:] = s[::-1]