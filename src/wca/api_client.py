import requests

def fetch_competitor_data(wca_id: str) -> dict:
    """
    Competition results for a person identified by their WCA.

    Args:
        wca_id (str): WCA ID.

    Returns:
        dict: Competition results.

    Notes:
        Data are fetched from unofficial WCA API.
    """
    url: str = "https://raw.githubusercontent.com/robiningelbrecht/wca-rest-api/master/api/persons/{}.json"
    url_to_fetch: str = url.format(wca_id.upper())

    response = requests.get(url_to_fetch)

    if response.status_code == 200:
        return response.json()
    else:
        return None

