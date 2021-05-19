import os
<<<<<<< HEAD
import sys
=======
>>>>>>> b7a695652455c758bddc03a1de6679fdf51a661b

from Steam_spider import Spider
from Info_extractor import Extractor
from Reviews_writer import Writer

__author__ =  "YU Yang"

def main():
    os.chdir(os.getcwd())
<<<<<<< HEAD
    appid = sys.argv[1]
=======
    # appid = input("Please input the appid here: ")
    appid = '275850' # No Man's Sky

>>>>>>> b7a695652455c758bddc03a1de6679fdf51a661b

    SteamCollector = Spider(appid)
    source_dict, _ = SteamCollector.source()
    print("Review collection complete!")
    SteamExtractor = Extractor(source_dict)
    record_dict,positive,negative,total,non_en_rates = SteamExtractor.handle_info()
    print("Review analysis complete!")
    
    try:
<<<<<<< HEAD
        os.chdir('{}_data'.format(appid))
    except:
        os.mkdir('{}_data'.format(appid))
        os.chdir('{}_data'.format(appid))

=======
        os.chdir('data')
    except:
        os.mkdir('data')
        os.chdir('data')

    with open('{} Info'.format(appid),'w+',encoding='utf-8') as file_info:
        file_info.write("positive: {}, negative: {}, total: {}, non_en_rates: {}".format(positive,negative,total,non_en_rates))
    
    
>>>>>>> b7a695652455c758bddc03a1de6679fdf51a661b
    SteamWriter = Writer(appid,record_dict)
    SteamWriter.write_all()
    

if __name__ == "__main__":
    main()
