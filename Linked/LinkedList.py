from Linked.Node import Node


class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        currentNode = self.head
        newNode = Node(data)
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = newNode

    def insertBegening(self, data):
        current_node = self.head
        newNode = Node(data)
        if newNode is not self.head:
            self.head=newNode
            newNode.nextNode = current_node

    def display(self):
        element = []
        currentNode = self.head
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
            element.append(currentNode.data)
        print(element)

    def elements(self):
        self.counter = 0
        currentNode = self.head
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
            self.counter += 1
        print("Number of elements are", self.counter)

    def length(self):
        self.counter = 0
        currentNode = self.head
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
            self.counter += 1
        return self.counter

    def get(self, index):
        if index >= self.length():
            print("Out of range")
        else:
            current_index = 0
            currentNode = self.head
            while True:
                currentNode = currentNode.nextNode
                if current_index == index:
                    return currentNode.data
                current_index += 1

    def delete(self, data):
        currentNode = self.head
        while currentNode.nextNode is not None:
            previousnode = currentNode
            currentNode = currentNode.nextNode
            if (currentNode.data == data):
                previousnode.nextNode = currentNode.nextNode
                print("Element", currentNode.data, "deleted")
                break
        else:
            print("Not found")

    def insert_middle(self, index, data):
        counter = 0
        newNode = Node(data)
        current_node = self.head
        while current_node.nextNode is not None:
            previousnode = current_node
            current_node = current_node.nextNode
            counter += 1
            if (counter - 1 == index):
                previousnode.nextNode = newNode
                newNode.nextNode = current_node
                break
        else:
            print("Index not found")
