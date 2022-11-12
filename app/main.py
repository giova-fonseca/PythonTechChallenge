MAX_VALUE = 1000

class DataCapture():
    def __init__(self):
        self.data = []
        self.mySet = set()
            
    def add(self,value:int):
        try:           
            if value:
                if type(value) ==int:
                    if value <= MAX_VALUE:                    
                        self.data.append(value)
                        self.data.sort()
                    else:
                        raise ValueError("The value must be less than 1000")
                        
                else:
                    raise TypeError("The value must be Integer type")
                                        
        except ValueError as e:
            print(f"Error executing method add for the value {value} {e.__str__()}")            
        except Exception as e:
            print(f"Error executing method add for the value {value}")
        
    
    
    def build_stats(self,value:int):
        try:
            if type(value) == int:
                self.mySet.update(self.data)
                print(f"Founded in the position {self.data.index(value)}")
                print(f"Less than {value} are {self.data.index(value)}")
                print(f"Greater than {value} are {len(self.data)-self.data.index(value)-1}")
                print(f"Counts of items in the set {len(self.mySet)}")
                print(f"Items in the set {self.mySet}")
                print(f"Counts of items in the stats {len(self.data)}")
                return self.mySet
            else:
                raise TypeError("The value must be Integer")
        except TypeError as ex:
            print(ex)
        except Exception as ex:
            print(ex)
    
    def less(self,value:int):
        pass
    
    def __str__(self):
        return f"This is the content of data {self.data.__str__()}"
    
capture = DataCapture()
capture.add(value=4)
capture.add(value=3)
capture.add(value=2)
capture.add(value=5)
capture.add(value=7)
capture.add(value=3)
stats = capture.build_stats(4)
print(capture.__str__())
print(stats)