import math

class bst():
    self._stage = 5
    self._default_size = int(math.pow(2,5)) 
    self.data = []*self._default_size
    self._empty_flag = [0]*self._default_size 

    def _left(self,x):
        return 2*x + 1

    def _right(self,x):
        return 2*x + 2
    
    def _extend_till(self,index):
        while len(self._data)<index:
            self._stage = self._stage + 1
            t = []*math.pow(2,self._stage)
            t[:len(self._data)]=l[:]
            self._data = t

    def _insert(self,element,root):
        if root >= len(self._data):
           self._extend_till(root)  

        if self._empty_flag[root]:
            self.data[root] = element
        else:
            if element<=self.data[root]:
                _insert(self,element,self._left(root))
            else:
                _insert(self,element,self._right(root))

    def insert(self,element):
        _insert(self,element,0)


    def search(self,element):


    def min(self):


    def max(self):


    def traverse(self):


    def delete(self,element):


