import requests
from bs4 import BeautifulSoup as bs
import time


def scrape(iop):
    n = 0
    results = []
    output = []
    while n < 5:
        time.sleep(5)  # let's be polite
        n = n + 1
        print(f"page {n}")
        r = requests.get(iop + f"twitter/page:{n}")
        results.append(r.text)

    for r in results:
        soup = bs(r, "lxml")  # import data
        x = soup.select(".handle")  # select only <div id=handle> tags
        x = [i.string for i in x]  # remove tags
        output = output + x

    output = list(set(output))  # deduplicate
    return output


if __name__ == "__main__":
    iop = "https://iop.altmetric.com/details/5152221/"
    print(scrape(iop))
