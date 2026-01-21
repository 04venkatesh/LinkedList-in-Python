class DLL:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.start = None

    def InsertBegin(self, data):
        newNode = self.Node(data)
        if self.start is not None:
            self.start.prev = newNode
            newNode.next = self.start
        self.start = newNode

    def InsertEnd(self, data):
        newNode = self.Node(data)
        if self.start is None:
            self.start = newNode
            return

        pointer = self.start
        while pointer.next is not None:
            pointer = pointer.next

        pointer.next = newNode
        newNode.prev = pointer

    def Display(self):
        pointer = self.start
        while pointer is not None:
            if pointer.next is not None:
                print(f"{pointer.data}<->", end="")
            else:
                print(pointer.data, end="")
            pointer = pointer.next

    def DelBegin(self):
        if self.start is None:
            print("List is empty")
            return

        if self.start.next is None:
            self.start = None
            return

        self.start = self.start.next
        self.start.prev = None

    def DelEnd(self):
        if self.start is None:
            print("List is empty")
            return

        if self.start.next is None:
            self.start = None
            return

        pointer = self.start
        while pointer.next is not None:
            pointer = pointer.next

        pointer.prev.next = None

    def Count(self):
        c = 0
        pointer = self.start
        while pointer is not None:
            c += 1
            pointer = pointer.next
        return c

    def InsertPos(self, pos, data):
        size = self.Count()
        if pos < 1 or pos > size + 1:
            print("Invalid Position")
            return

        if pos == 1:
            self.InsertBegin(data)
            return

        newNode = self.Node(data)
        pointer = self.start
        for _ in range(1, pos - 1):
            pointer = pointer.next

        newNode.next = pointer.next
        newNode.prev = pointer
        if pointer.next is not None:
            pointer.next.prev = newNode
        pointer.next = newNode

    def DelPos(self, pos):
        size = self.Count()
        if pos < 1 or pos > size:
            print("Invalid Position")
            return

        if pos == 1:
            self.DelBegin()
            return

        pointer = self.start
        for _ in range(1, pos):
            pointer = pointer.next

        if pointer.next is not None:
            pointer.next.prev = pointer.prev
        pointer.prev.next = pointer.next

    def Search(self, data):
        pointer = self.start
        position = 1
        while pointer is not None:
            if pointer.data == data:
                return position
            pointer = pointer.next
            position += 1
        return -1


# -------- MENU --------
dll = DLL()

while True:
    print("\n1.Insert Begin  \n2.Insert End  \n3.Insert Position",end="")
    print("\n4.Delete Begin  \n5.Delete End  \n6.Delete Position",end="")
    print("\n7.Search        \n8.Display     \n9.Count")
    print("0.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        dll.InsertBegin(int(input("Enter data: ")))
    elif choice == 2:
        dll.InsertEnd(int(input("Enter data: ")))
    elif choice == 3:
        pos = int(input("Enter position: "))
        data = int(input("Enter data: "))
        dll.InsertPos(pos, data)
    elif choice == 4:
        dll.DelBegin()
    elif choice == 5:
        dll.DelEnd()
    elif choice == 6:
        dll.DelPos(int(input("Enter position: ")))
    elif choice == 7:
        data = int(input("Enter value to search: "))
        print("Position:", dll.Search(data))
    elif choice == 8:
        dll.Display()
    elif choice == 9:
        print("Count:", dll.Count())
    elif choice == 0:
        break
    else:
        print("Invalid choice")
