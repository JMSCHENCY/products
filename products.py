products = []
print('鍵入"q"結束輸入 ')
count = 0
while True:
    count += 1
    name = input('請輸入第 ' + str(count) + ' 項商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入第 ' + str(count) + ' 項商品價格： ')
    products.append([name, price])
#   p = []
#   p.append(name)
#   p.append(price)
#   products.append(p)

print(products)

for p in products:
    print(p[0], '的價格是', p[1])

# 下方為分別存為txt與csv檔案格式
with open('products.txt', 'w', encoding='utf-8') as f:
    for p in products:
        f.write('商品名稱：' + p[0] + ', ' '價格：' +p[1] + '元' + '\n')

with open('products.csv', 'w', encoding='utf-8') as f:
    for p in products:
        f.write('商品名稱：' + p[0] + ', ' '價格：' +p[1] + '元' + '\n')

# with open('products.csv', 'w') as f:
#     for p in products:
#         f.write('商品名稱：' + p[0] + ', ' '價格：' +p[1] + '元' + '\n')

# line36 & 41：增加檔案顯示的標題欄位，故將line24 & 28簡化成line38 & 43
with open('products2.txt', 'w', encoding='utf-8') as f:
    f.write('商品名稱,商品價格\n')
    for p in products:
        f.write(p[0] + ', ' +p[1] + '\n')

with open('products2.csv', 'w', encoding='utf-8') as f:
    f.write('商品名稱,商品價格\n')
    for p in products:
        f.write(p[0] + ', ' +p[1] + '\n')