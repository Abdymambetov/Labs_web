class Student:
    def __init__(self, name, age, student_id):
        self.__name = name
        self.__age = age
        self.__student_id = student_id

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_student_id(self):
        return self.__student_id

    # отображение информации о студенте
    def display_info(self):
        print(f"Имя: {self.__name}, Возраст: {self.__age}, ID: {self.__student_id}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Студент {student.get_name()} добавлен.")

    def remove_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print(f"Студент с ID {student_id} удален.")
        else:
            print(f"Студент с ID {student_id} не найден.")

    
    def find_student(self, student_id):
        for student in self.students:
            if student.get_student_id() == student_id:
                return student
        return None

    
    def display_all_students(self):
        if not self.students:
            print("Список студентов пуст.")
        else:
            print("Список всех студентов:")
            for index, student in enumerate(self.students, start=1):
                print(f"{index}. {student.get_name()}, {student.get_age()} лет, ID: {student.get_student_id()}")

def main():
    manager = StudentManager()

    while True:
        command = input("Введите команду (add, remove, find, display, exit): ").strip().lower()

        if command == "add":
            name = input("Введите имя студента: ").strip()
            age = input("Введите возраст: ").strip()
            student_id = input("Введите номер студенческого билета: ").strip()
            new_student = Student(name, age, student_id)
            manager.add_student(new_student)

        elif command == "remove":
            student_id = input("Введите номер студенческого билета для удаления: ").strip()
            manager.remove_student(student_id)

        elif command == "find":
            student_id = input("Введите номер студенческого билета для поиска: ").strip()
            student = manager.find_student(student_id)
            if student:
                student.display_info()
            else:
                print(f"Студент с ID {student_id} не найден.")

        elif command == "display":
            manager.display_all_students()

        elif command == "exit":
            print("Выход из программы.")
            break

        else:
            print("Неверная команда, попробуйте снова.")

if __name__ == "__main__":
    main()
