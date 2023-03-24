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
   #for shows
   if ( event_data['Item']['Type'] == 'Episode' ):
     try:
        print(event_data['Description'])
        body = {"chat_id":chat_id, "photo":emby_url+"/Items/"+event_data['Item']['SeriesId']+"/Images/Primary", "caption": "New element \n"+event_data['Title']+"\n Description:\n"+event_data['Description']}
     except:
        body = {"chat_id":chat_id, "photo":"https://emby.media/resources/shutterstock_1434923111.jpg", "caption": "New element \n"+event_data['Title']}
   #for movies
   if ( event_data['Item']['Type'] == 'Movie' ):
     dbs=""
     trailers=""
     for x in event_data['Item']['ExternalUrls']:
       keys = x.keys()
       dbs=dbs+"<a href='"+x['Url']+"'>"+x['Name']+"</a>\n"
     size = len(dbs)
     dbs=dbs[:size - 1]
     for y in event_data['Item']['RemoteTrailers']:
       keys = y.keys()
       trailers=trailers+y['Url']+"\n"
     size = len(trailers)
     trailers=trailers[:size - 1]
     server_watch=emby_url+"/web/index.html#!/item?id="+str(event_data['Item']['Id'])+"&serverId="+event_data['Item']['ServerId']
     try:
       #exclude bluray
       if event_data['Item']['Container'] == "bluray":
         multiline_str = """<b>On Server:</b>
"""+event_data['Server']['Name']+"""
<b>New Film:</b>
"""+event_data['Item']['SortName']+"""
<b>Genre:</b>
"""+', '.join(event_data['Item']['Genres'])+"""
<b>Description:</b>
"""+event_data['Item']['Overview'][:300]+"""
<b>Ratings:</b> """+str(event_data['Item']['CommunityRating'])+"""
<b>Year production</b>: """+str(event_data['Item']['ProductionYear'])+"""
<b>See film on external sources:</b>
"""+dbs+"""
<b>Trailers:</b>
"""+trailers+"""
<b>Film physical path:</b>
"""+event_data['Item']['Path'].replace("\\", " ")+"""
<b>Watch link:</b>
<a href='"""+server_watch+"'>Emby</a>"
       else:
         multiline_str = """<b>On Server:</b>
"""+event_data['Server']['Name']+"""
<b>New Film:</b>
"""+event_data['Item']['SortName']+"""
<b>Genre:</b>
"""+', '.join(event_data['Item']['Genres'])+"""
<b>Description:</b>
"""+event_data['Item']['Overview'][:300]+"""
<b>Ratings:</b> """+str(event_data['Item']['CommunityRating'])+"""
<b>Year production</b>: """+str(event_data['Item']['ProductionYear'])+"""
<b>See film on external sources:</b>
"""+dbs+"""
<b>Trailers:</b>
"""+trailers+"""
<b>Film physical path:</b>
"""+event_data['Item']['Path'].replace("\\", " ")+"""
<b>Video resolution:</b>
"""+str(event_data['Item']['Width'])+"""x"""+str(event_data['Item']['Height'])+"""
<b>Watch link:</b>
<a href='"""+server_watch+"'>Emby</a>"
       body = {"chat_id":chat_id, "photo":emby_url+"/Items/"+event_data['Item']['Id']+"/Images/Primary", "caption": multiline_str, "parse_mode": "html"}   
     except:
          body = {"chat_id":chat_id, "photo":"https://emby.media/resources/shutterstock_1434923111.jpg", "caption": "New element \n"+event_data['Title']}
   y = requests.post(urls, json = body)
   return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18000, debug=True)
