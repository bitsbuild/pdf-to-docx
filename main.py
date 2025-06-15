from pdf2docx import Converter
pdf_file = r"./input.pdf"
docx_file = r"./output.docx"
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()