import os



major_list=[]

with open("major_list.txt",'r',encoding='utf-8') as file:
    for i in file.readlines():
        major_list.append(i.strip('\ufeff').strip('\n'))



#
# list=os.listdir("./rank")
# for i in list:
#     list[list.index(i)]=i.replace('.txt','')
# for i in major_list:
#     if i not in list:
#         print(i)


#空格&nbsp;


for i in major_list:
    print("正在创建%s"%(i))
    html='''
    <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no" />
    <title>%s</title>
    <link href="https://cdn.bootcss.com/mui/3.4.0/css/mui.min.css" rel="stylesheet">
    <script src="https://cdn.bootcss.com/mui/3.4.0/js/mui.min.js"></script>
</head>

<body>
    <!--带策划导航的页面由两部分构成，一部分是class为mui-off-canvas-wrap的元素（要弹出的侧菜单），另一部分是class为mui-inner-wrap的元素（正常页面）-->
    <div class="mui-off-canvas-wrap">
        <!--上面class为mui-off-canvas-wrap的元素即为要弹出的侧菜单-->
        <aside id="catalog" class="mui-off-canvas-right">
            <!--上面class为mui-off-canvas-right的元素标志这是一个右侧弹出的菜单，若要改为其他方位弹出，可参考官方示例-->
            <!--注意，此处的id非常重要，它的值要和后面“选择章节”按钮的href属性值对应，才能自动绑定-->
            <div class="mui-scroll-wrapper">
                <div class="mui-scroll">
                    <!--上面class为mui-scroll-wrapper和mui-scroll的两行，是为了让内容太长的时候可以滚动-->
                    <ul class="mui-table-view mui-table-view-inverted">
                        <!--ul和li是列表，可参见04实例，其中mui-table-view-inverted是为了让列表颜色反白，呈现黑底白字效果-->
                        <li class="mui-table-view-cell">
                            <a class="mui-navigate" href="#chapter1">
                                <!--上面class为mui-navigate-right的列表，是为了右面有个小箭头，此处注意href属性的值是要链接的页内锚点，要和后面的锚点name属性的值对应-->
                                </br><h3>专业简介</h3></br>
                            </a>
                        </li>
                        <li class="mui-table-view-cell">
                            <a class="mui-navigate" href="#chapter2">
                                </br><h3>专业性视频</h3></br>
                            </a>
                        </li>
                        <li class="mui-table-view-cell">
                            <a class="mui-navigate" href="#chapter3">
                                </br><h3>有趣性视频</h3></br>
                            </a>
                        </li>
						<li class="mui-table-view-cell">
						    <a class="mui-navigate" href="#chapter4">
						        </br><h3>相关院校排名</h3></br>
						    </a>
						</li>
                    </ul>
                </div>
            </div>
        </aside>
        <div class="mui-inner-wrap">
            <!--上面class为mui-inner-wrap的元素即为正常页面-->
            <header class="mui-bar mui-bar-nav">
                <a href="../home.html" class="mui-icon mui-icon-arrowleft"></a>
                <!--注意，上面的href属性值非常重要，它的值要和前面侧菜单的id属性值对应，才能自动绑定-->
                <h1 class="mui-title"><strong>
%s</strong></h1>
            </header>
            <div class="mui-content mui-scroll-wrapper">
                <div class="mui-scroll" style="padding:20px">
                    <a name="chapter1" id="chapter1" ><font color="#000000"><h3>专业简介</br></h3></font></a></br>
                    <!--上面这种没有href属性的超链接a元素，叫做“锚点”，即页面内链接，比如在其他a元素的href中定义此锚点的name属性值“chapter1”，页面就会滚动到这个位置-->

    '''%(i,i)


    #baike

    with open("./baike/%s.txt"%(i),'r',encoding='utf-8') as file:
        for j in file.readlines():
            content=j.strip("\n").strip("\ufeff")
            html+="<h5>&nbsp;&nbsp;&nbsp;&nbsp;%s</h5></br>"%(content)

    html+='''
    <h5 align="right">
  ————from百度百科
    </h5></br><a name="chapter2" id="chapter2" ><font color="#000000"><h3>专业性视频</h3></font></a></br>
    '''

    #bili  profess
    judge=0
    list = os.listdir("./bilibili/profess")
    for j in list:
        list[list.index(j)] = j.replace('.txt', '')
    if i not in list:
        html+='''
        <h5>暂时没有相关视频</h5>
        '''
    else:
        html+='<ul class="mui-table-view">'
        title=[]
        urls=[]
        num=0
        js=0
        with open("./bilibili/profess/%s.txt" % (i), 'r', encoding='utf-8') as file:
            for j in file.readlines():
                num+=1
                if num % 2 == 1:
                    title.append(j.strip("\n").strip("\ufeff"))
                    js+=1
                else:
                    urls.append(j.strip("\n").strip("\ufeff"))
                if num==10:
                    break
        for j in range(0,js):
            add='''
            <li class="mui-table-view-cell mui-media">
							<a href="https://%s" class="">
								
								<div class="mui-media-body">
									%s
								</div>
								<!--上面class为mui-media-body的div，是图文列表中的文-->
							</a>
						</li>

            '''%(urls[j],title[j])
            html+=add

    html+='''
    </ul>
			
					
					
					
					</br><a name="chapter3" id="chapter3" ><font color="#000000"><h3>有趣性视频</h3></font></a></br>

    '''
    # bili  funny
    judge = 0
    list = os.listdir("./bilibili/funny")
    for j in list:
        list[list.index(j)] = j.replace('.txt', '')
    if i not in list:
        html += '''
            <h5>暂时没有相关视频</h5>
            '''
    else:
        html+='<ul class="mui-table-view">'
        title = []
        urls = []
        num = 0
        js = 0
        with open("./bilibili/funny/%s.txt" % (i), 'r', encoding='utf-8') as file:
            for j in file.readlines():
                num += 1
                if num % 2 == 1:
                    title.append(j.strip("\n").strip("\ufeff"))
                    js += 1
                else:
                    urls.append(j.strip("\n").strip("\ufeff"))
                if num == 10:
                    break
        for j in range(0, js):
            add = '''
                <li class="mui-table-view-cell mui-media">
    							<a href="https://%s" class="">

    								<div class="mui-media-body">
    									%s
    								</div>
    								<!--上面class为mui-media-body的div，是图文列表中的文-->
    							</a>
    						</li>

                ''' % (urls[j], title[j])
            html += add

    #rank
    html+='''
    </ul></br><a name="chapter4" id="chapter4" ><font color="#000000"><h3>相关院校排名</h3></font></a></br>
    '''
    list = os.listdir("./rank")
    for j in list:
        list[list.index(j)] = j.replace('.txt', '')
    if i not in list:
        html += '''
                <h5>暂时没有相关资料</h5>
                '''
    else:
        add=''
        with open("./rank/%s.txt"%(i),'r',encoding='utf-8') as file :
            for j in file.readlines():
                add+=j.strip('\n').strip("\ufeff")
        html+=add
        html+='''
        <h5 align="right">
  ————from校友会and高三网
    </h5>
        '''
    html+='''
				</div>
            </div>
            <div class="mui-off-canvas-backdrop"></div>
            <!--上面这个div很重要，有了它点击页面空白处才能关闭侧菜单，没有它关不掉-->
        </div>
    </div>
    <script>
        mui('.mui-scroll-wrapper').scroll();
        //上面这句是让class为mui-scroll-wrapper的元素可以滚动
        mui(document.body).on('click', '.mui-navigate-right', function (e) {
            mui('.mui-off-canvas-wrap').offCanvas('close');
        });
        //上面这句mui带的、很常用的事件绑定语句，意思是：让class为mui-navigate-right的元素（即侧菜单里面的章节）在被点击（click）之后，侧菜单收回
    </script>
</body>
</html>
    '''
    with open("../MajorPage/%s.html"%(i),'a',encoding='utf-8') as file:
        file.write(html)

