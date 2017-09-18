#!/usr/bin/python

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None #initialise next as NULL

class linkedList:
    def __init__(self):
        self.head=None
        self.count=0

    #push an element in the beginning
    def push(self, new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        self.count += 1

    #push an element in the end 
    def append(self, data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.count += 1
            return
        ptr=self.head
        while(ptr.next):
            ptr=ptr.next
        ptr.next=new_node
        self.count += 1

    #delete element by position 
    def deleteByPosition(self, position):
        pos=self.head
        if position > self.count or position <= 0:
            print "Invalid position"
            return
        if self.count==1 and position==1:
            self.head=None
            self.count -= 1
            return

        if position==1:
            self.head=self.head.next
        else:
            for count in range(1, position-1):
                pos=pos.next
            if position==self.count:
                pos.next=None
            else:
                pos.next=pos.next.next
        self.count -= 1

    #print the List 
    def printList(self):
        ptr=self.head
        print "List:",
        if self.count==0:
            print "Empty List"
            return
        while(ptr):
            print "%d "% ptr.data,
            ptr=ptr.next
        print ""

if __name__=='__main__':
    lst=linkedList()
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.printList()
    lst.deleteByPosition(3)
    lst.printList()
