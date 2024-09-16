class ReverseIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = len(my_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.my_list[self.index]


list_to_reverse = [4, 7, 10, 34]
reverse_iter = ReverseIterator(list_to_reverse)

for item in reverse_iter:
    print(item)
