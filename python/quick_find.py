from dynamic_array import dynamic_array

class quick_find(object):
    """ 
    An array in which :
        1. The index represents the element identifier
        2. The element represents the component identifier
    """

    def __init__(self,default_size)
        self.id = dynamic_array(default_size)

    def find(self,element):
        """
        return the component identifier of the given element
        """
        return self.id[element]

    def union(self,e_1,e_2):
        """
        cnnnect the components of given elements
        """
        if self.id[e_1] != self.id[e_2]:
            first_cid = self.id[e_1]
            second_cid = self.id[e_2]
            for i in self.id:
                if self.id[i]==second_cid:
                    self.id[i] = first_cid

    def connected(self,e_1,e_2):
        """
        return true if the elements are connected
        """
        return self.id[e_1]==self.id[e_2]
