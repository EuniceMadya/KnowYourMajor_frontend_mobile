import os



major_list=[]

with open("major_list.txt",'r',encoding='utf-8') as file:
    for i in file.readlines():
        major_list.append(i.strip('\ufeff').strip('\n'))



for i in major_list:
    print("正在创建%s"%(i))
    with open("./baike/%s.txt"%(i),'r',encoding='utf-8') as file:
        print(file.readlines())