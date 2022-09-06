import unittest 
from main import walk 

class TestMethods(unittest.TestCase):
    def test1D(self):
        w = walk(1,None,None,None,None)
        self.assertEqual(w.x,1)
        self.assertIsNone(w.y)
        self.assertIsNone(w.z)
        self.assertIsNone(w.a)
        print("test1d passed")
        
    def test2D(self):
        w = walk(1,2,None,None,None)
        self.assertEqual(w.x,1)
        self.assertEqual(w.y,2)
        self.assertIsNone(w.z)
        self.assertIsNone(w.a)
        print("test2d passed")
    
    def test3D(self):
        w = walk(1,2,3,None,None)
        self.assertEqual(w.x,1)
        self.assertEqual(w.y,2)
        self.assertEqual(w.z,3)
        self.assertIsNone(w.a)
        print("test3d passed")

    def test4D(self):
        w = walk(1,2,3,4,None)
        self.assertEqual(w.x,1)
        self.assertEqual(w.y,2)
        self.assertEqual(w.z,3)
        self.assertEqual(w.a,4)
        print("test4d passed")
    
    def testNextIsWalk(self):
        w = walk(1,2,3,4 ,walk(1,2,3,4,None))
        self.assertIsInstance(w.next,walk)
        self.assertNotIsInstance(w.next.next,walk)
        print("test next is Walk passed")

    def testmovex(self):
        w= walk(1,None,None,None,None)
        self.assertEqual(w.x,1)
        w.movex(1)
        self.assertEqual(w.x,2)
        w.movex(-4)
        self.assertEqual(w.x,-2)
        print("testmovex passed")
    
    def testaddstep(self):
        w= walk(1,None,None,None,None)
        self.assertIsNone(w.next)
        w.movex(1)
        self.assertIsNotNone(w.next)
        print("testaddStep passed")

        


if __name__ == '__main__':
    unittest.main()