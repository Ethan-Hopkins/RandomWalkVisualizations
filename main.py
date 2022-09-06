
from random import randint, random, randrange
#from graphics import *

class walkNode:
    def __init__(self,next=None, x=0,y=0,z=0,a=0 ):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.next = next
    

def appendNode(head,x=0,y=0,z=0,a=0):
    newHead = walkNode(head,x,y,z,a)
    head = newHead
    return head

def walk(head,x=0,y=0,z=0,a=0):
    return appendNode(head,head.x+x,head.y+y,head.z+z,head.a+a)

def printList(head):
    print(head.x,head.y,head.z,head.a)
    while head.next:
        head = head.next
        print(head.x,head.y,head.z,head.a)

def oneDWalk(head,length):
    for b in range(length):
        step=-1
        if(randint(0,1)==1): step = 1
        head = walk(head, step)
    return head

def twoDWalk(head,length):
    for b in range(length):
        step=-1
        if(randint(0,1)==1): step = 1
        if(randint(0,1)==1): head = walk(head,0,step)
        else: head = walk(head,step)
    return head
def threeDWalk(head,length):
    for b in range(length):
        step=-1
        if(randint(0,1)==1): step = 1
        direction = randint(0,2)
        if(direction ==2): head = walk(head,0,0,step)
        elif(direction ==1): head = walk(head,0,step)
        else: head = walk(head,step)
    return head

def fourDWalk(head,length):
    for b in range(length):
        step=-1
        if(randint(0,1)==1): step = 1
        direction = randint(0,3)
        if(direction==3):head = walk(head,0,0,0,step)
        elif(direction ==2): head = walk(head,0,0,step)
        elif(direction ==1): head = walk(head,0,step)
        else: head = walk(head,step)
    return head

def main():
    # what should I store the walk as? I could have it as a linked list or an array
    head = walkNode(None,0)
    head = fourDWalk(head,20000)
    printList(head)
    print(head.x,head.y,head.z,head.a)
    """
    #for i in range(10000):
        head = walkNode(None,0)
        end = oneDWalk(head,20).x
        count+=end
        if end<=smallest: smallest = end
        if end>largest:largest =end
    print(count,largest,smallest)
    """


if __name__ == "__main__":
    main()