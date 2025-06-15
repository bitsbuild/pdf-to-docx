# 📝 PDF to DOCX Converter

A minimal Python script to convert a PDF file into a Word DOCX file using the `pdf2docx` library.

---

## 📦 Requirements

- Python 3.x
- `pdf2docx` library

Install the library using pip:

```bash
pip install pdf2docx
````

---

## 🚀 Usage

Place your input PDF as `input.pdf` in the same folder and run the script:

```python
from pdf2docx import Converter

pdf_file = r"./input.pdf"
docx_file = r"./output.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
```

The converted Word file will be saved as `output.docx`.

---

## 📁 Notes

* Accuracy may vary depending on the layout of the PDF.
* No complex formatting is preserved.
