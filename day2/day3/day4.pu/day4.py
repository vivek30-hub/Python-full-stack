# class student:
#     def display(self):
#         print("AIDS are bad students")
# s1=student()
# s1.display()


# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# s1 = student("Vivek", 20)
# s1.display()





# class employee:
#     def __init__(self, name,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.department = def department(self):

#     def dislay(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Salary:", self.salary)
#         print("Department:", self.department)

# e1 = employee("Vivek", 20, 50000, "IT")
# e2 = employee("dileep", 20, 60000, "HR")
# e1.display()
# e2.display()



# ============================================================
# 1. SINGLE INHERITANCE (one parent -> one child)
# ============================================================
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


# ============================================================
# 2. MULTILEVEL INHERITANCE (chain: Grandparent -> Parent -> Child)
# ============================================================
class Person:
    def __init__(self, name):
        self.name = name

    def show_person(self):
        print(f"Person: {self.name}")


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def show_employee(self):
        self.show_person()
        print(f"Employee ID: {self.emp_id}")


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_manager(self):
        self.show_employee()
        print(f"Department: {self.department}")


# ============================================================
# 3. MULTIPLE INHERITANCE (child inherits from 2+ parents)
# ============================================================
class Father:
    def skills_father(self):
        print("Father: Cooking, Gardening")


class Mother:
    def skills_mother(self):
        print("Mother: Painting, Music")


class Child(Father, Mother):
    def skills_child(self):
        print("Child: Coding")


# ============================================================
# 4. HIERARCHICAL INHERITANCE (one parent -> multiple children)
# ============================================================
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving")


class Bike(Vehicle):
    def ride(self):
        print(f"{self.brand} bike is riding")


# ============================================================
# 5. HYBRID INHERITANCE (combination of two or more types above)
#    Here: Hierarchical + Multiple
# ============================================================
class Base:
    def show_base(self):
        print("Base class method")


class Branch1(Base):        # Hierarchical
    def show_branch1(self):
        print("Branch1 class method")


class Branch2(Base):        # Hierarchical
    def show_branch2(self):
        print("Branch2 class method")


class Hybrid(Branch1, Branch2):   # Multiple + Hierarchical = Hybrid
    def show_hybrid(self):
        print("Hybrid class method")


# ============================================================
# TESTING ALL TYPES
# ============================================================
if __name__ == "__main__":

    print("---- 1. Single Inheritance ----")
    d = Dog("Buddy")
    d.eat()
    d.bark()

    print("\n---- 2. Multilevel Inheritance ----")
    mgr = Manager("Ravi Kumar", "EMP101", "Engineering")
    mgr.show_manager()

    print("\n---- 3. Multiple Inheritance ----")
    c = Child()
    c.skills_father()
    c.skills_mother()
    c.skills_child()

    print("\n---- 4. Hierarchical Inheritance ----")
    car = Car("Toyota")
    bike = Bike("Yamaha")
    car.show_brand()
    car.drive()
    bike.show_brand()
    bike.ride()

    print("\n---- 5. Hybrid Inheritance ----")
    h = Hybrid()
    h.show_base()
    h.show_branch1()
    h.show_branch2()
    h.show_hybrid()
    print("MRO:", [cls.__name__ for cls in Hybrid.__mro__])