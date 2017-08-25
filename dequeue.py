class Dequeue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)
        
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def get_list(self):
        return self.items

print("=== DEQUEUE - First In First Out for Both Side")
data = input("[INT, 0 to exit] What is your data? ")
dq = Dequeue()
while data != 0:
    dq.add_front(data)
    print(dq.get_list())
    data = input('[INT, 0 to exit] What is your data? ')

data = raw_input("[Y/N] Remove data: ")
data = data.upper()
while data !=  'N':
    dq.remove_front()
    print(dq.get_list())
    data = raw_input('[[Y/N] Remove data: ')

print('Thank you!')