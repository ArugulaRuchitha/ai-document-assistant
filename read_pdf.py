import fitz
print("AI Document Assistant")
pdf = fitz.open("sample.pdf")
for page in pdf:
    text = page.get_text()
    print(text)