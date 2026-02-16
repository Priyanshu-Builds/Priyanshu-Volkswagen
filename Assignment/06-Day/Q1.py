class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print("Company Name:", self.name)
        print("Location:", self.location)


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Designation:", self.designation)


class CompanyAcquisition(Company):
    def __init__(self, name, location, employees):
        super().__init__(name, location)
        self.employees = employees

    def show_details(self):
        super().show_details()
        print("\nEmployees after acquisition:")
        for emp in self.employees:
            print("-", emp.emp_name, "(", emp.designation, ")")


class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print("Joining Date:", self.joining_date)
        print("Previous Company:", self.previous_company)


class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, team_size):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size

    def show_details(self):
        super().show_details()
        print("Team Size:", self.team_size)


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.policies_handled = policies_handled

    def show_details(self):
        super().show_details()
        print("Policies Handled:", self.policies_handled)


class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, languages):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.languages = languages

    def show_details(self):
        super().show_details()
        print("Programming Languages:", self.languages)


class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company, duration):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.duration = duration

    def show_details(self):
        super().show_details()
        print("Intern Duration:", self.duration)

class ManagerHR(Manager, HR):
    pass

class DeveloperIntern(Developer, Intern):
    pass


def main():

    emp1 = Manager(1, "Anand", "Project Manager", "01-01-2024", "ABC", 109)
    emp2 = HR(2, "Sam", "HR Executive", "01-02-2026", "Volkswagen", "Company Policies")
    emp3 = Developer(3, "Priyanshu", "Software Developer", "21-11-2025", "VIT", ["Python", "Java"])
    emp4 = Intern(4, "Piyush", "Intern", "15-01-2026", "Startup", "6 Months")

    employees = [emp1, emp2, emp3, emp4]

    company = CompanyAcquisition("Skoda", "Pune", employees)
    
    print("\n>>>>>>>>>>>>>------------------Company After Acquisition------------------<<<<<<<<<<<<<<<")
    company.show_details()

    print("\n>>>>>>>>>>>>>------------------Individual Employee Details------------------<<<<<<<<<<<<<<<")
    for emp in employees:
        print("\n---------------------")
        emp.show_details()


if __name__ == "__main__":
    main()