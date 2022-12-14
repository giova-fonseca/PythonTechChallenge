from data_capture import DataCapture
from unittest import TestCase, main


class TestDataCapture(TestCase):
    
    def load_List(self):
        # Create a test list with 99 random items.
        capture = DataCapture()        
        capture.add(value=29)
        capture.add(value=30)
        capture.add(value=40)
        capture.add(value=47)
        capture.add(value=68)
        capture.add(value=24)
        capture.add(value=21)
        capture.add(value=95)
        capture.add(value=49)
        capture.add(value=9)
        capture.add(value=11)
        capture.add(value=73)
        capture.add(value=83)
        capture.add(value=23)
        capture.add(value=89)
        capture.add(value=65)
        capture.add(value=30)
        capture.add(value=31)
        capture.add(value=87)
        capture.add(value=59)
        capture.add(value=96)
        capture.add(value=7)
        capture.add(value=37)
        capture.add(value=48)
        capture.add(value=58)
        capture.add(value=10)
        capture.add(value=58)
        capture.add(value=19)
        capture.add(value=17)
        capture.add(value=31)
        capture.add(value=68)
        capture.add(value=46)
        capture.add(value=61)
        capture.add(value=81)
        capture.add(value=54)
        capture.add(value=65)
        capture.add(value=15)
        capture.add(value=30)
        capture.add(value=19)
        capture.add(value=83)
        capture.add(value=10)
        capture.add(value=80)
        capture.add(value=70)
        capture.add(value=69)
        capture.add(value=1)
        capture.add(value=70)
        capture.add(value=45)
        capture.add(value=97)
        capture.add(value=92)
        capture.add(value=71)
        capture.add(value=89)
        capture.add(value=31)
        capture.add(value=98)
        capture.add(value=24)
        capture.add(value=65)
        capture.add(value=38)
        capture.add(value=27)
        capture.add(value=57)
        capture.add(value=29)
        capture.add(value=19)
        capture.add(value=65)
        capture.add(value=45)
        capture.add(value=50)
        capture.add(value=47)
        capture.add(value=39)
        capture.add(value=83)
        capture.add(value=14)
        capture.add(value=66)
        capture.add(value=44)
        capture.add(value=95)
        capture.add(value=12)
        capture.add(value=73)
        capture.add(value=50)
        capture.add(value=14)
        capture.add(value=61)
        capture.add(value=83)
        capture.add(value=65)
        capture.add(value=80)
        capture.add(value=25)
        capture.add(value=77)
        capture.add(value=94)
        capture.add(value=87)
        capture.add(value=1)
        capture.add(value=97)
        capture.add(value=88)
        capture.add(value=3)
        capture.add(value=87)
        capture.add(value=5)
        capture.add(value=8)
        capture.add(value=64)
        capture.add(value=38)
        capture.add(value=3)
        capture.add(value=59)
        capture.add(value=25)
        capture.add(value=2)
        capture.add(value=16)
        capture.add(value=28)
        capture.add(value=96)
        capture.add(value=88)
        return capture
               

    def test_add(self):
        # Test the add method of the class DataCapture.
        temp_capture = DataCapture()        
        temp_capture.add(value=5)
        temp_capture.add(value=18)
        temp_capture.build_stats()
        self.assertIn(5,temp_capture.dataOrderAsc,"ok")
        self.assertIn(18,temp_capture.dataOrderAsc,"ok")

    def test_less(self):
        # Test the less method of the class DataCapture
        capture = self.load_List()
        capture.build_stats()     
              
        print(f"List of values for the test \n {capture.dataOrderAsc}")
        self.assertNotIn(4,capture.dataOrderAsc,"Not Founded")
        self.assertEqual(-1,capture.less(4),"Test Less OK")
        self.assertEqual(7,capture.less(8),"Test Less OK")
        self.assertEqual(5,capture.less(5),"Test Less OK")
        self.assertEqual(99,capture.less(150),"Test Less OK")
    
    def test_greater(self):
        # Test the greater method of the class DataCapture
                
        capture = self.load_List()
        capture.build_stats()           
        self.assertEqual(97,capture.greater(1),"Test Greater OK")
        self.assertEqual(94,capture.greater(3),"Test Greater OK")
        self.assertGreater(6,capture.greater(95),"Is greater")

        if self.assertNotIn(4,capture.dataOrderDes,"Values"):
            self.assertEqual(-1,capture.greater(4),"This value is not in the list")
            
        self.assertEqual(99,capture.greater(0),"Is greater")
                       
    def test_between(self):
        # Test the between method of the class DataCapture
        
        capture = self.load_List()
        capture.build_stats()           
        self.assertEqual(6,capture.between(1,5),"Test Between OK")
        self.assertEqual(7,capture.between(10,15),"Test Between OK")
        self.assertEqual(4,capture.between(1,3),"Test Between OK")


if __name__ == '__main__':
    main()
    
    