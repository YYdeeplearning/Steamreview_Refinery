import json
import pandas as pd


class Writer:
    def __init__(self, appid, record_dict) -> str:
        self.appid = appid
        self.record_dict = record_dict

    def result_csv(self):
        csv_list = []
        for value in self.record_dict.values():
            author_id,attitude,helpful,funny,updated_time,length,review = value
            csv_dict = {'author_id':author_id,'attitude':attitude,'helpful':helpful,'funny':funny,'updated_time':updated_time,'length':length,'review':review}
            csv_list.append(csv_dict)

        data_df = pd.DataFrame(csv_list)
        data_df.to_csv('{}_csv.csv'.format(self.appid))
    

    def result_json(self):
        with open('{}_json.json'.format(self.appid), 'w+', encoding='utf-8') as file_json_dict:
            for key,value in self.record_dict.items():
                index = key
                author_id,attitude,helpful,funny,updated_time,length,review = value
                json.dump({index:{'author_id':author_id,'attitude':attitude,'helpful':helpful,'funny':funny,'updated_time':updated_time,'length':length,'review':review}}, file_json_dict, indent = 4)

    
    def result_txt(self):
        with open('{}_txt.txt'.format(self.appid), 'w+', encoding='utf-8') as file_txt:
            for key,value in self.record_dict.items():
                index = key
                author_id,attitude,helpful,funny,updated_time,length,review = value
                file_txt.write('{})  {}   {}  {}  {}   {}   {} %%%% {} \n\n'.format(index,author_id,attitude,helpful,funny,updated_time,length,review))


    
    def write_all(self):
        self.result_csv()
        self.result_json()
        self.result_txt()
        print("Write to local done!")
