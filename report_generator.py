import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# Read CSV file
def read_data(file_name):
    data = pd.read_csv(file_name)
    return data


# Analyze data
def analyze_data(data):
    summary = data.describe()
    return summary


# Generate PDF report
def generate_pdf(summary, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica", 12)

    # Title
    c.drawString(180, height - 50, "Automated Data Report")

    y = height - 100

    # Write summary to PDF
    for col in summary.columns:
        c.drawString(50, y, f"Column: {col}")
        y -= 20

        for stat in summary.index:
            value = round(summary[col][stat], 2)
            text = f"{stat}: {value}"
            c.drawString(70, y, text)
            y -= 15

        y -= 20

        if y < 100:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 100

    c.save()
    print("PDF Report Generated Successfully!")


# Main function
def main():
    file_name = "data.csv"
    output_file = "report.pdf"

    data = read_data(file_name)
    summary = analyze_data(data)
    generate_pdf(summary, output_file)


# Run program
if __name__ == "__main__":
    main()
