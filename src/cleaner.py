import pandas as pd 
import re 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from config.constants import NORMALIZATION_MAP
import os 


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

df = pd.read_csv('data/jobs_raw.csv')

def clean_text(text):
    if pd.isnull(text):
        return ''
    
    # Remove HTML
    text = re.sub(r'<.*?>', '', text)

    # Add space after punctuation to avoid merging words (e.g., "PowerBI.SQL" → "PowerBI SQL")
    text = re.sub(r'([a-zA-Z])([.\/\-])([a-zA-Z])', r'\1 \3', text)

    # Lowercase
    text = text.lower()

    for k, v in NORMALIZATION_MAP.items():
        text = text.replace(k, v)

    # Remove special characters, but allow spaces
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize and remove stopwords
    tokens = text.split()
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)
    
def run_cleaner():
    df = pd.read_csv('data/jobs_raw.csv')

    df['clean_description'] = df['description'].apply(clean_text)
    df['clean_title'] = df['title'].apply(clean_text)
    df['clean_company'] = df['company'].apply(clean_text)

    df_final = df[[
        'country', 'city', 'query',
        'title', 'clean_title',
        'company', 'clean_company',
        'description', 'clean_description',
        'salary_min', 'salary_max', 'contract_type'
    ]]

    df_final.to_csv('data/jobs_cleaned.csv', index=False)