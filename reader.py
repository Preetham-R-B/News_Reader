import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {
	'wired': 'https://www.wired.com/feed/',
	'bbc': 'http://feeds.bbci.co.uk/news/rss.xml'
}

@app.route("/", methods=['GET', 'POST'])
def default():
	query = request.form.get("publication")
	if not query or query.lower() not in RSS_FEEDS:
		publication = "wired"
	else:
		publication = query.lower()
	return get_news(publication)

@app.route("/wired")
def wired():
	return get_news('wired')

@app.route("/bbc")
def bbc():
	return get_news('bbc')

def get_news(publication):
	feed = feedparser.parse(RSS_FEEDS[publication])
	return render_template("home.html", articles=feed['entries'], publication=publication)

if __name__ == "__main__":
	app.run(port=5000, debug=True)
