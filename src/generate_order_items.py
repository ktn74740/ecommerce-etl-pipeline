import random
import pandas as pd
from utils.paths import get_output_path


def generate_order_items() -> pd.DataFrame :

    random.seed(42)
    products = pd.read_csv(get_output_path("products.csv"))
    orders = pd.read_csv(get_output_path("orders.csv"))

    records =[]
    order_item_id = 9001

    for order_id in orders["order_id"] :
        n_items = random.randint(1,4)
        chosen_products = products.sample(n_items)

        for _,product in chosen_products.iterrows() :
            quantity = random.randint(1,3)

            records.append(
                {
                    "order_item_id" : order_item_id,
                    "order_id" : order_id,
                    "product_id" : product["product_id"],
                    "quantity" : quantity,
                    "unit_price" : product["price"]
                }
            )
            order_item_id += 1
    return pd.DataFrame(records)

def main():
    df = generate_order_items()
    output_path = get_output_path("order_items.csv")
    df.to_csv(output_path,index=False)
    print("order items saved at",output_path)

if __name__ == "__main__" :
    main()

