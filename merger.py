import os
from fpdf import FPDF
from pip._vendor.distlib.compat import raw_input

pdf = FPDF()

destination_path = "/Users/uhel/Documents/claim_form.pdf"

image_paths = raw_input("ENTER PATH TO YOUR IMAGES SEPARATED BY &\n")

pdf_destination_path = raw_input("ENTER DESTINATION PATH FOR YOUR PDF FILE\n")

if pdf_destination_path[-3:] != '.pdf':
    pdf_destination_path = "".join((pdf_destination_path, '.pdf'))
image_paths = image_paths.split("&")

for image in image_paths:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)

pdf.output(pdf_destination_path, "F")

if os.path.isfile(pdf_destination_path):
    print("PDF was created successfully, \nPATH: " + pdf_destination_path)


