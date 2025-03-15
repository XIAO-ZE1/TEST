import json

class Record:
    def __init__(self, date,order_id,money,province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province
    def __str__(self):
        return f'{self.date},{self.order_id},{self.money},{self.province}'

class FileReader:
    def read_data(self)->list[Record]:
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path
    def read_data(self)->list[Record]:
        with open(self.path,'r',encoding='utf-8') as f: 
            record_list:list[Record] = []
            for line in f.readlines():
                line=line.strip().split(',') #去掉换行符，以逗号分隔
                record=Record(line[0],line[1],int(line[2]),line[3])
                record_list.append(record)
        return record_list
    
class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path
    def read_data(self)->list[Record]:
        with open(self.path,'r',encoding='utf-8') as f: 
            record_list:list[Record] = []
            for line in f.readlines():
                data_dict = json.loads(line)
                record = Record(data_dict['date'],data_dict['order_id'],int(data_dict['money']),data_dict['province'])
                record_list.append(record)
        return record_list
    
if __name__ == '__main__':
    text=TextFileReader('数据分析案例/data_output.txt')
    json1=JsonFileReader('数据分析案例/data_output.json')
    t=text.read_data()
    j=json1.read_data()
    for l in t:
        print(l)
    for l in j:
        print(l)