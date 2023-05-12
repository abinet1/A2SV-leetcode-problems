class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.current_size = 0
        self.circular_deque = []        

    def insertFront(self, value: int) -> bool:
        if self.current_size<self.size:
            self.current_size+=1
            self.circular_deque.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.current_size<self.size:
            self.circular_deque.insert(self.current_size, value)
            self.current_size+=1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.current_size>0:
            self.circular_deque.pop(0)
            self.current_size-=1
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.current_size>0:
            self.circular_deque.pop()
            self.current_size-=1
            return True
        return False

    def getFront(self) -> int:
        return self.circular_deque[0] if self.current_size>0 else -1
        
    def getRear(self) -> int:
        return self.circular_deque[self.current_size-1] if self.current_size>0 else -1

    def isEmpty(self) -> bool:
        return True if self.current_size == 0 else False 

    def isFull(self) -> bool:
        return True if self.current_size == self.size else False 