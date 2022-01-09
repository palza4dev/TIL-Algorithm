'''
배열 파티션 I

n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

Input: nums = [1,4,3,2]
Output: 4
'''

# 나의 풀이 -> 오름차순 정렬 후 짝수번째의 합 구하기
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]):
        nums.sort()
        sum = 0
        
        for i, n in enumerate(nums):
            if i%2 == 0:
                sum += n
        return sum

# 다른 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]):
        return sum(sorted(nums)[::2])