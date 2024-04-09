import os

# تابع برای جستوجو
def search(files , string):
<<<<<<< HEAD
    for file in os.listdir(files):
        i=1
        with open(os.path.join(files , file) , 'r' , encoding="utf-8") as filee:
            for str in filee:
=======
    for file in os.listdir(files): #دسترسی به فایل ها
        i=1 #  شمارشگر خط
        with open(os.path.join(files , file) , 'r' , encoding="utf-8") as filee: # باز کردن فایل 
            for str in filee: # جستجوی خط به خط
>>>>>>> 7dd856eb67808516b01b3d69fc43dc1325bbdf73
                if string in str:   
                     print(f"string ***{string}*** found in {file}: line={i}")
                i+=1
   

# رشته مد نظر
string = input("enter your string: ")

#آدرس فایل ها
files= 'dickens'

# فراخوانی تابع
search(files , string)
