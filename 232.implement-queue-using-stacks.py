#
# @lc app=leetcode.cn id=232 lang=python3
# @lcpr version=30204
#
# [232] 用栈实现队列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        p = self.stack[0]
        self.stack = self.stack[1:]
        return p


    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end



#
# @lcpr case=start
# ["MyQueue", "push", "push", "peek", "pop", "empty"][[], [1], [2], [], [], []]\n
# @lcpr case=end

#

