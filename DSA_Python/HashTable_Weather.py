class Weather:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, ele in self.arr[h]:
            if ele[0] == key:
                del self.arr[h][index]

    def avg_of_temp(self):
        sum = 0
        count = 0
        for sublist in self.arr:
            for key, temp in sublist:
                sum += temp
                count += 1
        if count == 0:
            return
        return round(sum / count, 2)

    def max_of_temp(self):
        t = []
        for sublist in self.arr:
            for key, temp in sublist:
                t.append(temp)
        return max(t)


NY = Weather()
NY["Jan 1"] = 27
NY["Jan 2"] = 31
NY["Jan 3"] = 23
NY["Jan 4"] = 34
NY["Jan 5"] = 37
NY["Jan 6"] = 38
NY["Jan 7"] = 29
NY["Jan 8"] = 30
NY["Jan 9"] = 35
NY["Jan 10"] = 30
NY["Jan 11"] = 45

print(NY.arr)

print("Average temp:{}".format(NY.avg_of_temp()))
print("Max Temp:{}".format(NY.max_of_temp()))
