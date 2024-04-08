import os

# تایع برای جستوجو
def search(files , string):
    for file in os.listdir(files):
        with open(os.path.join(files , file) , 'r' , encoding="utf-8") as filee:
            file_txt=filee.read()
        
        # جستجو در فایل
            if string in file_txt:
                
                print(f"string *{string}* found in *{file}*:")
            
   
 # رشته مد نظر
string = input("enter your string: ")
files= 'dickens'
search(files , string)