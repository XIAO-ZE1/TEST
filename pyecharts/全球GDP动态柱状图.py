from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline

with open('pyecharts/1960-2019GDP.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines() # 读取所有行
    lines.pop(0) # 去掉第一行
dict={} # 创建字典
for line in lines:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    gdp = float(line.split(',')[2])
    try:
        dict[year].append((country,gdp))
    except KeyError:
        dict[year] = [(country,gdp)]

timeline=Timeline()
sortDict=sorted(dict.keys()) # 按年份排序
for year in sortDict:
    dict[year].sort(key=lambda x:x[1],reverse=True) # 按gdp排序 倒序
    year_dict = dict[year][:10] # 取前10名
    x_data = []
    y_data = []
    for country_gdp in year_dict:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/1000000000) # 转换为亿
    
    bar=Bar(init_opts=opts.InitOpts(width="1000px", height="600px"))
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data,label_opts=opts.LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(title_opts=opts.TitleOpts(title=f"{year}年全球GDP动态柱状图"),
                        xaxis_opts=opts.AxisOpts(name="国家",name_gap=30),
                        yaxis_opts=opts.AxisOpts(name="GDP(亿)"),
                        legend_opts=opts.LegendOpts(is_show=False))
    
    timeline.add(bar,str(year))

timeline.add_schema(play_interval=700,is_auto_play=True,is_timeline_show=True,is_loop_play=False)
timeline.render('pyecharts/全球GDP动态柱状图.html')