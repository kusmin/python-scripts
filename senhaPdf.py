import sys

from PyPDF2 import PdfFileReader, PdfFileWriter


def secure_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader()
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"secure_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"secure_file created successfully")


if __name__ == "__main__":
    file = sys.argv[4]
    password = sys.argv[2]
    secure_pdf(file, password)
