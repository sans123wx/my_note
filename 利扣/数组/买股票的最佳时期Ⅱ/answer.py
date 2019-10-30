while True:
    prices_str = input('请输入每日股票价格，以空格隔开：')
    prices_temp = prices_str.split(' ')
    prices = []
    try:
        for e in prices_temp:
            prices.append(int(e))
    except:
        print('请输入每日价格，必须为数字')
    else:
        break
maxpro = 0
temp = 0 
for i in range(1 , len(prices)):
    temp = prices[i] - prices[i - 1]
    if temp > 0:
        maxpro += temp
print(maxpro)

