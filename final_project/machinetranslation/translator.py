import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

os.environ['apikey'] = 'rXmfgYmsqxIUaTtHVtqFjNMas7ImdiBi8OmrkQ_eYfpB'
os.environ['url'] = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/b65a8cca-561c-45bf-b2e8-f666f460f596'
authenticator = IAMAuthenticator('rXmfgYmsqxIUaTtHVtqFjNMas7ImdiBi8OmrkQ_eYfpB')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
SERVICE_URL = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/b65a8cca-561c-45bf-b2e8-f666f460f596'
language_translator.set_service_url(SERVICE_URL)

#translate from english to french
def english_to_french(english_text):
    'translate hello to bonjour'
    translator = language_translator.translate(text = english_text, model_id = "en-fr").get_result()
    french_text = translator['translations'][0]['translation']
    return french_text

#translate from french to english
def french_to_english(french_text):
    'translates bonjour to hello'
    translator = language_translator.translate(text = french_text, model_id = "fr-en").get_result()
    english_text = translator['translations'][0]['translation']
    return english_text
