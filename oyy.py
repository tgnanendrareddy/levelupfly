from docx import Document

document = Document()

document.add_paragraph(input("tell me about your self"))

document.save('gittha.docx')
