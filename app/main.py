MAX_VALUE = 1000

class DataCapture():
    def __init__(self):
        self.data = []
        self.dataOrderAsc = []
        self.dataOrderDes = []
        # self.mySet = set()

    def __str__(self):
        return f"This is the content of data {self.data.__str__()}"

            
    def add(self,value:int):
        try:           
            if value:
                if type(value) ==int:
                    if value <= MAX_VALUE:                    
                        self.data.append(value)
                    else:
                        raise ValueError("The value must be less than 1000")
                        
                else:
                    raise TypeError("The value must be Integer type")
                                        
        except ValueError as e:
            print(f"Error executing method add for the value {value} {e.__str__()}")            
        except Exception as e:
            print(f"Error executing method add for the value {value}")      
    
    
    def build_stats(self):
        try:
            # import pdb;
            # pdb.set_trace()
            
            self.dataOrderAsc = self.data.copy()
            self.dataOrderAsc.sort()
            self.dataOrderDes = self.data.copy()
            self.dataOrderDes.sort(reverse=True)
            return self
        except TypeError as ex:
            print(ex)
        except Exception as ex:
            print(ex)
           
           
    def less(self,value:int)-> int:
        try:
            if type(value) == int:
                return self.dataOrderAsc.index(value)
            else:
                raise TypeError("The value must be Integer")
        except TypeError as ex:
            print(ex)
        except Exception as ex:
            print(ex)


    def greater(self,value:int)-> int:
        try:
            if type(value) == int:
                return self.dataOrderDes.index(value)
            else:
                raise TypeError("The value must be Integer")
        except TypeError as ex:
            print(ex)
        except Exception as ex:
            print(ex)

    
    def between(self,value1:int, value2:int):
        try:
            if type(value1) == int and type(value2) == int:                
                if value1>value2:
                    posIni =  self.dataOrderAsc.index(value2)
                    posFin =  self.dataOrderDes.index(value1)
                    x = self.dataOrderAsc[posIni:len(self.data)-posFin]                    
                else:
                    posIni =  self.dataOrderAsc.index(value1)
                    posFin =  self.dataOrderDes.index(value2)
                    x = self.dataOrderAsc[posIni:len(self.data)-posFin]
                return len(x)
            else:
                raise TypeError("The value must be Integer")
        except TypeError as ex:
            print(ex)
        except Exception as ex:
            print(ex)
    
capture = DataCapture()
capture.add(value=2)
capture.add(value=3)
capture.add(value=9)
capture.add(value=3)
capture.add(value=4)
capture.add(value=4)
capture.add(value=6)
stats = capture.build_stats()
value = 4
print(f"The list of values is {stats.dataOrderAsc}")
print(f"The value to analyze is {value}")
print(f"Less {stats.less(value)}")

print(f"Greater {stats.greater(value)}")
val1 =4
val2 =3
print(f"Items between {val1} and {val2}: {stats.between(val1,val2)}")
