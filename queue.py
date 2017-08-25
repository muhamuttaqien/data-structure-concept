class Queue:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_list(self):
        return self.items

print("=== STACK - First In First Out")
data = input("[INT, 0 to exit] What is your data? ")
q = Queue()
while data != 0:
    q.enqueue(data)
    print(q.get_list())
    data = input('[INT, 0 to exit] What is your data? ')

data = raw_input("[Y/N] Remove data: ")
data = data.upper()
while data !=  'N':
    q.dequeue()
    print(q.get_list())
    data = raw_input('[[Y/N] Remove data: ')

print('Thank you!')