from parsel import Selector
from lxml import html
from utils import xpath_file

file="xpaths.json"
XPATHS=xpath_file(file)

def parser(text):
    tree = html.fromstring(text)
    sizes_path = tree.xpath(XPATHS["sizes_path"])
    discount_path = tree.xpath(XPATHS["discount_path"])
    brands_path = tree.xpath(XPATHS["brands_path"])

    sizes = sorted(set(sizes_path),key=int)
    discounts = sorted(set(discount_path))
    brands = sorted(set(b.strip() for b in brands_path if b.strip()))

    base_url="https://www.bata.com/in/men/shoes/slippers-e-flipflop"
    urls=[]
    for brand in brands:
        for size in sizes:
            for discount in discounts:
                url=f"{base_url}/{brand.replace(" ","-").lower()}/{size}/?prefn1=discountPercent&prefv1={discount.replace("%","%25").replace(" ","%20")}"
                urls.append({
                    "brand":brand,
                    "size":size,
                    "discount":discount,
                    "url":url
                })
    return urls
