class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_num or self.min_num[-1] >= val:
            self.min_num.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

        if self.min_num and val == self.min_num[-1]:
            self.min_num.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        if self.min_num:
            return self.min_num[-1]



obj = MinStack()
obj.push(3)
obj.push(2)
obj.push(2)
obj.push(5)
obj.pop()
print(obj.top())
print(obj.getMin())
