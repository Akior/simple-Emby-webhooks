from flask import Flask,request,json
import requests

bot_id="botXXXXXXXXXXXXXXXXXXXXXXXX"
urls="https://api.telegram.org/"+bot_id+"/sendPhoto"
chat_id=-XXXXXXXXXXXX
emby_url="http://XXXX.XXXX.com"

app = Flask(__name__)

@app.route('/emby', methods=['POST'])
def index():
   event_data = json.loads(request.form.get('data', {}))
   if ( event_data['Item']['Type'] == 'Episode' ):
#get series
     print(event_data['Item']['SeriesId'])
     try:
        print(event_data['Description'])
        body = {"chat_id":chat_id, "photo":emby_url+"/Items/"+event_data['Item']['SeriesId']+"/Images/Primary", "caption": "New element \n"+event_data['Title']+"\n Description:\n"+event_data['Description']}
     except:
        body = {"chat_id":chat_id, "photo":"https://emby.media/resources/shutterstock_1434923111.jpg", "caption": "New element \n"+event_data['Title']}
   if ( event_data['Item']['Type'] == 'Movie' ):
#find movies?
     try:
        print(event_data['Description'])
        body = {"chat_id":chat_id, "photo":emby_url+"/Items/"+event_data['Item']['Id']+"/Images/Primary", "caption": "New element \n"+event_data['Title']+"\n Description:\n"+event_data['Description']}
     except:
        body = {"chat_id":chat_id, "photo":"https://emby.media/resources/shutterstock_1434923111.jpg", "caption": "New element \n"+event_data['Title']}
   y = requests.post(urls, json = body)
   return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18000, debug=True)
