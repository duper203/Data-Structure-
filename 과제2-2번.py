class Heap:
    def __init__(self,size):
        self.size = size
        self.heap = [None]*size
        self.count = 0

    def isempty(self): return self.count == 1
    def isfull(self): return self.size - 1== self.count

    def add_heap(self, item): #item추가
        list2 = []
        if self.isfull(): return
        self.count += 1
        i =self.count
        while i != 1 and item > self.heap[i//2]:
            self.heap[i] = self.heap[i // 2]
            i//= 2

        self.heap[i] = item


        for i in self.heap: #self.heap앞에 None을 제외하고 list2에 추가된 item들을 넣음
            if i != None:
                list2.append(i)


        j = 0
        total = 0
        for i in range(len(list2)): #트리 형식대로 출력이 가능하게 2**j 씩 레벨을 나눈다다
            if i == 0:
                print(list2[i])
                total += 2 ** j
                j += 1
                total += 2 ** j
            elif i == total - 1:
                print(list2[i])
                j += 1
                total += 2 ** j
            else:
                print(list2[i], end='')


h = Heap(100)

num = int(input("input"))
while not num == 999:
    h.add_heap(num)
    print()
    num = int(input("\ninput"))


