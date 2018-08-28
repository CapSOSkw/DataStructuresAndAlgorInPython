import time
class Stack(list):

    def push(self, n):
        self.append(n)


    def is_empty(self):
        return self.__len__() == 0

    @property
    def top(self):
        return self[-1]



if __name__ == '__main__':
    stack = Stack()


    stack.push(5)

    print(stack.top)