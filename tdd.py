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
        w= walk(1)
        self.assertEqual(w.x,1)
        w.move(1)
        self.assertEqual(w.x,2)
        w.move(-4)
        self.assertEqual(w.x,-2)
        print("testmovex passed")

    def testmovey(self):
        w= walk(0,1)
        self.assertEqual(w.y,1)
        w.move(0,1)
        self.assertEqual(w.y,2)
        w.move(0,-4)
        self.assertEqual(w.y,-2)
        print("testmovey passed")

    def testmovez(self):
        w= walk(0,0,1)
        self.assertEqual(w.z,1)
        w.move(0,0,1)
        self.assertEqual(w.z,2)
        w.move(0,0,-4)
        self.assertEqual(w.z,-2)
        print("testmovez passed")

    def testmovea(self):
        w= walk(0,0,0,1)
        self.assertEqual(w.a,1)
        w.move(0,0,0,1)
        self.assertEqual(w.a,2)
        w.move(0,0,0,-4)
        self.assertEqual(w.a,-2)
        print("testmovea passed")

    def testmoveAll(self):
        w= walk(1,1,1,1)
        self.assertEqual(w.x,1)
        self.assertEqual(w.y,1)
        self.assertEqual(w.z,1)
        self.assertEqual(w.a,1)
        w.move(1,1,1,1)
        self.assertEqual(w.x,2)
        self.assertEqual(w.y,2)
        self.assertEqual(w.z,2)
        self.assertEqual(w.a,2)
        w.move(-4,-4,-4,-3)
        self.assertEqual(w.x,-2)
        self.assertEqual(w.y,-2)
        self.assertEqual(w.z,-2)
        self.assertEqual(w.a,-1)
        print("testmoveall passed")
    
    def testaddstep(self):
        w= walk(1)
        self.assertIsNone(w.next)
        w.move(1)
        self.assertIsNotNone(w.next)
        print("testaddStep passed")

    def testChain(self):
        w = walk(1)
        self.assertIsNone(w.next)
        w.move(1)
        w.move(1)
        w.move(1)
        w.move(1)
        w.move(1)
        for i in range(5):
            print(w.next)
            self.assertIsNotNone(w.next)
            w = w.next
        self.assertIsNone(w.next)
        print("testchain passed")

        


if __name__ == '__main__':
    unittest.main()