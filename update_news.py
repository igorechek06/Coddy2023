import json
import re
from traceback import print_exc
from urllib.parse import urljoin

import bs4
import requests


def gameguru() -> list:
    news = []
    BASE_URL = "https://gameguru.ru/articles/rubrics_news/"

    for i in range(1, 4):
        soup = bs4.BeautifulSoup(
            requests.get(BASE_URL + "?page=" + str(i)).text, "html.parser"
        )

        publications = soup.select('div[id^="publication-"]')

        for pub in publications:
            title = pub.select_one("div.short-news-title a").contents[0]
            description = None
            if title == "LootGuru":
                continue
            image = urljoin(BASE_URL, pub.select_one("picture>source").attrs["srcset"])
            url = urljoin(
                BASE_URL, pub.select_one("div.short-news-title a").attrs["href"]
            )

            news.append(
                {
                    "title": title,
                    "description": description,
                    "image_url": image,
                    "page_url": url,
                    "site_name": "Gameguru",
                    "site_link": BASE_URL,
                }
            )
    return news


def igromania() -> list:
    news = []
    BASE_URL = "https://www.igromania.ru/news/"

    soup = bs4.BeautifulSoup(requests.get(BASE_URL).text, "html.parser")

    publications = soup.select('div[class="aubl_item"]')

    for pub in publications:
        title = pub.select_one("img").attrs["alt"]
        description = None
        image = pub.select_one("img").attrs["src"]
        url = urljoin(BASE_URL, pub.select_one("a[class=aubli_name]").attrs["href"])

        news.append(
            {
                "title": title,
                "description": description,
                "image_url": image,
                "page_url": url,
                "site_name": "Igromania",
                "site_link": BASE_URL,
            }
        )
    return news


def stopgame() -> list:
    news = []
    BASE_URL = "https://stopgame.ru/news"

    for i in range(1, 10):
        soup = bs4.BeautifulSoup(
            requests.get(BASE_URL + "/all/p" + str(i)).text, "html.parser"
        )

        publications = soup.select('div[class^="_card_"]')

        for pub in publications:
            title = pub.select_one('a[class^="_title_"]').contents[0]
            description = None
            image = pub.select_one("img").attrs["src"]
            url = urljoin(BASE_URL, pub.select_one('a[class^="_title_"]').attrs["href"])
            news.append(
                {
                    "title": title,
                    "description": description,
                    "image_url": image,
                    "page_url": url,
                    "site_name": "StopGame",
                    "site_link": BASE_URL,
                }
            )
    return news


def cubiq() -> list:
    news = []
    BASE_URL = "https://cubiq.ru/news/"

    for i in range(1, 10):
        soup = bs4.BeautifulSoup(
            requests.get(BASE_URL + "page/" + str(i)).text, "html.parser"
        )

        publications = soup.select("article")

        for pub in publications:
            title = pub.select_one("h2 a").contents[0]
            description = None
            image = pub.select_one("a img").attrs["data-lazy-src"]
            url = urljoin(BASE_URL, pub.select_one("h2 a").attrs["href"])
            news.append(
                {
                    "title": title,
                    "description": description,
                    "image_url": image,
                    "page_url": url,
                    "site_name": "Cubiq",
                    "site_link": BASE_URL,
                }
            )
    return news


def shazoo() -> list:
    news = []
    BASE_URL = "https://shazoo.ru/tags/419/games"

    for i in range(1, 10):
        soup = bs4.BeautifulSoup(
            requests.get(BASE_URL + "?page=" + str(i)).text, "html.parser"
        )

        publications = soup.select('div[class="flex flex-col gap-2 py-6 first:pt-0"]')

        for pub in publications:
            title = pub.select_one("h4 a").contents[0]
            description = pub.select_one("div.break-words").contents[0].strip()
            image = pub.select_one('img[class="rounded"]').attrs["src"]
            url = pub.select_one("h4 a").attrs["href"]

            news.append(
                {
                    "title": title,
                    "description": description,
                    "image_url": image,
                    "page_url": url,
                    "site_name": "Shazoo",
                    "site_link": BASE_URL,
                }
            )
        return news


def goharu() -> list:
    news = []
    BASE_URL = "https://www.goha.ru/news"

    for i in range(1, 10):
        soup = bs4.BeautifulSoup(
            requests.get(BASE_URL + "?page=" + str(i)).text, "html.parser"
        )

        publications = soup.select('div[class="articles-snippets__snippet-wrapper"]')

        for pub in publications:
            title = pub.select_one(
                "a[class=article-snippet__body-title-link]"
            ).contents[0]
            description = pub.select_one(
                "span[class=article-snippet__body-shortly-label]"
            ).contents[0]
            image = pub.select_one("img[class=article-snippet__image-img]").attrs["src"]
            url = pub.select_one("a[class=article-snippet__body-title-link]").attrs[
                "href"
            ]

            news.append(
                {
                    "title": title,
                    "description": description,
                    "image_url": image,
                    "page_url": url,
                    "site_name": "Goharu",
                    "site_link": BASE_URL,
                }
            )
        return news


