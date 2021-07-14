products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

for p in products: # p = [name, price]
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f: # utf-8 為最廣泛使用的編碼
	f.write('商品,價格\n') # 加入欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # f.write:真正寫入檔案
							# 由於price先前已被轉成數字(行7)，須於此處轉為字串
							# 方可使用 "+"


# (行14) 設定編碼後，到excel點選 資料 - 取得資料 - 從檔案\從文字 - 匯入檔案 -
# 檔案原點欄位設定為utf-8, 分隔符號設定為逗號, 並載入即完成