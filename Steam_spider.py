import steamreviews
import json


class Spider:
    def __init__(self,appid) -> int:
        self.appid = appid
        
    
    def source(self):
        request_params = dict()
        # Reference: https://partner.steamgames.com/doc/store/localization#supported_languages
        request_params['language'] = 'english'
        # Reference: https://partner.steamgames.com/doc/store/getreviews
        request_params['review_type'] = 'all'
        request_params['purchase_type'] = 'all'

        app_id = int(self.appid)
        source_dict, query_count = steamreviews.download_reviews_for_app_id(app_id,
                                                                            chosen_request_params=request_params)
        print("query_count: {}".format(query_count))     
        return source_dict,query_count


    def source_output(self):
        source_dict,_ = self.source()
        with open('{}_source.json'.format(self.appid), 'w+', encoding='utf-8') as source_json:
            json.dump(source_dict, source_json, ensure_ascii=False, indent = 4)

    