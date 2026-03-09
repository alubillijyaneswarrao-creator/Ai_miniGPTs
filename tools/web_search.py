import requests


def web_search(query):

    url = "https://api.duckduckgo.com/"

    params = {
        "q": query,
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = []

    if "RelatedTopics" in data:
        for topic in data["RelatedTopics"]:

            if isinstance(topic, dict) and "Text" in topic:
                results.append(topic["Text"])

            if len(results) >= 5:
                break

    return results