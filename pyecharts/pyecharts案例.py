import random
from pyecharts import options as opts

# 折线图
from pyecharts.charts import Line

line=Line()
line.add_xaxis(["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"])
line.add_yaxis("商家A",[5,20,36,10,75,90])
# 全局配置
line.set_global_opts(
    title_opts=opts.TitleOpts(title="折线图示例",pos_left='center')
    )
line.render('pyecharts/练习折线图.html')

# 地图
from pyecharts.charts import Map

map=Map()
data=[("北京市",99),("上海市",random.randint(0,100)),("陕西省",random.randint(0,100)),("河南省",random.randint(0,100))]
map.add("地图",data,'china')
map.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,
        max_=200,
        min_=0,
        orient='horizontal',
        pos_left='center',
        pos_top='90%'
        )
    )
map.render('pyecharts/练习地图.html')

# 柱状图+动态timeline
from pyecharts.charts import Bar, Timeline

bar1=Bar()
bar1.add_xaxis(["中国","美国","日本","韩国","英国"])
bar1.add_yaxis("GDP",[900,1000,800,400,600],label_opts=opts.LabelOpts(position='right'))
bar1.reversal_axis() # 翻转x和y轴

bar2=Bar()
bar2.add_xaxis(["中国","美国","日本","韩国","英国"])
bar2.add_yaxis("GDP",[1000,900,800,400,600],label_opts=opts.LabelOpts(position='right'))
bar2.reversal_axis()

timeline=Timeline()
timeline.add(bar1,"2020")
timeline.add(bar2,"2021")
timeline.add_schema(play_interval=1000,is_auto_play=True)

timeline.render('pyecharts/练习柱状图.html')


# 3D柱状图
from pyecharts.charts import Bar3D

x_data = y_data = list(range(10))

def generate_data():
    data = []
    for j in range(10):
        for k in range(10):
            value = random.randint(0, 9)
            data.append([j, k, value * 2 + 4])
    return data

bar3d = Bar3D()
for _ in range(10):
    bar3d.add(
        "",
        generate_data(),
        shading="lambert",
        xaxis3d_opts=opts.Axis3DOpts(data=x_data, type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(data=y_data, type_="value"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
bar3d.set_global_opts(title_opts=opts.TitleOpts("Bar3D-堆叠柱状图示例"))
bar3d.set_series_opts(**{"stack": "stack"})
bar3d.render("pyecharts/bar3d_stack.html")
