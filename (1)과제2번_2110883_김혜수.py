#2장 10(2)문제
#튜플 리스트를 다시 원래의 행렬 형식으로 출력하는 함수
class sparsematrix:
    def __init__(self):
        self.tuple = [(0, 1, 3), (0, 3, 2), (1, 0, 8), (1, 2, 4), (2, 3, 5)]
        #희소행렬에서 0이 아닌 원소만을 튜플(행, 열, 값)현식으로 리스트에 저장
        self.array1 = [[0]*4 for i in range(3)] #3x4배열 선언

    def matrix(self):#tuple리스트의 튜플을 하나씩 꺼내어 해당 행과열에 맞게 값을 넣는다
        for tuple1 in self.tuple:
            x, y, i = tuple1
            self.array1[x][y] = i


s = sparsematrix()
s.matrix()

for i in s.array1:
    for j in i:
        print("%2d" %j, end = '')
    print()