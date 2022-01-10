'''
주식을 사고팔기 가장 좋은 시점

한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

날짜 순서로 이어져서 역행할 수 없다.

Input: prices = [7,1,5,3,6,4]
Output: 5
'''

# 풀이 -> 카데인 알고리즘
import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]):
        profit = 0
        min_price = sys.maxsize

        # 최소값과 최대값 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit