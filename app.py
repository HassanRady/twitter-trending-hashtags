import json
import uvicorn
from fastapi import FastAPI
from main import Tweets


tweets = Tweets()
app = FastAPI()


@app.get("/trending_hashtags")
async def get_trending_hashtags(WOEID=1):
    trends = tweets.get_trending_hashtags(WOEID)
    return json.dumps(trends[0]['trends'])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9093)