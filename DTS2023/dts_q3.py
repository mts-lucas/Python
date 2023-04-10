
class Faturameto:

    def __init__(self, array) -> None:
        self.array = array
        self.arrayNotNull = self.notNull()

    def notNull(self):
        arrayNotNull: list[float] = []

        for i in self.array:
            if i is not None:
                arrayNotNull.append(i)
        return arrayNotNull

    def minor(self) -> float:
        return min(self.arrayNotNull)

    def major(self) -> float:
        return max(self.arrayNotNull)

    def media(self) -> float:

        return (sum(self.arrayNotNull))/len(self.arrayNotNull)

    def betterDaysFat(self):
        betterDays: int = 0
        for i in self.arrayNotNull:
            if i > self.media():
                betterDays += 1
        return betterDays


random_list = [3221.4, 2660.49, None, 4949.09, 2602.33,
               3915.64, 2408.16, 4216.23, 2125.74, 4775.53, None, 3043.24]

fat = Faturameto(random_list)
print(f'minor value is {fat.minor()}')
print(f'major value is {fat.major()}')
print(f'better days count {fat.betterDaysFat()}')
