import os

# تابع برای جستوجو
def search(files , string):
    for file in os.listdir(files):
        i=1
        with open(os.path.join(files , file) , 'r' , encoding="utf-8") as filee:
            for str in filee:
                if string in str:   
                     print(f"string ***{string}*** found in {file}: line={i}")
                i+=1
   

# رشته مد نظر
string = input("enter your string: ")

#آدرس فایل ها
files= 'dickens'

# فراخوانی تابع
search(files , string)
