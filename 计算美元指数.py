import pandas as pd

# 计算美元指数的函数
def calculate_usd_index(EURUSD, USDJPY, GBPUSD, USDCAD, USDSEK, USDCHF):
    """
    计算美元指数的Python函数
    参数说明(均为实时汇率值):
    EURUSD : 欧元对美元汇率
    USDJPY : 美元对日元汇率
    GBPUSD : 英镑对美元汇率
    USDCAD : 美元对加元汇率
    USDSEK : 美元对瑞典克朗汇率
    USDCHF : 美元对瑞士法郎汇率
    """
    constant = 50.14348112
    product = (
        (EURUSD ** (-0.576))
        * (USDJPY ** 0.136)
        * (GBPUSD ** (-0.119))
        * (USDCAD ** 0.091)
        * (USDSEK ** 0.042)
        * (USDCHF ** 0.036)
    )
    usd_index = constant * product
    return round(usd_index, 4)

# 读取CSV文件并计算美元指数
def read_currency_data_and_calculate_index():
    # 读取CSV文件
    data = pd.read_csv('currency_data2.csv')
    # 初始化一个空的列表来存储计算结果
    results = []

    # 遍历数据行
    for index, row in data.iterrows():
        # 从每行数据中提取汇率
        EURUSD = row['EUR']
        USDJPY = row['JPY']
        GBPUSD = row['GBP']
        USDCAD = row['CAD']
        USDSEK = row['SEK']
        USDCHF = row['CHF']

        # 计算美元指数
        usd_index = calculate_usd_index(EURUSD, USDJPY, GBPUSD, USDCAD, USDSEK, USDCHF)
        results.append(usd_index)

    # 将结果添加到数据框中
    data['USD_Index'] = results
    # 输出结果到文件
    data[['date', 'USD_Index']].to_csv('usd_index_results.csv', index=False)

# 调用函数
read_currency_data_and_calculate_index()