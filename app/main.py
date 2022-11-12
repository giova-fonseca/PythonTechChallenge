MAX_VALUE = 1000

class DataCapture():
    def __init__(self):
        self.data = []
    
    def add(self,value:int):
        try:
            if value and int(value) and value <= MAX_VALUE:
                self.data.append(value)
                self.data.sort()
        except ValueError as e:
            print(f"Error executing method add for the value {value} {e.__str__()}")            
        except Exception as e:
            print(f"Error executing method add for the value {value}")
        
    
    
    def build_stats(self,value:int):
        print(self.data.index(value))
        return len(self.data)

    
    def less(self,value:int):
        pass
    
    def __str__(self):
        return f"This is the content of data {self.data.__str__()}"
    
capture = DataCapture()
capture.add(value=4)
capture.add(value=8)
capture.add(value=7)
capture.add(value=3)
stats = capture.build_stats(4)

print(capture.__str__())
print(stats)