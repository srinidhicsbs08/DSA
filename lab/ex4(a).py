# Class created for node creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class to perform LL operations
class LL:
    def __init__(self):
        self.head = None  

    # Function to display the linked list
    def display(self):
        temp = self.head
        if self.head is None:  # if head is none it means list is empty
            print("List is Empty")
            return
        while temp:
            print(temp.data, "--->", end=" ")
            temp = temp.next
        print()

    # Function to Insert node at the beginning of the LL
    def insert_beginning(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb  

    # Function to Insert node at the end of the LL
    def insert_end(self, data):
        ne = Node(data)
        if self.head is None:
            self.head = ne
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne 

    # Function to Insert node at a given position
    def insert_position(self, pos, data):
        np = Node(data)  # create new node
        if pos == 0:  # insert at beginning
            np.next = self.head
            self.head = np
            return
        temp = self.head
        for i in range(pos - 1):  # loop till the specified position-1
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        np.next = temp.next
        temp.next = np  

    # Function to Delete node at the beginning of the LL
    def delete_beginning(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        self.head = temp.next
        temp.next = None  

    # Function to delete node at the end of the LL
    def delete_end(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            self.head = None
            return
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None

    # Function to delete node at a given position
    def delete_position(self, pos):
        if self.head is None:
            print("List is Empty")
            return
        if pos == 0:
            self.head = self.head.next
            return
        prev = self.head
        temp = self.head.next
        for i in range(pos - 1):
            if temp is None:
                print("Position out of range")
                return
            prev = temp
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        prev.next = temp.next

# Object created for LL class
obj = LL()

# node 1 created with data 10
n1 = Node(10)
obj.head = n1 

# node 2 created with data 20
n2 = Node(20)
n1.next = n2 

# node 3 with data 30
n3 = Node(30)
n2.next = n3  

# display the linked list created
print("DISPLAY THE CREATED LIST ..... ")
obj.display()  

# Insertion of data 5 at the beginning of the list
obj.insert_beginning(5)
print("AFTER INSERTING 5 AT THE BEGINNING.... ")
obj.display()  

# Insert 40 at the end of the list
obj.insert_end(40)
print("INSERTING 40 AT THE END OF THE LIST")
obj.display()

# Insert 25 at position 3
obj.insert_position(3, 25)
print("INSERTING 25 AT THE MIDDLE OF THE LIST")
obj.display()

# Delete beginning
obj.delete_beginning()
print("AFTER DELETING THE FIRST NODE 5 FROM THE LIST...")
obj.display()

# Delete end
obj.delete_end()
print("AFTER DELETING THE LAST NODE 40 FROM THE LIST...")
obj.display()

# Delete position
obj.delete_position(2)
print("AFTER DELETING MIDDLE NODE 25 FROM THE LIST...")
obj.display()

