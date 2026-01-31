class LL:

    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None

    def __init__(self):
        self.start = None

    def insertBeg(self, v):
        newNode = self.Node(v)

        if self.start is None:
            self.start = newNode
            newNode.next = self.start
            return

        tptr = self.start
        while tptr.next != self.start:
            tptr = tptr.next

        newNode.next = self.start
        tptr.next = newNode
        self.start = newNode

    def insertEnd(self, v):
        newNode = self.Node(v)

        if self.start is None:
            self.start = newNode
            newNode.next = self.start
            return

        tptr = self.start
        while tptr.next != self.start:
            tptr = tptr.next

        tptr.next = newNode
        newNode.next = self.start

    def count_of_node(self):
        if self.start is None:
            return 0

        c = 0
        tptr = self.start
        while True:
            c += 1
            tptr = tptr.next
            if tptr == self.start:
                break
        return c

    def insertAtPos(self, v, p):
        if p == 1:
            self.insertBeg(v)
            return

        size = self.count_of_node()
        if p < 1 or p > size + 1:
            print("Invalid Position")
            return

        newNode = self.Node(v)
        tptr = self.start

        for _ in range(1, p - 1):
            tptr = tptr.next

        newNode.next = tptr.next
        tptr.next = newNode

    def deleteBeg(self):
        if self.start is None:
            print("List is empty")
            return

        if self.start.next == self.start:
            self.start = None
            print("Last node deleted")
            return

        tptr = self.start
        while tptr.next != self.start:
            tptr = tptr.next

        self.start = self.start.next
        tptr.next = self.start

    def deleteEnd(self):
        if self.start is None:
            print("List is empty")
            return

        if self.start.next == self.start:
            self.start = None
            print("Last node deleted")
            return

        tptr = self.start
        while tptr.next.next != self.start:
            tptr = tptr.next

        tptr.next = self.start

    def DeleteAtPos(self, p):
        if self.start is None:
            print("List is empty")
            return

        if p == 1:
            self.deleteBeg()
            return

        size = self.count_of_node()
        if p < 1 or p > size:
            print("Invalid Position")
            return

        tptr = self.start
        for _ in range(1, p - 1):
            tptr = tptr.next

        tptr.next = tptr.next.next

    def search(self, s):
        if self.start is None:
            return -1

        tptr = self.start
        pos = 0
        while True:
            pos += 1
            if tptr.data == s:
                return pos
            tptr = tptr.next
            if tptr == self.start:
                break
        return -1

    def Display(self):
        if self.start is None:
            print("List is empty")
            return

        tptr = self.start
        while True:
            print(f"{tptr.data} -> ", end="")
            tptr = tptr.next
            if tptr == self.start:
                break
        print("(back to start)")



# ================= MAIN MENU =================

list1 = LL()

while True:
    print("\n===== Circular Linked List Menu =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Position")
    print("7. Search")
    print("8. Display")
    print("9. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            v = int(input("Enter value: "))
            list1.insertBeg(v)

        case 2:
            v = int(input("Enter value: "))
            list1.insertEnd(v)

        case 3:
            v = int(input("Enter value: "))
            p = int(input("Enter position: "))
            list1.insertAtPos(v, p)

        case 4:
            list1.deleteBeg()

        case 5:
            list1.deleteEnd()

        case 6:
            p = int(input("Enter position: "))
            list1.DeleteAtPos(p)

        case 7:
            v = int(input("Enter value to search: "))
            pos = list1.search(v)
            if pos == -1:
                print("Value not found")
            else:
                print("Found at position:", pos)

        case 8:
            list1.Display()

        case 9:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice")
