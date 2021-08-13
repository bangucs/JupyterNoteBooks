import pandas as pd
import numpy as np

n = input("Please input number of players:")
scores = input("please input scores:")

def showResult(n, scores):
    players = int(n)    
    df = pd.DataFrame({'n': np.arange(1,players+1,1),
                      'scores': scores.split(' ')})
    df_sorted = df.sort_values('scores')
    df_sorted = df_sorted.reset_index()
    print(df_sorted.iloc[players-2, 1])

showResult(n, scores)