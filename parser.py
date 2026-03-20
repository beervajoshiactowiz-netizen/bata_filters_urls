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
    colors_paths=tree.xpath(XPATHS["colors_path"])

    sizes = sorted(set(sizes_path),key=int)
    discounts = sorted(set(discount_path))
    brands = sorted(set(b.strip() for b in brands_path if b.strip()))
    colors=sorted(set(colors_paths))

    base_url="https://www.bata.com/in/men/shoes/slippers-e-flipflop"
    urls=[]
    for brand in brands:
        for color in colors:
            for size in sizes:
                for discount in discounts:
                    url=f"{base_url}/{brand.replace(" ","-").lower()}/{color.replace(" ","-").lower()}/{size}/?prefn1=discountPercent&prefv1={discount.replace("%","%25").replace(" ","%20")}"
                    urls.append({
                        "brand":brand,
                        "color":color,
                        "size":size,
                        "discount":discount,
                        "url":url
                    })
    return urls
