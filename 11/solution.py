from collections import deque 
# dictionary that takes the difference in position between the head and the tail
# and returns the movement of the tail

class Monkey:
    def __init__(self, items, operation, test_divisor, true_monkey, false_monkey) -> None:
        self.items = deque(items)
        self.operation = operation
        self.test_divisor = test_divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect = 0
    
    def test(self, worry_level):
        return worry_level % self.test_divisor == 0
    
    def throw_item(self):
        # pops an item from the left
        self.inspect += 1
        item = self.items.popleft()
        # applies the operation to it then divides by 3
        item = self.operation(item)
        # returns the item to be thrown and the monkey to throw it to
        if self.test(item):
            return item, self.true_monkey
        else:
            return item, self.false_monkey
    
    def throw_item_with_divisor(self):
        # pops an item from the left
        self.inspect += 1
        item = self.items.popleft()
        # applies the operation to it
        item = self.operation(item) 
        # returns the item to be thrown and the monkey to throw it to
        if self.test(item):
            return item, self.true_monkey
        else:
            return item, self.false_monkey

def get_test():
    test = [
        Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
        Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
        Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
        Monkey([74], lambda x: x + 3, 17, 0, 1),
    ]
    return test

def get_monkeys():
    monkeys = [
        Monkey([56, 52, 58, 96, 70, 75, 72], lambda x: x * 17, 11, 2, 3),
        Monkey([75, 58, 86, 80, 55, 81], lambda x: x + 7, 3, 6, 5),
        Monkey([73, 68, 73, 90], lambda x: x * x, 5, 1, 7),
        Monkey([72, 89, 55, 51, 59], lambda x: x + 1, 7, 2, 7),
        Monkey([76, 76, 91], lambda x: x * 3, 19, 0, 3),
        Monkey([88], lambda x: x + 4, 2, 6, 4),
        Monkey([64, 63, 56, 50, 77, 55, 55, 86], lambda x: x + 8, 13, 4, 0),
        Monkey([79, 58], lambda x: x + 6, 17, 1, 5),
    ]
    return monkeys

def solution1(monkey_array):
    for i in range(20):
        for j in range(len(monkey_array)):
            while len(monkey_array[j].items) > 0:
                item, monkey = monkey_array[j].throw_item()
                monkey_array[monkey].items.append(item)

    monkey_inspections = []

    for j in range(len(monkey_array)):
        monkey_inspections.append(monkey_array[j].inspect)
    monkey_inspections.sort()

    return monkey_inspections[-1] * monkey_inspections[-2]

def solution2(monkey_array):
    common_product = 1
    for i in range(len(monkey_array)):
        common_product *= monkey_array[i].test_divisor

    for i in range(10000):
        for j in range(len(monkey_array)):
            while len(monkey_array[j].items) > 0:
                item, monkey = monkey_array[j].throw_item_with_divisor()
                monkey_array[monkey].items.append((item % common_product))

    monkey_inspections = []

    for j in range(len(monkey_array)):
        monkey_inspections.append(monkey_array[j].inspect)
    monkey_inspections.sort()

    return monkey_inspections[-1] * monkey_inspections[-2]
    
if __name__ == '__main__':
    f = open('input.txt', 'r')

    inputarray = f.read().splitlines()

    print(solution1(get_monkeys()))
    print(solution2(get_monkeys()))
