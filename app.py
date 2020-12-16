from flask import Flask, request, render_template
from flask_cors import CORS

try:
    from .model import get_tweet_similar, preprocessText
except ImportError:
    from model import get_tweet_similar, preprocessText

app = Flask(__name__)
CORS(app)


#return the prediction 
def submit_txt(txt):
	top20tw = get_tweet_similar(txt)
	i = 1
	strResult = ""
	for tweet in top20tw :
		strResult += '<p> Tweet number '+str(i)+' : ['+tweet["text"]+"] date : ["+tweet['date']+"] confidence : ["+str(tweet["confidence"])+']</p>'
		i = i+1
	return strResult


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		details = request.form	
		if details['form_type'] == 'submit_txt':
			return submit_txt(details['txt'])
	return render_template('interface2.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')