
# try:
#     fr = open("file1.txt","r",encoding="utf-8")
# except FileNotFoundError as fe:
#     print(fe)
# finally:
#     fr.close()
#     print("File is closed")

# fr = open("file1.txt","r",encoding="utf-8")   
# for i in fr :
#     print(i,end="")   

# content = fr.read()
# print(content)

# content = fr.readline() # 1 line okur
# content = fr.readlines() # diziye atar
# print(content,end="")

# for i in fr.readlines() :
# print(fr.tell()) # cursor un konumu
#     print(i,end="")
# fr.seek(2) # cursor konumlandirma
# fw.writelines(list)
# fw.write(str)
with open("file1.txt","r",encoding="utf-8") as fr :
    for line in fr.readlines() :
        print(line,end="")
        




        
    
