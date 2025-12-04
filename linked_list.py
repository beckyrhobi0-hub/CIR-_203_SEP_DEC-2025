
class Node:
    def __init__(self, name, admission_no, grades):
        self.data = {
            "name": name,
            "admission_no": admission_no,
            "grades": grades    
        }
        self.next = None



class StudentLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, name, admission_no, grades):
        new_node = Node(name, admission_no, grades)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return

        while current:
            print("Name:", current.data["name"])
            print("Admission No:", current.data["admission_no"])
            print("Grades:", current.data["grades"])
            print("-----")
            current = current.next


students = StudentLinkedList()

students.insert("John Doe", "ADM2025/001", [78, 82, 90])
students.insert("Mary Wanjiku", "ADM2025/002", [85, 79, 92])
students.insert("Kevin Otieno", "ADM2025/003", [66, 71, 80])

print("All Students:")
students.display()

