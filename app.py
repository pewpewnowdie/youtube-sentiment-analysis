from utils.sentiment_analysis import predict
from utils.youtube_scraper import get_comments

comments = get_comments('https://www.youtube.com/watch?v=Jx4YfRxhGmo&ab_channel=WestJett')
for comment in comments:
    print(comment, predict(comment))