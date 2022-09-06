
class walk:
    def __init__(self,x=0, y=0, z=0, a=0, next=None):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.next = next
    
    def move(self,mvX=0,mvY=0,mvZ=0,mvA=0):
        self.next = self
        self.x +=mvX
        self.y +=mvY
        self.z +=mvZ
        self.a +=mvA
        

def main():
    # what should I store the walk as? I could have it as a linked list or an array
    w = walk(0,None,None,None)


if __name__ == "__main__":
    main()