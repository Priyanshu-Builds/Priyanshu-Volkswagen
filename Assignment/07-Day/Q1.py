from abc import ABC, abstractmethod

class ReportTemplate(ABC):

    def generate_report(self):
        self.parse_data()
        self.validate_data()
        if self.needs_revalidation():
            self.revalidate_data()
        self.save_report()

    def parse_data(self):
        print("Parsing data for the report...")

    def validate_data(self):
        print("Validating data before generating report...")

    def revalidate_data(self):
        print("Revalidating data for special report...")

    @abstractmethod
    def save_report(self):
        pass

    def needs_revalidation(self):
        return False


class PDFReport(ReportTemplate):
    def save_report(self):
        print("Report saved as PDF file.")


class DOCXReport(ReportTemplate):
    def save_report(self):
        print("Report saved as DOCX file.")


class TXTReport(ReportTemplate):
    def save_report(self):
        print("Report saved as TXT file.")


class CSVReport(ReportTemplate):
    def needs_revalidation(self):
        return True

    def save_report(self):
        print("Report saved as CSV file.")


class JSONReport(ReportTemplate):
    def needs_revalidation(self):
        return True

    def save_report(self):
        print("Report saved as JSON file.")


def main():
    print("Welcome to Report Generator")
    print("1. PDF")
    print("2. DOCX")
    print("3. TXT")
    print("4. CSV")
    print("5. JSON")

    choice = input("Choose report type: ")

    if choice == "1":
        report = PDFReport()
    elif choice == "2":
        report = DOCXReport()
    elif choice == "3":
        report = TXTReport()
    elif choice == "4":
        report = CSVReport()
    elif choice == "5":
        report = JSONReport()
    else:
        print("Invalid choice")
        return

    print("\nGenerating report...")
    report.generate_report()


if __name__ == "__main__":
    main()