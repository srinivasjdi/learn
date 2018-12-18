class dynamic_array(object):
    def __init__(self,default_capacity=32,initializer=None):
        self.data = [initializer]*default_capacity
        self.capacity = default_capacity
        if initializer:
            self.size = self.capacity
        else:
            self.size = 0 

    def __setitem__(self,index,value):
        if index >= self.capacity:
            self.reset()
        self.data[index] = value
        if index > self.size:
            self.size = index

    def __getitem__(self,index):
        if index >= self.size:
            return IndexError("Index out of bounds !")
        return self.data[index]

    def reset(self):
        print("reset called")
        self.capacity = 2 * self.capacity
        self._new_data = [None]*self.capacity
        for i in range(len(self.data)):
            self._new_data[i] = self.data[i]
        self.data = self.new_data
    
    def display(self):
        print("repr called")
        for i,item in enumerate(self.data):
            print("{} ---> {}".format(i,item))
        print("repr ended")
