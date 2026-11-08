class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]

    def modulo_hash(self,key):
        return key%self.size

    def mid_square(self,key):
        square=key**2
        str_square=str(square)
        r=len(str(self.size))-1
        L=len(str_square)-1
        mid=L//2
        res=int(str_square[mid:mid+r])
        print(res)
        return res % self.size

    def insert(self,key,value):
        index=self.mid_square(key)
        for pairs in self.table[index]:
            if pairs[0]==key:
                pairs[1]=value
                return
        self.table[index].append([key,value])

    def linear_probing(self,key,value):
        i=0
        index=self.modulo_hash(key) % self.size
        while len(self.table[index]) != 0:
            i += 1
            index = (self.modulo_hash(key)+i) % self.size
        self.table[index] =[key,value]


    def search(self,key):
        index=self.mid_square(key)
        flag=False
        for k,value in self.table[index]:
            if key ==k:
                flag=True
                print(value)
                return
        if not flag:
            print("not found")         
    
    def display(self):
        for i,chain in enumerate(self.table):
            if chain:
                print(f"index[{i}]:{chain}")

h = HashTable(100)

# Inserting values into the table
h.insert(11, "Alpha")   # 11^2 = 121, mid digits -> 2, index = 2
h.insert(111, "Beta")   # 111^2 = 12321, mid digits -> 2, index = 2 (collision)
h.insert(201, "Gamma")  # 201^2 = 40401, mid digits -> 0, index = 0
h.insert(1001, "Delta") # 1001^2 = 1002001, mid digits -> 0, index = 0 (collision)
h.insert(211, "Epsilon") # 211^2 = 44521, mid digits -> 4, index = 4

# Additional inputs for more collisions
h.insert(22, "Zeta")    # 22^2 = 484, mid digits -> 8, index = 8
h.insert(32, "Eta")     # 32^2 = 1024, mid digits -> 0, index = 0 (collision)
h.insert(44, "Theta")   # 44^2 = 1936, mid digits -> 9, index = 9
h.insert(55, "Iota")    # 55^2 = 3025, mid digits -> 0, index = 0 (collision)
h.insert(77, "Kappa")   # 77^2 = 5929, mid digits -> 9, index = 9 (collision)

# Display the hash table with all inserted values
h.display()
        
h.search(55)

h.mid_square(1234)


h.linear_probing(10, "Alpha")
h.linear_probing(110, "Beta")
h.linear_probing(210, "Gamma")

# Colliding at Index 25
h.linear_probing(25, "Delta")
h.linear_probing(125, "Epsilon")

# Colliding at Index 42
h.linear_probing(42, "Zeta")
h.linear_probing(142, "Eta")
h.linear_probing(242, "Theta")

# Colliding at Index 67
h.linear_probing(67, "Iota")
h.linear_probing(167, "Kappa")

# Colliding at Index 88
h.linear_probing(88, "Lambda")
h.linear_probing(188, "Mu")
h.linear_probing(288, "Nu")

h.display()


