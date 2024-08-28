from pdf2docx import parse
from pathlib import Path

pdf_file = str(Path.home() / Path('Desktop', 'pdf.pdf'))
docx_file = str(Path.home() / Path('Desktop', 'word.docx'))

# convert pdf to docx
parse(pdf_file, docx_file)