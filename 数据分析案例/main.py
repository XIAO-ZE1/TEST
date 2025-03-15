from file import Record, TextFileReader, JsonFileReader
from pyecharts import options as opts
from pyecharts.charts import Bar

text=TextFileReader('数据分析案例/data_output.txt')
json1=JsonFileReader('数据分析案例/data_output.json')
all_data:list[Record]=text.read_data()+json1.read_data()


data_dict={}
for data in all_data:
    if data.date not in data_dict:
        data_dict[data.date]=data.money
    else:
        data_dict[data.date]+=data.money

bar=Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis('销售额',list(data_dict.values()),label_opts=opts.LabelOpts(position='top'))
bar.set_global_opts(title_opts=opts.TitleOpts(title='每日销售额柱状图'))
bar.render('数据分析案例/data_output.html')