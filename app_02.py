from requests_html import HTMLSession
from bs4 import BeautifulSoup
import lxml


session = HTMLSession()
r = session.get("https://lba.sportstrack.co/basketball/events/47/schedule?season_id=152")
r.html.render()
# page_content = BeautifulSoup(r.html.html, "html.parser")

print(r.html.html)