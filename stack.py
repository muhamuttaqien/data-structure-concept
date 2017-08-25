class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def get_list(self):
        return self.items

print("=== STACK - Last In First Out")
data = input("[INT, 0 to exit] What is your data? ")
s = Stack()
while data != 0:
    s.push(data)
    print(s.get_list())
    data = input('[INT, 0 to exit] What is your data? ')

data = raw_input("[Y/N] Remove data: ")
data = data.upper()
while data !=  'N':
    s.pop()
    print(s.get_list())
    data = raw_input('[[Y/N] Remove data: ')

print('Thank you!')