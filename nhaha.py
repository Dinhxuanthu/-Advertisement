import pandas as pd
import numpy as np
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Advertising.csv'
data = pd.read_csv(url)
data = data.drop(columns=['Unnamed: 0'])


# Tính hiệp phương sai giữa hai cột TV và Sales
cov_matrix = np.cov(data['TV'], data['sales'])

print("Ma trận hiệp phương sai giữa TV và Sales:\n", cov_matrix)
tv = data['TV']
radio = data['radio']
thu=pd.concat([tv,radio],axis='columns')
newspaper = data['newspaper']
sales = data['sales']

correlation = thu.corr()
print("Ma trận tương quan:\n", correlation)

print("Phương sai của cột TV:", tv.var())
print("Phương sai của cột Radio:", radio.var())
print("Phương sai của cột Newspaper:",newspaper.var())
print("Phương sai của cột Sales:", sales.var())