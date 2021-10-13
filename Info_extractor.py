import re
import nltk
import time
import langid
from better_profanity import profanity

# from googletrans import Translator
# translator = Translator()


class Extractor:
    def __init__(self, source_dict) -> None:
        self.source_dict = source_dict
    
    def handle_info(self):
        reviews_info = self.source_dict['reviews']  
        record_dict = {}        
        index, en_sum, total = 1, 0, 0
        positive = negative = non_en = 0

        for item in reviews_info.values():
            comment = item.get('review')
            text = re.sub('\s+', ' ', comment)

            censored_review = profanity.censor(text)
            review = censored_review.replace("*","")

            # try:
            #     lang_id = translator.detect(review).lang
            # except:
            #     lang_id = 'error'
            
            try:
                lang_id = langid.classify(review)[0]
            except:
                lang_id = 'error'
            
            length = len(nltk.word_tokenize(review))

            if length != 0 and lang_id == 'en':

                author_id = item.get('author')['steamid']

                voted_up = item.get('voted_up')
                if voted_up == True:
                    attitude = "Recommended"
                    positive += 1
                else:
                    attitude = "Not Recommended"
                    negative += 1
                
                helpful = item.get('votes_up')
                funny = item.get('votes_funny')
                
                timestamp_updated = item.get('timestamp_updated')

                
                time_local = time.localtime(timestamp_updated)
                updated_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

                            
                record_dict[index] = (author_id,attitude,helpful,funny,updated_time,length,review)
            
                index += 1
                en_sum += 1
            else:

                non_en += 1
            
            total += 1

        assert positive + negative == en_sum, "Total != POS + NEG"
        non_en_rates = non_en/total

        return record_dict,positive,negative,total,non_en_rates
