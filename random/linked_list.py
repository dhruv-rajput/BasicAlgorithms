class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class LL:
    def __init__(self):
        self.head = None
    def printl(self):
        temp = self.head
        while(temp):
          print(temp.data)
          temp=temp.next
    def inserti(self , pev , newdata):
        new = node(newdata)
        new.next = pev.next
        pev.next = new      

llist = LL()
llist.head = node(1)
second=node(2)
llist.head.next = second
third = node(4)
second.next = third
llist.inserti(llist.head.next,3)
llist.printl()



