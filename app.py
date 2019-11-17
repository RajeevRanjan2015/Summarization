from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.externals import joblib
import pickle
import nltk
import re
nltk.download('stopwords')
nltk.download('punkt')
import bs4 as bs
import urllib.request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analyze_url',methods=['GET','POST'])
def analyze_url():

	if request.method == 'POST':
		raw_url = request.form['message']
		rawtext = raw_url

		final_summary =summarize(rawtext)

	return render_template('result.html',final_summary=final_summary)



#---------------Text Summarization-------------------------------------------------------------------------------------------------

from heapq import nlargest

def summarize(link):
    source=urllib.request.urlopen(link).read()

    soup=bs.BeautifulSoup(source,'lxml')
    text=""
    for paragraph in soup.find_all('p'):
       text+=paragraph.text

    text=re.sub(r'\[[0-9]*\]',' ',text)
    text=re.sub(r"\s+"," ",text)
    clean_text=text.lower()
    clean_text=re.sub(r"\W"," ",clean_text)
    clean_text=re.sub(r"\d"," ",clean_text)
    clean_text=re.sub(r'\s+'," ",clean_text)


    sentences=nltk.sent_tokenize(text)
    stop_words=nltk.corpus.stopwords.words('english')

    word2count={}
    for word in nltk.word_tokenize(clean_text):
        if word not in stop_words:
            if word not in word2count.keys():
                word2count[word]=1
            else:
                word2count[word]+=1

    for key in word2count.keys():
        word2count[key]=word2count[key]/max(word2count.values())
    
    
    
    sent2score={}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word2count.keys():
                if len(sentence.split(' '))<25:
                    if sentence not in sent2score.keys():
                        sent2score[sentence]=word2count[word]
                    else:
                        sent2score[sentence]+=word2count[word]    
    
    
     # Summary result

    # Summary result

    import heapq
    best_sentences=heapq.nlargest(10,sent2score,sent2score.get)


    print('-----------------------------------------------------------------------------------------------------------------------')
    for sentence in best_sentences:
        print(sentence)
   
    print('-----------------------------------------------------------------------------------------------------------------------')    
    summary = ' '.join(best_sentences)  
    return summary
    
#--------------------------------------------------------------------------------------------------------------------------------------




if __name__ == '__main__':
    app.run(debug=True)
    