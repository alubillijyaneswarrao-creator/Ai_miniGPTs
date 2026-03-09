import requests

def search_web(query):
    """
    Search the web using DuckDuckGo API
    Returns top results as text list
    """

    url = "https://api.duckduckgo.com/"

    params = {
        "q": query,
        "format": "json",
        "no_redirect": 1,
        "skip_disambig": 1
    }

    response = requests.get(url, params=params)

    data = response.json()

    results = []

    # Extract related topics
    if "RelatedTopics" in data:
        for topic in data["RelatedTopics"]:

            if isinstance(topic, dict) and "Text" in topic:
                results.append(topic["Text"])

            if len(results) >= 5:
                break

    return results