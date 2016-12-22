import facebook
import twython

def main():
  #---| Facebook's access codes |---#
  # Sidenote: These codes run the risk of expiration.
  
  cfg = {
    "page_id"      : "page id", 
    "access_token" : "access token" +
                     "(token cont)" +
                     "(token cont)" +
                     "(token cont)" +
                     "(token cont)" +
                     "(token cont)"
    }
	
  #---| Twitter's access codes |---#
  
  twitter = twython.Twython (
    "app id",
    "app id secret",
    "consumer id",
    "consumer id secret"
  )
  #---| User welcome and input |---#

  print("Welcome to a Python script that currently posts to Twitter & Facebook.")
  print("\tIn Progress: Instagram\n")

  msg = input("Enter post's text: ")
  imag = input("Enter image's filename: ")

  print("\nPlease wait.. Uploading images.. (Takes a few minutes!)\n")

  #---| End User Input |---#
  
  api = get_api(cfg)
  photo = open(imag, 'rb')

  image_ids = twitter.upload_media(media=photo)

  #---| Twitter posting script |---#
  twitter.update_status(
    status=msg, media_ids=image_ids['media_id']
  )

  #---| Facebook posting script |---#
  api.put_photo(image=open(imag, 'rb'), album_path= 'me' + '/photos', message=msg)

  print("Upload was successful!")
  input("Press <AnyKey> to close window..")
  
  photo.close()
def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph

if __name__ == "__main__":
  main()
