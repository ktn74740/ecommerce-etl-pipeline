import random
from utils.paths import get_output_path
import pandas as pd

def generate_products() -> pd.DataFrame :
    random.seed(42)
    products = [
        ("Wireless Mouse", "Electronics"),
        ("Mechanical Keyboard", "Electronics"),
        ("Bluetooth Speaker", "Electronics"),
        ("USB Hub", "Electronics"),
        ("Webcam", "Electronics"),
        ("Running Shoes", "Footwear"),
        ("Sneakers", "Footwear"),
        ("Sandals", "Footwear"),
        ("Formal Shoes", "Footwear"),
        ("Slippers", "Footwear"),
        ("Backpack", "Accessories"),
        ("Wallet", "Accessories"),
        ("Water Bottle", "Accessories"),
        ("Sunglasses", "Accessories"),
        ("Cap", "Accessories"),
        ("T-Shirt", "Clothing"),
        ("Jeans", "Clothing"),
        ("Hoodie", "Clothing"),
        ("Jacket", "Clothing"),
        ("Shirt", "Clothing"),
        ("Table Lamp", "Home"),
        ("Bedsheet", "Home"),
        ("Coffee Mug", "Home"),
        ("Wall Clock", "Home"),
        ("Storage Box", "Home"),
    ]
    records = []
    product_id = 1001
    for i,(product,category) in enumerate(products) :
        price = round(random.uniform(199,499),2)
        records.append(
            {
                "product_id" : product_id + i,
                "product_name" : product,
                "category" : category,
                "price" : price
            }
        )
    return pd.DataFrame(records)

def main () -> None :
    df = generate_products()
    output_path = get_output_path("products.csv")
    df.to_csv(output_path,index=False)
    print("products dataset saved at",output_path)

if __name__ == "__main__" :
    main()



