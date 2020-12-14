from PyPDF2 import PdfFileMerger, PdfFileReader
import os

merged_object = PdfFileMerger()
str_output_name = 'output.pdf'

lst_pdfs = []
for obj in os.listdir('orders/'):
    if '.pdf' in obj:
        lst_pdfs.append(obj)
        print(lst_pdfs)

for file_name in lst_pdfs:
    merged_object.append(PdfFileReader(f'orders/{file_name}'), 'rb')
merged_object.write(f'orders/{str_output_name}')