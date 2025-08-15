from bs4 import BeautifulSoup
import pandas as pd
import re

def stitch_price_from_spans(container):
    parts = container.find_all("span", attrs={"aria-hidden": "true"})
    price_text = ''.join(span.get_text(strip=True) for span in parts)
    match = re.search(r'(\d+)(\d{2})$', price_text)
    if match:
        dollars, cents = match.groups()
        return float(f"{dollars}.{cents}")
    return None

def extract_category(card):
    current = card
    for _ in range(5):
        header = current.find_previous("h2")
        if header:
            return header.get_text(strip=True)
        current = current.find_parent("div")
    return "Uncategorized"

def parse_instacart_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    name_tags = soup.find_all("div", class_="e-xahufp")
    print(f"Found {len(name_tags)} product name tags")

    products = []

    for name_tag in name_tags:
        name = name_tag.get_text(strip=True)
        card = name_tag
        for _ in range(3):
            card = card.find_parent("div")
        if not card:
            continue

        stitched_price = card.find("span", class_="e-1ip314g")
        if not stitched_price:
            print(f"No stitched price found for: {name}")
            continue
        price = stitch_price_from_spans(stitched_price)

    
        size_tag = card.find("div", class_="e-cauxk8")
        size_text = size_tag.get_text(strip=True) if size_tag else "each"

        
        category = extract_category(card)

        products.append({
            "Product": name,
            "Price": f"${price:.2f}" if price else None,
            "Size/Weight": size_text,
            "Category": category
        })

    return pd.DataFrame(products)

if __name__ == "__main__":
    file_path = "instacart_fully_loaded.html" 
    df = parse_instacart_html(file_path)

    if df.empty:
        print("No product data found.")
    else:
        print(df.to_string(index=False))
        print(f"\n Total products scraped: {len(df)}")
    df.to_json("instacart_scraped_data_final_v1.json", orient="records", indent=2)
    print("\n Data saved to: instacart_scraped_data_final_v1.json")
    