import requests
from bs4 import BeautifulSoup as bs
import time


def scrape_handles(iop):
    print("scraping IOP for twitter handles...")
    n = 0
    results = []
    output = []
    while n < 5:
        if n != 0:
            time.sleep(5)  # let's be polite
        n += 1
        print(f"page {n}")
        r = requests.get(iop + f"twitter/page:{n}")
        results.append(r.text)

    for r in results:
        soup = bs(r, "lxml")  # import data
        x = soup.select(".handle")  # select only <div id=handle> tags
        x = [i.string for i in x]  # remove tags
        output = output + x

    output = list(set(output))  # deduplicate
    print("-" * 80)
    return output


def scrape_links(iop):
    print("scraping IOP for links to tweets...")
    n = 0
    results = []
    output = []
    while n < 5:
        if n != 0:
            time.sleep(5)  # let's be polite
        n += 1
        print(f"page {n}")
        r = requests.get(iop + f"twitter/page:{n}")
        results.append(r.text)

    for r in results:
        soup = bs(r, "lxml")  # import data
        x = soup.select("time")  # select only <time> tags
        for i in x:
            links = i.select("a")  # select the links within the <time tags>
            for link in links:
                output.append(link.get("href"))  # Append the link target to the list
    output = list(set(output))  # deduplicate
    print("-" * 80)
    return output


if __name__ == "__main__":
    iop = "https://iop.altmetric.com/details/5152221/"

    a = scrape_handles(iop)
    for i in a:
        print(i)

    a = scrape_links(iop)
    for i in a:
        print(i)
