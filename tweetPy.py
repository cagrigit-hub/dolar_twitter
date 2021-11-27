import time
import requests
import tweepy
import ast
consumer_key= "I1rLPe2WTnlRzd0qgk9VtdSys"
consumer_secret ="nL8mydCBBWuZf4I0BE2xPxU1WZJfntpcSybjmSNGXyrjqeMp5L"
access_token = "1298987475839250435-p96bODsu1lLaBhqzFSbg128RQvmuL0"
access_token_secret = "wTwg6YQBwYPq8G1wtwQYoK30qZul8yk7cqJ46yFnVOuqx"


bearer_token = "AAAAAAAAAAAAAAAAAAAAAGqOWAEAAAAAcXIGafBWn%2F86JEXnVmpqfe0H%2B%2FE%3Dx2MJJ6brj0LAIpxIgn32nY1o8HM9VhddBck0VMRGmFUSWqGUS7"
client = tweepy.Client(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret)

ids ={}
def create_url():

    user_id = 1298987475839250435
    return "https://api.twitter.com/2/users/{}/mentions".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserMentionsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    time.sleep(12)
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    
    
    
    for mention in json_response["data"]:
        if mention["text"] == '@cagrkutyok !dolar':
            dlr = requests.request("GET","https://api.fastforex.io/fetch-one?from=USD&to=TRY&api_key=c24eed3a02-0f52d1575e-r31t7h")
            clean = dlr.content.decode("utf-8")
            clean = ast.literal_eval(clean)
            if ids.get(mention["id"])== None:
                client.create_tweet(in_reply_to_tweet_id=mention["id"],text=str(clean["result"]["TRY"]))
            ids[mention["id"]] = 1
        elif mention["text"] == '@cagrkutyok !euro':
            euro = requests.request("GET","https://api.fastforex.io/fetch-one?from=EUR&to=TRY&api_key=c24eed3a02-0f52d1575e-r31t7h")
            clean = euro.content.decode("utf-8")
            clean = ast.literal_eval(clean)
            if ids.get(mention["id"])== None:
                client.create_tweet(in_reply_to_tweet_id=mention["id"],text=str(clean["result"]["TRY"]))
            ids[mention["id"]] = 1
        elif mention["text"] == '@cagrkutyok !sterlin':
            sterlin = requests.request("GET","https://api.fastforex.io/fetch-one?from=GBP&to=TRY&api_key=c24eed3a02-0f52d1575e-r31t7h")
            clean = sterlin.content.decode("utf-8")
            clean = ast.literal_eval(clean)
            if ids.get(mention["id"])== None:
                client.create_tweet(in_reply_to_tweet_id=mention["id"],text=str(clean["result"]["TRY"]))
            ids[mention["id"]] = 1


if __name__ == "__main__":
    while True:
        main()


#user_id = 1298987475839250435
