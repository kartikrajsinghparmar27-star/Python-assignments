#Lets talk about Pandas
#Lets not talk but code
import numpy as np
import pandas as pd
marks = pd.Series(np.random.randint(1,12,10))
print(marks.index)
print(marks[0])
print(marks[marks > 6])
print(marks.std())
print(marks.mean())
print(marks.median())
print(marks.max())
print(marks.min())