def kanobu() -> list:
    links = []
    j = 1
    url = "https://kanobu.ru/videogames/?page="
    while len(links) < 50:
        res = requests.get(url + str(j))
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        for i in soup.find_all("a", class_=re.compile(r"SmallTextCard_body.+")):
            links.append(i["href"])
            # print(i)
        j += 1
    url = "https://kanobu.ru"

    answ = []
    for i in links:
        res = requests.get(url + i)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        d = {}
        d["page_url"] = url + i
        d["description"] = None
        d["image_url"] = soup.find_all(
            "img",
            src=re.compile(
                r"https\:\/\/cdn\.kanobu\.ru\/articles\/pics\/tmp\/images\/.+"
            ),
        )[0]["src"]
        d["title"] = soup.find_all(
            "div", class_=re.compile("MaterialItemHead_head_left__f_.+")
        )[0].h1.text
        d["site_name"] = "Kanobu"
        d["site_link"] = "https://kanobu.ru/videogames/"

        answ.append(d)

    return answ


def ixbt_games() -> list:
    url = "https://ixbt.games/news"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    answ = []
    for i in soup.find_all("div", class_="py-2"):
        d = {}
        d["image_url"] = i.find_all_next("img")[0]["src"]
        d["page_url"] = (
            "https://ixbt.games" + i.find_all_next("a", class_="card-link")[0]["href"]
        )
        d["title"] = i.find_all_next("a", class_="card-link")[0].text.strip()
        d["description"] = i.find_all_next("div", class_="d-flex d-sm-block my-2")[
            0
        ].text.strip()
        d["site_name"] = "iXBT.games"
        d["site_link"] = "https://ixbt.games"
        answ.append(d)
    res = requests.get(soup.find_all("a", class_="page-link")[0]["href"])
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    for i in soup.find_all("div", class_="py-2"):
        d = {}
        d["image_url"] = i.find_all_next("img")[0]["src"]
        d["page_url"] = (
            "https://ixbt.games" + i.find_all_next("a", class_="card-link")[0]["href"]
        )
        d["title"] = i.find_all_next("a", class_="card-link")[0].text.strip()
        d["description"] = i.find_all_next("div", class_="d-flex d-sm-block my-2")[
            0
        ].text.strip()
        d["site_name"] = "iXBT.games"
        d["site_link"] = "https://ixbt.games"
        answ.append(d)
    return answ


def playground() -> list:
    url = "https://www.playground.ru/news?p="
    answ = []
    for i in range(1, 3):
        res = requests.get(url + str(i))
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        for j in soup.find_all("div", class_="post"):
            d = {}
            d["description"] = None
            k = j.find_all_next("img")[0]
            d["title"] = k["alt"]
            d["image_url"] = k["src"]
            d["page_url"] = urljoin(
                "https://www.playground.ru",
                j.find_all_next("a")[0]["href"],
            )
            d["site_name"] = "Playground"
            d["site_link"] = "https://www.playground.ru"
            answ.append(d)
    return answ


def kgportal() -> list:
    url = "https://kg-portal.ru/news/games/"
    answ = []
    for i in range(0, 5, 2):
        res = requests.get(url + str(i * 10))
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        for j in soup.find_all("div", class_="news_box games_cat"):
            d = {}
            k = j.find_all_next("a", class_="news_card_link")[0]
            d["page_url"] = "https://kg-portal.ru" + k["href"]
            d["title"] = k.text
            d["description"] = j.find_all_next("div", class_="news_text")[
                0
            ].text.strip()
            d["image_url"] = urljoin(
                "https://kg-portal.ru",
                j.find_all_next("div", class_="news_text")[0].find_all_next("img")[0][
                    "src"
                ],
            )
            d["site_name"] = "КГ-ПОРТАЛ"
            d["site_link"] = "https://kg-portal.ru/news/games/"
            answ.append(d)
    return answ


if __name__ == "__main__":
    done = []

    try:
        print("gameguru")
        done += gameguru()
        print("igromania")
        done += igromania()
        print("stopgame")
        done += stopgame()
        print("cubiq")
        done += cubiq()
        print("shazoo")
        done += shazoo()
        print("goharu")
        done += goharu()
        # print("kanobu")
        # done += kanobu()
        print("ixbt")
        done += ixbt_games()
        print("playground")
        done += playground()
        print("kgportal")
        done += kgportal()
    except Exception as e:
        print_exc()
    finally:
        with open("news.json", "w") as file:
            json.dump(done, file)
