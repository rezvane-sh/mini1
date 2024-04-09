import os

# تابع برای جستوجو
def search(files , string):
    for file in os.listdir(files): #دسترسی به فایل ها
        i=1
        with open(os.path.join(files , file) , 'r' , encoding="utf-8") as filee: # باز کردن فایل 
            for str in filee: # جستجوی خط به خط
                if string in str:   
                     print(f"string ***{string}*** found in {file}: line={i}")
                i+=1
   

# رشته مد نظر
string = input("enter your string: ")

#آدرس فایل ها
files= 'dickens'

# فراخوانی تابع
search(files , string)
