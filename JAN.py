import requests
import re
from bs4 import BeautifulSoup

def search(jan_code):
    res = requests.post("https://www.janken.jp/gadgets/jan/JanSyohinKensaku.php", data={"dummy":"", "jan": jan_code})
    html = BeautifulSoup(res.content, "lxml")
    status_code=res.status_code
    try:
        product_name = re.sub(r"[\n ]", "", html.find("a", attrs={"title": "商品紹介ページを開く"}).text)
        product_company = html.find("a", attrs={"title": "メーカのホームページを開く"}).text.replace("\n", "")
    except:
        return {"status_code": status_code}
    return {"product":{"name":product_name, "company":product_company}, "status_code": status_code}