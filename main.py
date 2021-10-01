import random

class RandomTable:
    elements: list[list[float]] = []

    def fill(self) -> list[list[float]]:
        self.elements = [[random.randrange(100, 5000)/100 for i in range(10)] for j in range(10)]
        return self.elements

    def largest(self) -> float:
        return max(max(x) for x in self.elements)

    def avg(self) -> float:
        zipped = [float(sum(l))/len(l) for l in zip(*self.elements)]
        return sum(zipped) / len(zipped)

    def above_avg(self) -> int:
        cur_avg = self.avg()
        above = 0

        for i in range(len(self.elements)):
            for j in range(i):
                if self.elements[i][j] > cur_avg:
                    above += 1
        
        return above

def main():
    table = RandomTable()
    table.fill()
    print("Največji element ", table.largest())
    print("Povprečje ", table.avg())
    print("Število elementov nad povprečjem ", table.above_avg())

if __name__ == "__main__":
    main()
