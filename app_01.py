import requests

def fetch_page():
    url = 'https://lba.sportstrack.co/basketball/events/47/schedule'
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    page_content = fetch_page()
    print(page_content)
