class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def _financial_report(self):
        print("Confidential Financial Report: Revenue is growing great!!")

    def show_details(self):
        print("Company:", self.name)
        print("Location:", self.location)


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def _policy_update(self):
        print("Confidential: Company policies updated, follow the new policies.")

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.emp_name)
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


class Manager(NewEmployee, Company):
    def access_financials(self):
        print("\nManager accessing financial report:")
        self._financial_report()


class HR(NewEmployee):
    def access_policy(self):
        print("\nHR accessing policy update:")
        self._policy_update()


class Developer(NewEmployee):
    pass


class Intern(NewEmployee):
    pass


class ManagerHR(Manager, HR):
    def access_all_confidential(self):
        print("\nManagerHR accessing both confidential features:")
        self._financial_report()
        self._policy_update()


class DeveloperIntern(Developer, Intern):
    pass


def main():

    m1 = Manager(1, "Anand", "Project Manager", "01-01-2024", "ABC")
    h1 = HR(2, "Sam", "HR Executive", "01-02-2026", "Volkswagen")
    d1 = Developer(3, "Priyanshu", "Software Developer", "21-11-2025", "VIT")
    i1 = Intern(4, "Piyush", "Intern", "15-01-2026", "Startup")

    employees = [m1, h1, d1, i1]

    company = CompanyAcquisition("Polo", "Pune", employees)

    print("\n>>>>>>>>>>>>>------------------Company After Acquisition------------------<<<<<<<<<<<<<<<")
    company.show_details()

    print(">>>>>>>>>>>>>>--------------------Access Control Demo--------------------<<<<<<<<<<<<<<<<")
    m1.access_financials()
    h1.access_policy()

    mh = ManagerHR(5, "Riya", "ManagerHR", "01-05-2024", "Volkswagen")
    mh.access_all_confidential()


if __name__ == "__main__":
    main()