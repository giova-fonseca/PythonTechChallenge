# Const for the max value in the structure
MAX_VALUE = 1000

class DataCapture:
    # Constructor for the class DataCapture, includes three structures. 
    def __init__(self):
        self.data = []
        self.dataOrderAsc = []
        self.dataOrderDes = []
        # self.mySet = set()

    def __str__(self):
        return f"This is the content of data {self.data.__str__()}"

            
    def add(self,value:int):
    # Method to add new value in main structure, validate the type and range of values between 0 and 1000.
        try:           
            if value:
                if type(value) ==int:
                    if value <= MAX_VALUE and value >=0:                    
                        self.data.append(value)
                    else:
                        raise ValueError("The value must be less than 1000 and greater than 0")
                        
                else:
                    raise TypeError("The value must be Integer type")                                        
        except ValueError as e:
            print(f"Error executing method add for the value {value} {e.__str__()}")            
        except Exception as e:
            print(f"Error executing method add for the value {value}")      
        return self
    
    def build_stats(self):
    # Make a copy of the main structure in descending order and another copy in ascending order, 
    # and return self object.
        try:
            self.dataOrderAsc = self.data.copy()
            self.dataOrderAsc.sort()
            self.dataOrderDes = self.data.copy()
            self.dataOrderDes.sort(reverse=True)
            return self
        except TypeError as ex:
            print(f"TypeError exception {ex}")
        except Exception as ex:
            print(f"Exception {ex}")
           
           
    def less(self,value:int)-> int:
    # Receive value per parameter, to determine how many elements in the structure are less than it
    # and return the count of items.
        
        try:
            if type(value) == int:
                return self.dataOrderAsc.index(value)
            else:
                raise TypeError("The value must be Integer")
        except TypeError as ex:
            print(f"TypeError exception {ex}")
        except Exception as ex:
            print(f"Exception {ex}")


    def greater(self,value:int)-> int:
    # Receive value per parameter, to determine how many elements in the structure are greater than it
    # and return the count of items.    
    
        try:
            if type(value) == int:
                return self.dataOrderDes.index(value)
            else:
                raise TypeError("The value must be Integer")
        except TypeError as ex:
            print(f"TypeError exception {ex}")
        except Exception as ex:
            print(f"Exception {ex}")

    
    def between(self,value1:int, value2:int)-> int:
    # Receive two values ​​per parameter, to determine how many elements of the structure are within 
    # the range of both parameters.
        
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
            print(f"TypeError exception {ex}")
        except Exception as ex:
            print(f"Exception {ex}")
