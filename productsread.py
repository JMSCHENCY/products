# 讀取檔案
products = []
with open('products2.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品名稱,商品價格' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])

print(products)