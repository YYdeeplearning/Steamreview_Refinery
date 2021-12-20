import os

from Steam_spider import Spider
from Info_extractor import Extractor
from Reviews_writer import Writer

__author__ =  "YU Yang"

def main():
    os.chdir(os.getcwd())
    appid = '570' #Dota2

    SteamCollector = Spider(appid)
    source_dict, _ = SteamCollector.source()
        
    SteamExtractor = Extractor(source_dict)
    record_dict, positive, negative, en_sum, total, non_en_rates = SteamExtractor.handle_info()
    print("Review analysis complete!")
    
    try:
        os.chdir('data/{}'.format(appid))
    except:
        os.mkdir('data/{}'.format(appid))
        os.chdir('data/{}'.format(appid))

    with open('{}_info.txt'.format(appid), 'w+', encoding='utf-8') as file_info:
        file_info.write("positive: {}, negative: {}, sum: {}, collected: {}, non_en_rates: {}".format(positive, negative, en_sum, total, non_en_rates))
    
    
    SteamWriter = Writer(appid,record_dict)
    SteamWriter.write_all()
    

if __name__ == "__main__":
    main()

