class ListArray(object):

    def __init__(self):
        self.array = []

    def insert_last(self, b):
        self.array.append(b)

    def delete_last(self):
        self.array.remove(self.array[len(self.array)-1])

    def insert_first(self, b):
        self.array = [b] + self.array

    def delete_first(self):
        self.array.remove(self.array[0])

    def insert(self, b, i):
        if i == len(self.array):
            self.insert_last(b)
        else:
            lst1 = [self.array[j] for j in range(i)]
            lst2 = [self.array[j] for j in range(i + 1, len(self.array))]
            self.array = lst1 + [b] + lst2

    def delete(self, i):
        self.array.remove(self.array[i])

    def __len__(self):
        return len(self.array)



