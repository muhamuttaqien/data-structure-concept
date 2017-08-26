class Dequeue:

    def __init__(self):
        self.items = []

    def _is_empty(self):
        return self.items == []

    def _add_front(self, item):
        self.items.append(item)

    def _add_rear(self, item):
        self.items.insert(0, item)

    def _remove_front(self):
        return self.items.pop()

    def _remove_rear(self):
        return self.items.pop(0)
        
    def _peek(self):
        return self.items[len(self.items)-1]

    def _size(self):
        return len(self.items)

    def _get_list(self):
        return self.items

print("=== DEQUEUE - First In First Out for Both Side")
data = input("[INT, 0 to exit] What is your data? ")
dq = Dequeue()
while data != 0:
    dq._add_front(data)
    print(dq._get_list())
    data = input('[INT, 0 to exit] What is your data? ')

data = raw_input("[Y/N] Remove data: ")
data = data.upper()
while data !=  'N':
    dq._remove_front()
    print(dq._get_list())
    data = raw_input('[[Y/N] Remove data: ')

print('Thank you!')