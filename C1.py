class Person:
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def __EQ__(self, other):
        return self.first == other.first and self.last == other.last

    def __NE__(self, other):
        return not self == other

    def __lt__(self, other):
        return len(self.last) < len(other.last) or len(self.last) == len(other.last) and len(self.first) < len(other.first)

    def __gt__(self, other):
        return len(self.last) > len(other.last) or len(self.last) == len(other.last) and len(self.first) > len(other.first)

    def __add__(self, other):
        return Person(self.first + self.last , other.first + other.last)


p_1 = Person("Mehadi", "Hasan")
p_2 = Person("Rashed", "Mahbub")

if p_1 == p_2:
    print("They are Equal")

if p_1 != p_2:
    print("They are not Equal")

if p_1 < p_2:
    print("p_1 is less than p_2")

if p_1 > p_2:
    print("p_1 is greater than p_2")

sum = p_1 + p_2
print(sum.first, sum.last)