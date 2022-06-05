from flask import Flask,jsonify,request
import csv

all_articles = []
with open("Articles.csv",encoding='UTF-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
notliked_articles = []

app = Flask(__name__)
@app.route('/getArticles')
def getArticles():
    return jsonify({
        'data' : all_articles[0],
        'status' : 'success',
    })

@app.route("/likedArticles",methods=["POST"])
def likedMovies():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles = all_articles[1:]
    return jsonify({
        'status' : 'success'
    }),200

@app.route("/likedArticles",methods=["POST"])
def notlikedMovies():
    article = all_articles[0]
    notliked_articles.append(article)
    all_articles = all_articles[1:]
    return jsonify({
        'status' : 'success'
    }),200

if(__name__ == '__main__'):
    app.run()