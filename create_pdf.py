import pymupdf

pdf = pymupdf.open()

page = pdf.new_page()

page.insert_text(
    (50, 50),
    "Artificial Intelligence is a technology that enables computers to perform tasks that normally require human intelligence."
)

pdf.save("sample.pdf")

pdf.close()

print("PDF created successfully!")