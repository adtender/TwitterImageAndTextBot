import os
import sys
import random
import tweepy
import keys

API_Key = keys.API_Key
API_Key_Secret = keys.API_Key_Secret
Access_Token = keys.Access_Token
Access_Token_Secret = keys.Access_Token_Secret

def textHandling(api, random_file): # untested

    with open(random_file, "r") as file:
        string = random.choice(file.readlines()).strip()
        if len(string) < 281:
            response = api.create_tweet(text=string)
            print(f"https://twitter.com/user/status/{response.data['id']}")
        else:
            print("Tweet too long, shorten to 280 characters or less")
            sys.exit(0)
            #If you can post longer than 280 characters change this yourself loser 

def mediaHandling(api, random_file):

    file_size = os.path.getsize(random_file)
    if os.path.splitext(random_file)[1] == ".mp4":
        if file_size < 512000000:
            print("to do")
    elif os.path.splitext(random_file)[1] == ".jpg" or os.path.splitext(random_file)[1] == ".png":
        if file_size < 5000000:
            media = api.media_upload(filename = random_file)
            response = api.update_status("", media_ids=[media.media_id])
            print(response.text)
    elif os.path.splitext(random_file)[1] == ".gif":
        if file_size < 15000000:
            return "tweet_gif"
    else:
        print("Incorrect file type of file too large (512 MB for mp4, 5 MB for png or jpg, 15 MB for gif")
    
    sys.exit(0)

def main():
    api_key = API_Key
    api_key_secret = API_Key_Secret
    access_token = Access_Token
    access_token_secret = Access_Token_Secret
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    client = tweepy.Client(consumer_key=API_Key, consumer_secret=API_Key_Secret, access_token=Access_Token, access_token_secret=Access_Token_Secret)

    random_file = "media/" + random.choice([f for f in os.listdir("media/") if os.path.isfile(os.path.join("media/", f))])

    if os.path.splitext(random_file)[1] == ".txt":
        textHandling(client, random_file)
    else:
        mediaHandling(api, random_file)

if __name__ == "__main__":
    main()
