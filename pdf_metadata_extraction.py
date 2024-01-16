from PyPDF2 import PdfReader

path = "eBook - How to Build a Career in AI.pdf"

with open(path,'rb') as f:
  pdf = PdfReader(f)
  info = pdf.metadata
  print(info)


Example output:
{'/CreationDate': "D:20221213160800-05'00'", '/Creator': 'Adobe InDesign 18.0 (Macintosh)', '/ModDate': "D:20221213160804-05'00'", '/Producer': 'Adobe PDF Library 17.0', '/Trapped': '/False'}

Same thing can also be done via another library:

import pikepdf

path = "eBook - How to Build a Career in AI.pdf"
pdf = pikepdf.Pdf.open(path)
docinfo = pdf.docinfo
print(docinfo)
  
