class Report:
    templates = {}

    def __init__(self, title, data):
        self.title = title
        self.data = data

    # Magic method
    def __str__(self):
        return f"Report: {self.title}"

    # Class method
    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    # Decorator
    @staticmethod
    def format_report(func):
        def wrapper(self):
            print("=" * 40)
            func(self)
            print("=" * 40)
        return wrapper

    @format_report
    def generate(self):
        template = self.templates.get("simple", "{}")
        print(template.format(self.title))
        for item in self.data:
            print(item)


# Define a report template
Report.add_template("simple", "REPORT: {}")

# Create a report
data = ["Sales: ₹50,000", "Profit: ₹15,000", "Employees: 10"]

report = Report("Monthly Sales", data)

# Generate report
print(report)
report.generate()
