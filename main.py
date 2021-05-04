import os

from Steam_spider import Spider
from Info_extractor import Extractor
from Reviews_writer import Writer

__author__ =  "YU Yang"

def main():
    os.chdir(os.getcwd())
    appid = input("Please input the appid here: ")

    SteamCollector = Spider(appid)
    source_dict, _ = SteamCollector.source()
    print("Review collection complete!")
    SteamExtractor = Extractor(source_dict)
    record_dict,positive,negative,total,non_en_rates = SteamExtractor.handle_info()
    print("Review analysis complete!")
    
    try:
        os.chdir('data')
    except:
        os.mkdir('data')
        os.chdir('data')

    SteamWriter = Writer(appid,record_dict)
    SteamWriter.write_all()
    

if __name__ == "__main__":
    main()
