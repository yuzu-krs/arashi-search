import requests

def get_live_streams(api_key, search_query, exclude_keywords=[]):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "eventType": "live",
        "q": search_query,
        "type": "video",
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    live_streams = []
    for item in data["items"]:
        title = item["snippet"]["title"]
        if not any(keyword.lower() in title.lower() for keyword in exclude_keywords):
            live_streams.append({
                "title": title,
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            })
    
    return live_streams

if __name__ == "__main__":
    api_key = "個人のAPIキーを使用してください"
    search_query = "マイクラ参加型初見さん大歓迎（統合版）"
    exclude_keywords = []
    
    live_streams = get_live_streams(api_key, search_query, exclude_keywords)
    
    for stream in live_streams:
        print(f"Title: {stream['title']}")
        print(f"URL: {stream['url']}")
        print()