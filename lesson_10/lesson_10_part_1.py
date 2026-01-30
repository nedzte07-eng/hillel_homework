class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

    def __str__(self):
        return f"Manager is {self.name}, salary is {self.salary}, department is {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f"Developer is {self.name}, salary is {self.salary}, programming language is {self.programming_language}"

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, programming_language, department, team_size):
        # super().__init__(name, salary, department, programming_language)
        # Developer.__init__(self, name, salary)
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def __str__(self):
        return f"Team lead is {self.name}, salary is {self.salary}, department is {self.department} and size of team is {self.team_size}"


masha = TeamLead("Masha", 2000, "JavaScript", "HR", 5)
# sasha = Developer("Sasha", 2500, "Python")
# dasha = Manager("Dasha", 3000, "PR")

def assert_with_message (class_argument_name, class_argument_value):
    assert class_argument_name == class_argument_value
    return print(f'{class_argument_name} - verified')

def test_name_in_classes():
    print('Starting our test')
    assert_with_message(masha.name, 'Masha')
    assert_with_message(masha.salary, 2000)
    assert_with_message(masha.programming_language, 'JavaScript')
    assert_with_message(masha.department, 'HR')
    assert_with_message(masha.team_size, 5)

    # print('-' * 80)
    #
    # assert_with_message(sasha.name, 'Sasha')
    # assert_with_message(sasha.salary, 2500)
    # assert_with_message(sasha.programming_language, 'Python')
    #
    # print('-' * 80)
    #
    # assert_with_message(dasha.name, 'Dasha')
    # assert_with_message(dasha.salary, 3000)
    # assert_with_message(dasha.department, 'PR')

    print('Ending our test')
# print(TeamLead.mro())
test_name_in_classes()
print(TeamLead.mro())
