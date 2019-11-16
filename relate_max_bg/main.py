import pandas as pd
import matplotlib.pyplot as plt
    
def getMAXLength(filepath):
    max_bp_per_window = []
    chunk_size = 10000
    reader = pd.read_csv(filepath, iterator=True)
    step = 500
    i = 0
    while i < 1000:
        try:
            chunk = reader.get_chunk(chunk_size)
            reader.get_chunk(step) # skip step size
            max_bp_per_window.append(chunk['BP'].max())
            i = i + 1
        except:
            return list(range(i)), max_bp_per_window
      
       

if __name__ == "__main__":
    x, y = getMAXLength("CEU.csv")
    hl, = plt.plot(x, [x / 100000 for x in y])
    plt.show()