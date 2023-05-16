import requests
import json
import argparse
import sys
import time

def news(args):
    r = f'https://newsapi.org/v2/everything?q={args.x}&from=2023-04-12&sortBy=publishedAt&apiKey=b7c7a9b0544d4a1393dc758de737d379'
    r_text = requests.get(r)
    article = json.loads(r_text.text)
    for r in article['articles']:
        print(f"{r['title']}:-")
        print("")
        print(r['content'])
        print("---------------------end-----------------------")
        print("")
        time.sleep(1)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=str,default='top',help="fuck off")

    args = parser.parse_args()
    sys.stdout.write(str(news(args)))
