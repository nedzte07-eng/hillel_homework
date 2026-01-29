class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"Manager is {self.name}, salary is {self.salary}, department is {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language=None):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f"Developer is {self.name}, salary is {self.salary}, programming language is {self.programming_language}"

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        Developer.__init__(self, name, salary)
        self.team_size = team_size

    def __str__(self):
        return f"Team lead is {self.name}, salary is {self.salary}, department is {self.department} and size of team is {self.team_size}"


masha = TeamLead("Masha", 2000, "HR", 5)
sasha = Developer("Sasha", 2500, "Python")
dasha = Manager("Dasha", 3000, "PR")

print(masha)
print(sasha)
print(dasha)
print(TeamLead.mro())