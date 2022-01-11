'''
팰린드롬 연결 리스트

연결 리스트가 팰린드롬인지 판별하라.

Input: head = [1,2,2,1]
Output: true
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 풀이 1 -> 리스트로 변환
from typing import List

class Solution:
    def isPalindrome(self, head: ListNode):
        q: List = []

        if not head:
            return True

        node = head
        # 리스트로 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        # 팰린드롬 판별
        return q == q[::-1]
    
        ''' 하나씩 판별
        while len(q) > 1:
            if q.pop(0) != q.pop(): -> 리스트에서 pop(0)의 시간복잡도는 O(N)이다.
                return False
        return True
        '''
        

# 풀이 2 ->  이중 연결 리스트인 데크를 활용한 최적화
import collections
from typing import Deque

class Solution:
    def isPalindrome(self, head: ListNode):
        # 데크 자료형 선언
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop(): # 맨 앞이나 뒤의 요소를 삭제할때 시간복잡도 O(1)
                return False

        return True

# 풀이 3 -> 러너를 이용한 풀이 [two runners pointer technique]
class Solution:
    def isPalindrome(self, head: ListNode):
        rev = None
        slow = fast = head
        # 러너를 이용해 역순 연결 리스트 구성
        while fast and fast.next: # 전체가 홀수개라면 fast가 None이 아니더라도 next가 None일때 멈춰야한다.
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next # 다중 할당을 해서 한 번의 트랜잭션으로 끝낸다. 분기로 나누면 결과가 달라진다. (불변객체를 참조)
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val: # rev의 마지막 노드는 초깃값 None이기 때문에 비교할 필요가 없다.
            slow, rev = slow.next, rev.next
        return not rev
''' 해설
# 러너 기법
1. 빠른 러너는 두칸씩, 느린 러너는 한칸씩 이동시킨다. (빠른 러너가 끝에 도달하면 느린 러너는 연결 리스트의 중간지점에 도착한다.)
2. 느린 러너가 중간지점에 도달하는 동안 지나온 노드를 역순으로 rev(연결 리스트)에 담는다.
3. 느린 러너가 중간지점부터 끝까지 도달하는 동안 거치는 노드를 rev의 노드와 비교한다.

# 초깃값
- 러너들의 초깃값은 모두 head에서 시작한다. 
- rev의 초깃값은 None에서 시작한다.

# rev 만들기
- rev 값은 slow가 되고, rev.next 값은 rev 값이 된다. 즉, 두번째 slow값 -> 첫번째 slow값 -> None(초깃값) 형태가 된다.
- 노드가 홀수개일때 rev는 중간값을 뛰어넘어야 한다. 홀수개이면 마지막에 fast.next가 None인데 fast가 None이 아니게 된다. 
   따라서 fast가 None이 아닌 경우 slow를 한칸 더 이동한다.

# 팰린드롬 판별
- rev 값이 None이 될때까지 노드를 거쳐간다.
- rev 값과 slow 값을 하나씩 비교한다.
- 모두 일치한다면 rev와 slow값은 결국 None이 된다.
'''