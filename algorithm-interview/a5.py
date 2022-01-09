'''
두 수의 합

덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''

# 나의 풀이 -> O(n^2)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
                
# 다른 풀이 1 -> O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int):
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

    # 개선된 풀이
    def twoSum(self, nums: List[int], target: int):
        nums_map = {}
        # 하나의 `for`문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i