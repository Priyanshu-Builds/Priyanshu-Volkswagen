import time

def log_and_time(func):
    def wrapper(*args, **kwargs):
        print("Starting report generation...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Report generated successfully.")
        print("Time taken:", round(end - start, 2), "seconds")
        return result
    return wrapper


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        print("File opened successfully.")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed safely.")


class ReportGenerator:

    def generate_data(self):
        for i in range(1, 6):
            yield f"Report line {i}\n"


class TextReport(ReportGenerator):

    @log_and_time
    def create_report(self):
        with FileManager("text_report.txt") as file:
            for line in self.generate_data():
                print("Writing:", line.strip())
                file.write(line)


class StructuredReport(ReportGenerator):

    @log_and_time
    def create_report(self):
        with FileManager("structured_report.txt") as file:
            for line in self.generate_data():
                formatted = f'{{ "data": "{line.strip()}" }}\n'
                print("Writing:", formatted.strip())
                file.write(formatted)


def main():
    print("Choose report type")
    print("1. Text Report")
    print("2. Structured Report")

    choice = input("Enter choice: ")

    if choice == "1":
        report = TextReport()
    elif choice == "2":
        report = StructuredReport()
    else:
        print("Invalid choice")
        return

    report.create_report()


if __name__ == "__main__":
    main()