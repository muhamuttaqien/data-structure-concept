class Queue:

    def __init__(self):
        self.items = []
    
    def _is_empty(self):
        return self.items == []

    def _enqueue(self, item):
        self.items.insert(0, item)

    def _dequeue(self):
        return self.items.pop()

    def _size(self):
        return len(self.items)

    def _get_list(self):
        return self.items

print("=== QUEUE - First In First Out")
data = input("[INT, 0 to exit] What is your data? ")
q = Queue()
while data != 0:
    q._enqueue(data)
    print(q._get_list())
    data = input('[INT, 0 to exit] What is your data? ')

data = raw_input("[Y/N] Remove data: ")
data = data.upper()
while data !=  'N':
    q._dequeue()
    print(q._get_list())
    data = raw_input('[[Y/N] Remove data: ')

print('Thank you!')