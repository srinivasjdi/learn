class queue:
    data = []
    
    def __init__(self,initializer=None):
        if initializer:
            for item in initializer:
                self.data.append(itr)

    def add(self,element):
        self.data.append(element)
        
    def remove(self):
        tmp =  self.data[0]
        del self.data[0]
        return tmp

    def display(self):
        print(data)
