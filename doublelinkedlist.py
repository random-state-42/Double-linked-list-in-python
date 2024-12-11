class Node:
    def __init__(self,value):
        self.next = None
        self.prev=None
        self.value = value
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end="")
            if temp.next is not None:
                print(" -> ",end="")
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.tail
            self.tail = None
            self.head = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None 
        self.length -= 1
        return temp
    

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1 :
            return self.pop()
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1 
        return temp
    
    def get(self,index):
        if index >= self.length or index < 0:
            return None
        if index < self.length/2:
            temp = self.head
            while index != 0:
                temp = temp.next
                index -= 1
        else:
            index = self.length - index -1
            temp  = self.tail
            while index != 0:
                temp = temp.prev
                index -= 1
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index > self.length or index <0:
            return False
        elif index == 0 :
            return self.prepend(value)
        elif (index) == self.length:
            return self.append(value)
        else:
            temp = self.get(index-1)
            temp2 = temp.next
            new_node = Node(value)
            new_node.prev = temp
            new_node.next = temp2
            temp.next = new_node
            temp2.prev = new_node
            return True
        
    def remove(self,index):
        if index > self.length or index < 0:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp
        


dll = DoublyLinkedList()

while True:
    
    print("""
          1.insert element at first: 
          2.insert element at last:
          3.insert element at specific place:
          4.remove element at last: 
          5.remove element at first:
          6.remove a specific element:
          7.fetch an element at a index:
          8.print the list:
          9.change value at a index:
          10.quit
          """)
    uip = input("Enter Your choice: ")
    match int(uip):
        case 1:
            dll.prepend(int(input("Enter a number: ")))
        case 2:
            dll.append(int(input("Enter a number: ")))
        case 3:
            index = int(input("Enter the index: "))
            num = int(input("Enter the number: "))
            dll.insert(index,num)
        case 4:
            ele = dll.pop()
            if ele is None:
                print("No element at last: ")
            else:
                print("removed element is : ", ele.value)
        case 5:
            ele = dll.pop_first()
            if ele is None:
                print("No element at first: ")
            else: 
                print("removed element is : ", ele.value)
        case 6:
            ele = dll.remove(int(input("Enter the index to remove an element: ")))
            if ele is None:
                print("No element at the given index: ")
            else:
                print("removed element is : ", ele.value)
        case 7:
            index = int(input("Enter the index to get an element: "))
            print("element is : ", dll.get(index).value," at index: ",index)
        case 8:
            dll.print_list()
        case 9:
            index = int(input("Enter the index: "))
            num = int(input("Enter the new number: "))
            dll.set_value(index,num)
        case 10:
            break
        case _:
            print("Invalid option")


            



            




