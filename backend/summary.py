import sys
import re
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import metapy
import gensim
from gensim.summarization.summarizer import summarize

def clean_text(html_text):
    # Remove HTML tags
    # clean_text = html_text.decode('utf-8')
    soup = BeautifulSoup(html_text, 'html.parser')
    text_content = soup.get_text().lower()

    # # Unescape HTML entities
    # # clean_text = HTMLParser.HTMLParser().unescape(text_content)

    # # Remove unwanted characters and extra whitespaces
    # cleannn_text = re.sub(r'\s+', ' ', text_content).strip()

    clean_text = re.sub(r'[^a-zA-Z0-9\s.,;:!?\'"-]', '', text_content)

    return clean_text


def convert_to_dat(text_data, file_name='output/output.dat'):
    try:
        with open(file_name, 'w') as file:
            file.write(text_data)
            # print(f'Successfully converted and saved to {file_name}')
    except Exception as e:
        # print(f'Error: {e}')
        print('error is ', e)

def create_config_toml():
    # Create a config.toml file based on the article title
    config_content = """
    prefix = "."
    stop-words = "stopwords.txt"

    dataset = "output"
    corpus = "line.toml"
    index = "news-articles-idx"
    
    [[analyzers]]
    method = "ngram-word"
    ngram = 1
    filter = "default-unigram-chain"
    """
    
    # Save config to a file
    with open('config.toml', 'w') as config_file:
        config_file.write(config_content)

def summarize_article(article_text):
    convert_to_dat(article_text)
    create_config_toml()

    # Create a Tokenizer
    # tok = metapy.analyzers.ICUTokenizer()

    # # Create an Inverted Index
    # idx = metapy.index.make_inverted_index('config.toml')

    # # Create a Ranker using the BM25 ranking function
    # ranker = metapy.index.OkapiBM25()

    # # Create a Summarizer
    # summarizer = metapy.summarization.Summarizer(tok, ranker, idx)

    # # Tokenize and summarize the article
    # doc = metapy.index.Document()
    # doc.content(article_text)
    # summary = summarizer.summarize(doc, 3)  # 3 is the number of sentences in the summary
    # Tokenize and rank the article
    # tok.set_content(article_text)
    # tok_id = metapy.index.Document()
    # tok_id.content(article_text)
    # ranking = ranker.score(idx, tok_id)

    # # Get the top-ranked sentences
    # top_sentences = sorted(enumerate(ranking), key=lambda x: x[1], reverse=True)[:3]

    # # Extract the top sentences
    # top_sentences_text = [idx.metadata(i).get('content') for i, _ in top_sentences]
    # print(top_sentences_text)

    # # Join the top sentences to create the summary
    # summary = ' '.join(top_sentences_text)

    summary = summarize(article_text, ratio=0.05)

    return summary

article_text = sys.stdin.read()
cleaned_text = clean_text(article_text)
# print(cleaned_text)
# summary = summarize(cleaned_text, ratio=0.5)
summary = summarize_article(cleaned_text)
print(summary)