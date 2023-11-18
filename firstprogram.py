class VirtualClassroomManager:
    def __init__(s):
        s.classrooms = {}
        s.students = {}
        s.assignments = {}

    def add_classroom(s, class_name):
        s.classrooms[class_name] = []
        print(f"Classroom {class_name} has been created.")

    def list_classrooms(s):
        print("Classrooms:")
        for class_name in s.classrooms:
            print(f"- {class_name}")

    def remove_classroom(s, class_name):
        if class_name in s.classrooms:
            del s.classrooms[class_name]
            print(f"Classroom {class_name} has been removed.")
        else:
            print(f"Classroom {class_name} not found.")

    def add_student(s, student_id, class_name):
        if class_name in s.classrooms:
            s.students[student_id] = class_name
            s.classrooms[class_name].append(student_id)
            print(f"Student {student_id} has been enrolled in {class_name}.")
        else:
            print(f"Classroom {class_name} not found.")

    def list_students(s, class_name):
        if class_name in s.classrooms:
            print(f"Students in {class_name}:")
            for student_id in s.classrooms[class_name]:
                print(f"- {student_id}")
        else:
            print(f"Classroom {class_name} not found.")

    def schedule_assignment(s, class_name, assignment_details):
        if class_name in s.classrooms:
            s.assignments[class_name] = assignment_details
            print(f"Assignment for {class_name} has been scheduled.")
        else:
            print(f"Classroom {class_name} not found.")

    def submit_assignment(s, student_id, class_name):
        if student_id in s.students and s.students[student_id] == class_name:
            print(f"Assignment submitted by Student {student_id} in {class_name}.")
        else:
            print(f"Student {student_id} not enrolled in {class_name}.")

# Example Usage
manager = VirtualClassroomManager()

manager.add_classroom("19ECE345")
manager.add_student("Rahul", "19ECE345")
manager.list_students("19ECE345")

manager.schedule_assignment("19ECE345", "Assignment 1")
manager.submit_assignment("Rahul", "19ECE345")

manager.list_classrooms()
