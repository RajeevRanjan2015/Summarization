from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
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


if __name__ == '__main__':
    app.run(debug=True)