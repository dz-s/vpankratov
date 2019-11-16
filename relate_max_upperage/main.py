import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# def roll_max_age(filepath):
#     max_upper_age_per_window = []
#     chunk_size = 10000
#     reader = pd.read_csv(filepath, iterator=True)
#     step = 500
#     i = 0
#     while i < 1000:
#         try:
#             chunk = reader.get_chunk(chunk_size)
#             reader.get_chunk(step) # skip step size
#             max_upper_age_per_window.append(chunk['BP'].max())
#             i = i + 1
#         except:
#             return list(range(i)), max_upper_age_per_window

if __name__ == "__main__":
    max_bp_per_window = []
    chunk_size = 10000
    df = pd.read_csv("../data/CEU.csv")
    bp = list(df['BP'])  
    spots = np.arange(bp[0], bp[-1], 500)
    upper_age = []
    i = 0
    plt.ion()
    plt.show()
    for spot in spots:
        i = i + 1
        print('Spot: ', i)
        upper_age.append((df.loc[df['BP'] <= spot+10000]).loc[df['BP'] >=  spot]['upper_age'].max())

        plt.plot(spots[:i], upper_age)
        plt.draw()
        plt.pause(0.01)
    
