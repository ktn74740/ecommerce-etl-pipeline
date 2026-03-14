
from datetime import date, timedelta
import pandas as pd
from faker import Faker

from utils.paths import get_output_path


def generate_customers(n_rows : int = 100) :
    fake = Faker()
    Faker.seed(42)
    start_date = date.today()-timedelta(730)
    records = []
    for i in range(1,n_rows+1):
        records.append(
            {
            "customer_id" : i,
            "customer_name" : fake.name(),
            "city" : fake.city(),
            "signup_date" : fake.date_between_dates(date_start=start_date,date_end=date.today())
            }
            )
    return pd.DataFrame(records)

def main() -> None :
    print("gerating customer dataset...")
    customers_df = generate_customers(n_rows = 100)
    output_path = get_output_path("customers.csv")
    customers_df.to_csv(output_path, index=False)
    print("customer dataset saved at",output_path)


if __name__ == "__main__" :
    main()

