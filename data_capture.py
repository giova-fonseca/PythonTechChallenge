# Const for the max value in the structure

MAX_VALUE = 1000

class DataCapture:
    # Constructor for the class DataCapture, includes three structures.     
               
    def __init__(self):
        self.data = []
        self.dataOrderAsc:list = []
        self.dataOrderDes:list = []

    def __str__(self):
        return f"This is the content of data {self.data.__str__()}"

    
    def validateInput(self,value:int)->bool:
    # Method to validate if a value is type int and is within the defined range of values.
    # return True/False
    
        
        if type(value) == int:
            if value <= MAX_VALUE and value>=0:
                return True
            else:
                return False
        return False
    
    @staticmethod    
    def searchValueAsc(list_values:list, position:int, search_value:int):
    # Static method implements binary search with a ascending sorted list.
    
        pos = -1 
        izq = 0
        der = len(list_values) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if list_values[medio] == search_value:
                pos = medio     
            if list_values[medio] > search_value:
                der = medio - 1
            else:               
                izq = medio + 1 
        return pos
    

    @staticmethod    
    def searchValueDes(list_values:list, position:int, search_value:int):
    # Static method implements binary search with a descending sorted list.
    
        pos = -1 
        izq = 0
        der = len(list_values) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if list_values[medio] == search_value:
                pos = medio     
            if list_values[medio] < search_value:
                der = medio - 1
            else:               
                izq = medio + 1 
        if pos != -1:
            return pos-1
        else:
            return pos
        
                
    def add(self,value:int):
    # Method to add new value in main structure, validate the type and range of values between 0 and 1000.
        try:  
            if self.validateInput(value):
                self.data.append(value)
            else:
                raise ValueError("The value must be less than 1000 and greater than 0 and Integer type")                                     
        except ValueError as e:
            print(f"Error executing method add for the value {value}. {e.__str__()}")
        except Exception as e:
            print(f"Error executing method add for the value {value}. {e.__str__()}")
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
        
        if self.validateInput(value):           
            if value < self.dataOrderAsc[0]:
                return len(self.dataOrderAsc)
            else:
                position = int(len(self.dataOrderAsc)/2)
            
                try:
                    return self.searchValueAsc(self.dataOrderAsc,position,value)
                except TypeError as ex:
                    print(f"TypeError exception {ex}")
                except Exception as ex:
                    print(f"Exception {ex}")
        else:                
            raise ValueError("The value must be less than 1000 and greater than 0 and Integer type")                                     


    def greater(self,value:int)-> int:
    # Receive value per parameter, to determine how many elements in the structure are greater than it
    # and return the count of items.    
    
        if self.validateInput(value):           
            if value > self.dataOrderDes[0]:
                return len(self.dataOrderDes)
            else:
                position = int(len(self.dataOrderDes)/2)
            
                try:
                    return self.searchValueDes(self.dataOrderDes,position,value)
                except TypeError as ex:
                    print(f"TypeError exception {ex}")
                except Exception as ex:
                    print(f"Exception {ex}")
        else:                
            raise ValueError("The value must be less than 1000 and greater than 0 and Integer type")                                     



    
    def between(self,value1:int, value2:int)-> int:
    # Receive two values ​​per parameter, to determine how many elements of the structure are within 
    # the range of both parameters.
        
        try:
            if self.validateInput(value1) and self.validateInput(value2):
                if value1>value2:
                    posIni =  self.searchValueAsc(self.dataOrderAsc,int(len(self.dataOrderAsc)/2),value2)
                    posFin =  self.searchValueDes(self.dataOrderDes,int(len(self.dataOrderDes)/2),value1)
                    
                    x = self.dataOrderAsc[posIni:len(self.data)-posFin]                    
                else:
                    posIni =  self.searchValueAsc(self.dataOrderAsc,int(len(self.dataOrderAsc)/2),value1)                    
                    posFin =  self.searchValueDes(self.dataOrderDes,int(len(self.dataOrderDes)/2),value2)
                    
                    x = self.dataOrderAsc[posIni:len(self.data)-posFin]
                                        
                return len(x)
            else:
                raise TypeError("The value must be Integer")
        except TypeError as ex:
            print(f"TypeError exception {ex}")
        except Exception as ex:
            print(f"Exception {ex}")


