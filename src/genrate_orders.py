import random
import pandas as pd
from datetime import datetime,timedelta
from utils.paths import get_output_path

def weighted_hour() -> int :
    hours = list(range(24))
    weights = [
        1, 1, 1, 1, 1, 2,  # 0–5
        3, 4, 5, 6, 7, 8,  # 6–11
        8, 8, 7, 7, 8, 9,  # 12–17
        10, 10, 9, 7, 4, 2  # 18–23
    ]
    return random.choices(hours,weights = weights , k=1)[0]

def weighted_status() -> str:
    """
    Realistic order status distribution.
    """
    return random.choices(
        ["Completed", "Cancelled", "Pending"],
        weights=[80, 12, 8],
        k=1
    )[0]


def weighted_payment() -> str:
    """
    Realistic Indian ecommerce payment distribution.
    """
    return random.choices(
        ["UPI", "Card", "CashOnDelivery", "Wallet", "NetBanking"],
        weights=[45, 25, 20, 5, 5],
        k=1
    )[0]
def generate_orders(n_orders: int = 200) -> pd.DataFrame :
    random.seed(42)
    start_date = datetime.now() - timedelta(days=180)
    records = []
    order_id_start = 5001

    for i in range(n_orders):
        day_offset = random.randint(0,179)
        base_day = start_date + timedelta(days=day_offset)

        #weekend boost logic
        if base_day.weekday() >= 5 and random.random() > 0.35 :
            hour = random.choice([11, 12, 13, 18, 19, 20, 21])
        else :
            hour = weighted_hour()

        minute = random.randint(0,59)
        second = random.randint(0,59)

        order_timestamp = base_day.replace(hour = hour,minute = minute,second = second,microsecond=0)

        records.append(
            {
                "order_id" : order_id_start + i,
                "customer_id" : random.randint(1,100),
                "order_timestamp" : order_timestamp,
                "payment_mode": weighted_payment(),
                "order_status": weighted_status()
            }
        )
    return pd.DataFrame(records)

def main() -> None :
    df = generate_orders()
    output_path = get_output_path("orders.csv")
    df.to_csv(output_path,index=False)
    print("orders csv file generated successfully at",output_path)

if __name__ == "__main__" :
    main()
