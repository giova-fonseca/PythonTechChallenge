from data_capture import DataCapture

from unittest import TestCase, main
# from app.app import DataCapture


class TestDataCapture(TestCase):
   
    def test_add(self):
        capture = DataCapture()
        capture.add(value=3)
        capture.add(value=4)
        capture.add(value=3)
        capture.add(value=6)
        capture.add(value=9)
        capture.build_stats()   
        self.assertIn(4,capture.data)
        self.assertNotIn(5,capture.data)

    def test_less(self):
        capture = DataCapture()
        capture.add(value=3)
        capture.add(value=4)
        capture.add(value=3)
        capture.add(value=6)
        capture.add(value=9)
        capture.build_stats()           
        self.assertEqual(2,capture.less(4),"Test Less OK")

    
    def test_greater(self):
        capture = DataCapture()
        capture.add(value=3)
        capture.add(value=4)
        capture.add(value=3)
        capture.add(value=6)
        capture.add(value=9)
        capture.build_stats()           
        self.assertEqual(1,capture.greater(6),"Test Greater OK")
    

    def test_between(self):
        capture = DataCapture()
        capture.add(value=3)
        capture.add(value=4)
        capture.add(value=3)
        capture.add(value=6)
        capture.add(value=9)
        capture.build_stats()           
        self.assertEqual(4,capture.between(3,6),"Test Between OK")


if __name__ == '__main__':
    main()
    