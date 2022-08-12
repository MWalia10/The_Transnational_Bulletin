#TRANSLATION MODEL
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")
model = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")

from transformers import MBartForConditionalGeneration, MBartTokenizer
from transformers import MBart50TokenizerFast
class Translator:

    '''
        Install Requirements -
        pip install pickle5 transformers==4.12.2 sentencepiece
        MBart Documentation
        https://huggingface.co/transformers/model_doc/mbart.html
        Get the supported lang codes
        https://huggingface.co/facebook/mbart-large-50-one-to-many-mmt
        Class - Translator
        Initializes MBart Seq2Seq Model and Tokenizer
        Helper func to translate input language to desired target language
        Supported Languages: English, Gujarati, Hindi, Bengali, Malayalam, Marathi, Tamil, Telugu, Urdu
        
    '''

    def __init__(self):
        
        self.model = MBartForConditionalGeneration.from_pretrained('facebook/mbart-large-50-many-to-many-mmt')
        self.tokenizer = MBart50TokenizerFast.from_pretrained('facebook/mbart-large-50-many-to-many-mmt')
        self.supported_langs = ['en_XX', 'ar_AR', 'es_XX', 'fr_XX', 'ru_RU']

    def translate(self, input_text, src_lang, tgt_lang):

        if src_lang not in self.supported_langs:
            raise RuntimeError('Unsupported source language.')
        if tgt_lang not in self.supported_langs:
            raise RuntimeError('Unsupported target language.')

        self.tokenizer.src_lang = src_lang
        encoded_text = self.tokenizer(input_text, return_tensors='pt')
        generated_tokens = self.model.generate(**encoded_text, forced_bos_token_id=self.tokenizer.lang_code_to_id[tgt_lang])
        output_text_arr = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

        if len(output_text_arr) > 0:
            return output_text_arr[0]
        else:
            raise RuntimeError('Failed to generate output. Output Text Array is empty.')
#driver function


def translator(txt, lang):
    codes = {'Arabic':'ar_AR','French':'fr_XX', 'Russian':'ru_RU','Spanish':'es_XX'}
    lang_code = codes[lang]
    obj = Translator()
    translated_txt=obj.translate(txt,lang_code,'en_XX')
    return translated_txt


#Importing necessary libraires
import requests
from glom import glom
import pandas as pd

#ARABIC
url_ar = ('https://newsapi.org/v2/top-headlines?sources=google-news-sa&apiKey=d727286721fd4fed98fa35a8b45ee868')
df = pd.read_json(url_ar)

titles_ar = df['articles'].apply(lambda row: glom(row, 'title'))
url_ar = df['articles'].apply(lambda row: glom(row, 'url'))
des_ar = df['articles'].apply(lambda row: glom(row, 'description'))

Eng_title = []
for i in titles_ar.values:
  translated_text = translator(i, 'Arabic')
  Eng_title.append(translated_text)

Eng_des = []
for i in des_ar.values:
  translated_text = translator(i, 'Arabic')
  Eng_des.append(translated_text)


ArabicNews_dict = {"Title": titles_ar, "Description":des_ar, "Eng Title":Eng_title, "Eng_Des":Eng_des, "URL":url_ar }
ArabicNews = pd.DataFrame.from_dict(ArabicNews_dict)
ArabicNews.to_csv('Arabic.tsv', sep="\t")

#FRENCH
url_fr = ('https://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey=d727286721fd4fed98fa35a8b45ee868')
df_fr = pd.read_json(url_fr)

titles_fr = df_fr['articles'].apply(lambda row: glom(row, 'title'))
url_fr = df_fr['articles'].apply(lambda row: glom(row, 'url'))
des_fr = df_fr['articles'].apply(lambda row: glom(row, 'description'))

Eng_title = []
for i in titles_fr.values:
  translated_text = translator(i, 'French')
  Eng_title.append(translated_text)

Eng_des = []
for i in des_fr.values:
  translated_text = translator(i, 'French')
  Eng_des.append(translated_text)

FranceNews_dict = {"Title": titles_fr,"Description":des_fr, "Eng Title":Eng_title, "Eng_Des":Eng_des, "URL":url_fr}
FranceNews = pd.DataFrame.from_dict(FranceNews_dict)
FranceNews.to_csv('French.tsv', sep="\t")


#INDIA
url_in = ('https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=d727286721fd4fed98fa35a8b45ee868')
df_in = pd.read_json(url_in)

titles_in = df_in['articles'].apply(lambda row: glom(row, 'title'))
url_in = df_in['articles'].apply(lambda row: glom(row, 'url'))
des_in = df_in['articles'].apply(lambda row: glom(row, 'description'))

IndiaNews_dict = {"Title": titles_in,"Description":des_in, "URL":url_in }
IndiaNews = pd.DataFrame.from_dict(IndiaNews_dict)
IndiaNews.to_csv('India.tsv', sep="\t")


#RUSSIAN
url_ru = ('https://newsapi.org/v2/top-headlines?sources=google-news-ru&apiKey=d727286721fd4fed98fa35a8b45ee868')
df_ru = pd.read_json(url_ru)

titles_ru = df_ru['articles'].apply(lambda row: glom(row, 'title'))
url_ru = df_ru['articles'].apply(lambda row: glom(row, 'url'))
des_ru = df_ru['articles'].apply(lambda row: glom(row, 'description'))

Eng_title = []
for i in titles_ru.values:
  translated_text = translator(i, 'Russian')
  Eng_title.append(translated_text)

Eng_des = []
for i in des_ru.values:
  translated_text = translator(i, 'Russian')
  Eng_des.append(translated_text)

RussiaNews_dict = {"Title": titles_ru,"Description":des_ru,  "Eng Title":Eng_title, "Eng_Des":Eng_des, "URL":url_ru }
RussiaNews = pd.DataFrame.from_dict(RussiaNews_dict)
RussiaNews_dict
RussiaNews.to_csv('Russian.tsv', sep="\t")

# SPANISH (ARGENTENA)

url_sp = ('https://newsapi.org/v2/top-headlines?sources=google-news-ar&apiKey=d727286721fd4fed98fa35a8b45ee868')
df_sp = pd.read_json(url_sp)

titles_sp = df_sp['articles'].apply(lambda row: glom(row, 'title'))
url_sp = df_sp['articles'].apply(lambda row: glom(row, 'url'))
des_sp = df_sp['articles'].apply(lambda row: glom(row, 'description'))

Eng_title = []
for i in titles_sp.values:
  translated_text = translator(i, 'Spanish')
  Eng_title.append(translated_text)

Eng_des = []
for i in des_sp.values:
  translated_text = translator(i, 'Spanish')
  Eng_des.append(translated_text)

ArgentinaNews_dict = {"Title": titles_sp,"Description":des_sp, "Eng Title":Eng_title, "Eng_Des":Eng_des, "URL":url_sp }
ArgentinaNews = pd.DataFrame.from_dict(ArgentinaNews_dict)
ArgentinaNews.to_csv('Argentina.tsv', sep="\t")


'''
FINAL DICTIONARIES TO RETRIEVE VALUES FROM:
ArabicNews_dict
FranceNews_dict
IndiaNews_dict
RussiaNews_dict
ArgentinaNews_dict
'''