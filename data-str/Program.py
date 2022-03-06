from asyncio import new_event_loop


class Node:
    def __init__(self,data,next = None , prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DLL:
    def __init__(self):
        self.head = None
     
    def apppend(self,new_data):
        last = self.head
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        while(last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
             
    def push(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.apppend(new_data)
            return
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
            return
    def AfterNode(self ,data , prev_data):
        if prev_data == None:
            print('Provide the previous Node data')
            return
        temp = self.head
        new_node = Node(data)
        while temp:
            if temp.data == prev_data:
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp
                break
            temp = temp.next
            
    def printDLL(self):
        temp = self.head
        if self.head == None:
            print('Empty List')
            return
        while temp is not None:
            print(temp.data)
            temp = temp.next


dll = DLL()
dll.apppend(12)
dll.apppend(34)
dll.apppend(123)
dll.push(11)
dll.AfterNode(1000,34)
dll.printDLL() 
             
