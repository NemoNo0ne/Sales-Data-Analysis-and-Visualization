import pandas as pd

data = {
    'date': ['2023-10-01', '2023-10-02', '2023-10-03'],  # Даты продаж
    'product_id': [101, 102, 103],  # Идентификаторы продуктов
    'quantity': [3, 5, 2],  # Количество проданных единиц для каждого продукта
    'revenue': [300, 500, 200]  # Выручка от продажи каждого продукта
}

# DataFrame
df = pd.DataFrame(data)

# CSV
df.to_csv('sales_data.csv', index=False)
