
# تایع برای جستوجو
def search(files , string):
    for file_txt in files:
        # باز کردن فایل 
        file = open(file_txt, 'r' , encoding="utf-8")
        
        # جستجو در فایل
        for str in file:
            if string in str:
                print(f"string *{string}* found in *{file_txt}*:")
                print(str)
        
        # بستن فایل
        file.close()

# رشته مد نظر
string = input("enter your string: ")

# لیستی فایل‌ها
files = ['564-0.txt', 'pg699.txt']

search(files , string)