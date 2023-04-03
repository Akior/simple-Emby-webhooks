from flask import Flask,request,json
import requests

bot_id="botXXXXXXXXXXXXXXXXXXXXXXXX"
urls="https://api.telegram.org/"+bot_id+"/sendPhoto"
chat_id=-XXXXXXXXXXXX
server="http://XXXX.XXXX.com"

app = Flask(__name__)

@app.route('/emby', methods=['POST'])
def index():
def index():
   event_data = json.loads(request.form.get('data', {}))
   if 'Item' in event_data:
      if 'Type' in event_data['Item']:
         if ( event_data['Item']['Type'] == 'Episode' ):
#check\get series
            if "SeriesId" in event_data['Item']:
               if 'Overview' in event_data['Item']:
                  body = {"chat_id":chat_id, "photo":server+"/Items/"+event_data['Item']['SeriesId']+"/Images/Primary", "caption": "New series\n"+event_data['Item']['SortName']+"\nDescription:\n"+event_data['Item']['Overview']+"\nWatch:\n"+"<a href='"+server+"/web/index.html#!/item?id="+str(event_data['Item']['Id'])+"&serverId="+event_data['Item']['ServerId']+"'>Emby</a>", "parse_mode": "html"}
               else:
                  body = {"chat_id":chat_id, "photo":"https://emby.media/resources/shutterstock_1434923111.jpg", "caption": "New series\n"+event_data['Item']['SortName']+"\nWatch:\n"+"<a href='"+server+"/web/index.html#!/item?id="+str(event_data['Item']['Id'])+"&serverId="+event_data['Item']['ServerId']+"'>Emby</a>", "parse_mode": "html"}
            else:
               print("Key SeriesId doesn't exist in JSON data event_data['Item']")
#check\get movies
         elif ( event_data['Item']['Type'] == 'Movie' ):
            if 'ExternalUrls' in event_data['Item']:
               dbs=""
               trailers=""
               for x in event_data['Item']['ExternalUrls']:
                  keys = x.keys()
                  dbs=dbs+"<a href='"+x['Url']+"'>"+x['Name']+"</a>\n"
               size = len(dbs)
               dbs=dbs[:size - 1]
            else:
               print("Key ExternalUrls doesn't exist in JSON data event_data['Item']")
            if 'RemoteTrailers' in event_data['Item']:
               for y in event_data['Item']['RemoteTrailers']:
                  keys = y.keys()
                  trailers=trailers+y['Url']+"\n"
               size = len(trailers)
               trailers=trailers[:size - 1]
            else:
               print("Key RemoteTrailers doesn't exist in JSON data event_data['Item']")
            if 'Id' in event_data['Item']:
               if 'ServerId' in event_data['Item']:
                  server_watch=server+"/web/index.html#!/item?id="+str(event_data['Item']['Id'])+"&serverId="+event_data['Item']['ServerId']
               else:
                  print("Key ServerId doesn't exist in JSON data event_data['Item']")
            else:
               print("Key Id doesn't exist in JSON data event_data['Item']")
            multiline_str= """<b>On Server:</b>
"""+event_data['Server']['Name']
            if 'SortName' in event_data['Item']:
               multiline_str=multiline_str+"""
<b>New movie:</b>
"""+event_data['Item']['SortName']
            else:
               print("Key SortName doesn't exist in JSON data event_data['Item']")
            if 'Genres' in event_data['Item']:
               multiline_str=multiline_str+"""
<b>Genre:</b>
"""+', '.join(event_data['Item']['Genres'])
            else:
               print("Key Genres doesn't exist in JSON data event_data['Item']")
            if 'Overview' in event_data['Item']:
               multiline_str=multiline_str+"""
<b>Description:</b>
"""+event_data['Item']['Overview'][:300]
            else:
               print("Key Overview doesn't exist in JSON data event_data['Item']")
            if 'CommunityRating' in event_data['Item']:
               multiline_str=multiline_str+"""
<b>Ratings:</b> """+str(event_data['Item']['CommunityRating'])
            else:
               print("Key CommunityRating doesn't exist in JSON data event_data['Item']")
            if 'ProductionYear' in event_data['Item']:
               multiline_str=multiline_str+"""
<b>Year</b>: """+str(event_data['Item']['ProductionYear'])
            else:
               print("Key ProductionYear doesn't exist in JSON data event_data['Item']")
            if 'Width' in event_data['Item']:
               multiline_str=multiline_str+"""
<b>Resolution:</b> """+str(event_data['Item']['Width'])+"x"+str(event_data['Item']['Height'])
            else:
               print("Key Width doesn't exist in JSON data event_data['Item']")
            multiline_str=multiline_str+"""
<b>External db:</b>
"""+dbs+"""
<b>Trailers:</b>
"""+trailers
            if 'Path' in event_data['Item']:
               multiline_str=multiline_str+"""
<b>Path:</b>
"""+event_data['Item']['Path'].replace("\\", "-")
            else:
               print("Key Path doesn't exist in JSON data event_data['Item']")
            multiline_str=multiline_str+"""
<b>Watch:</b>
<a href='"""+server_watch+"'>Emby</a>"
            if 'Id' in event_data['Item']:
               body = {"chat_id":chat_id, "photo":server+"/Items/"+event_data['Item']['Id']+"/Images/Primary", "caption": multiline_str, "parse_mode": "html"}
            else:
               body = {"chat_id":chat_id, "photo":"https://emby.media/resources/shutterstock_1434923111.jpg", "caption": "Новый фильм\n"+event_data['Title']+"\nПуть:\n"+event_data['Item']['Path'].replace("\\", " ")}
         else:
            print("Not a part of episode or movie")
      else:
         print("Key Type doesn't exist in JSON data event_data['Item']")
      time.sleep(3)
      y = requests.post(urls, json = body)
   else:
      print("Key Item doesn't exist in JSON data event_data")
   return ''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18000, debug=True)
