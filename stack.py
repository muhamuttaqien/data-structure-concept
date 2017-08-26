class Stack:

    def __init__(self):
        self.items = []

    def _is_empty(self):
        return self.items == []

    def _push(self, item):
        self.items.append(item)

    def _pop(self):
        return self.items.pop()

    def _peek(self):
        return self.items[len(self.items)-1]

    def _size(self):
        return len(self.items)

    def _get_list(self):
        return self.items


def main():
    print("=== STACK - Last In First Out")
    data = input("[INT, 0 to exit] What is your data? ")
    s = Stack()
    while data != 0:
        s._push(data)
        print(s._get_list())
        data = input('[INT, 0 to exit] What is your data? ')

    data = raw_input("[Y/N] Remove data: ")
    data = data.upper()
    while data !=  'N':
        s._pop()
        print(s._get_list())
        data = raw_input('[[Y/N] Remove data: ')

    print('Thank you!')


if __name__=='__main__':
	main()