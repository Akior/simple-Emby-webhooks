from flask import Flask,request,json
import requests

server = "http://127.0.0.1:8096";
Text='Hello'
Header='';
TimeoutMs='1500';
api_key='XXXXXX';


app = Flask(__name__)

@app.route('/emby', methods=['POST'])
def index():
	event_data = json.loads(request.form.get('data', {}))
  #post back if event playback.start
	if (event_data['Event'] == "playback.stop"):
		url = server+"/emby/Sessions/"+event_data['Session']['Id']+"/Message?Text="+Text+"&Header="+Header+"&TimeoutMs="+TimeoutMs+"&api_key="+api_key
		post_fields = "Text="+Text+"&Header="+Header+"&TimeoutMs="+TimeoutMs+"&api_key="+api_key
		x = requests.post(url, data = post_fields)
		print(x.text)
	return ''

if __name__ == '__main__':
    app.run()

