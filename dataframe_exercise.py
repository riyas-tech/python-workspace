import pandas as pd

clothes = pd.DataFrame({'type': ['pants', 'shirt', 'shirt', 'pants', 'shirt', 'pants'],
                       'color': ['red', 'blue', 'green', 'blue', 'green', 'red'],
                       'price_usd': [20, 35, 50, 40, 100, 75],
                       'mass_g': [125, 440, 680, 200, 395, 485]})

print(clothes)

grouped = clothes.groupby('type')
print(grouped)
print(grouped.mean('price_usd'))

print(clothes.groupby(['type', 'color']).min())

# Aggregations
print(clothes[['price_usd', 'mass_g']].agg(['sum', 'mean']))