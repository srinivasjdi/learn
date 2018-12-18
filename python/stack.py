class stack:
    data = []

    def __init__(self,initializer=None):
        if initializer:
            for item in initializer: 
                self.data.append(item)

    def push(self,element):
        self.data.append(element)

    def pop(self):
        if self.data != []:
            del self.data[-1]
        else:
            print("cannot delete from empty stack")

    def display(self):
        for item in self.data:
            print(item)









