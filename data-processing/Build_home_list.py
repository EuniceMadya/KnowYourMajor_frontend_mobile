from pypinyin import lazy_pinyin

chars=[]
with open("major_list.txt",'r',encoding='utf-8') as file:
    for i in file.readlines():
        chars.append(i.strip('\ufeff').strip('\n'))
# print(chars,len(chars))

chars_=[]

chars.sort(key=lambda char: lazy_pinyin(char)[0][0])
chars_=[lazy_pinyin(char) for char in chars]
# print(chars)

chars_ABC=[]

for i in chars_:
    chars_ABC.append(i[0])

print(chars_ABC,len(chars_ABC))


file=open("home_list_code.txt",'w',encoding="utf-8")

list_abc=[]


print(chars_ABC,len(chars_ABC))

for i in range(0,547):
    cap=chars_ABC[i][0]
    if cap not in list_abc:
        list_abc.append(cap)
        add='''
        <li class="mui-table-view-cell">
        <a class="mui-navigate">
        <h2>%s↓<h2>
        </a>
        </li>
        '''%(str.upper(cap))
        file.write(add)
    add = '''
        <li class="mui-table-view-cell">
        <a class="mui-navigate" href="MajorPage/%s.html">
        %s
        </a>
        </li>
        '''%(chars[i],chars[i])
    file.write(add)
file.close()
