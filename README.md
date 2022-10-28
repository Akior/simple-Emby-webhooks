# simple Emby php webhooks for send message to client
Get webhooks from Emby, than generate api request return for push message by session_id

# Emby to telegram work with new beta version of Emby (4.8.0.15+) with new event library.new
Limitation:
Emby server trigger library.new before it fetch some metadata to file, so we dont have poster and description.
Script use sendphoto telegram api, so I cannot send photo without photo, so as alternative, I use sample picture from emby site.
