import os
import fitz
import numpy as np
import pandas as pd
import string
def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(pdf_file)
    for page_num in range(len(doc)):
     page = doc.load_page(page_num)
     text += page.get_text()
    doc.close()
    return text
def main(pdf_folder):
        pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        text_ar=[]
        for pdf_file in pdf_files:
         text=extract_text_from_pdf(pdf_file)
         text_ar.append(text)
        df=pd.DataFrame(text_ar)
        dir_list=os.listdir(pdf_folder)
        for i in range(len(dir_list)):
         dir_list[i]=dir_list[i].replace(".pdf","")
        df.insert(1,'ID',dir_list)
        df.columns=["Resume","ID"]
        print(df)
        return df
if __name__ == "__main__":
    pdf_folder = '/home/shashwat_tripathi/RM_pdf_folder/IIT'
    data_csv=main(pdf_folder).to_csv('resume_file.csv')
