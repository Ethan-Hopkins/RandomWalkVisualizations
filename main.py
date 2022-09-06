
class walk:
    def __init__(self,x, y, z, a, next):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.next = next
    
    def movex(self,mv):
        self.next = walk(self.x,self.y,self.z,self.a,None)
        self.x +=mv
        

def main():
    # what should I store the walk as? I could have it as a linked list or an array
    w = walk(0,None,None,None)


if __name__ == "__main__":
    main()