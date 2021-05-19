import os
import sys

from Steam_spider import Spider
from Info_extractor import Extractor
from Reviews_writer import Writer

__author__ =  "YU Yang"

def main():
    os.chdir(os.getcwd())
    # appid = input("Please input the appid here: ")
    appid = sys.argv[1]

    SteamCollector = Spider(appid)
    source_dict, _ = SteamCollector.source()
    print("Review collection complete!")
    SteamExtractor = Extractor(source_dict)
    record_dict,positive,negative,total,non_en_rates = SteamExtractor.handle_info()
    print("Review analysis complete!")
    
    try:
        os.chdir('{}_data'.format(appid))
    except:
        os.mkdir('{}_data'.format(appid))
        os.chdir('{}_data'.format(appid))

    with open('{} Info'.format(appid),'w+',encoding='utf-8') as file_info:
        file_info.write("positive: {}, negative: {}, total: {}, non_en_rates: {}".format(positive,negative,total,non_en_rates))
    
    SteamWriter = Writer(appid,record_dict)
    SteamWriter.write_all()
    

if __name__ == "__main__":
    main()
