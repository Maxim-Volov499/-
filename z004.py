import pandas as pd
 from faker import Faker
 import random
 fake = Faker()
 num_entries = 100  
 categories = ['Категория 1', 'Категория 2', 'Категория 3']
 data = {
     'ID': [i for i in range(1, num_entries + 1)],
     'Имя': [fake.name() for _ in range(num_entries)],
     'Email': [fake.email() for _ in range(num_entries)],
     'Возраст': [random.randint(18, 65) for _ in range(num_entries)],
     'Категория': [random.choice(categories) for _ in range(num_entries)]
 }
 df = pd.DataFrame(data)
 df.to_csv('synthetic_data.csv', index=False)
 print(df.head())