import pandas as pd


def getAVGLength(filepath):
    total_avg = 0
    chunk_size = 100
    reader = pd.read_csv(filepath, iterator=True)
    step = 0
    chunk = reader.get_chunk(3)
    
    while step < 5:
        step += 500
        chunk = reader.get_chunk(3)
        if total_avg == 0:
            total_avg = chunk['BP'].mean()
        else:
            total_avg = (total_avg + chunk['BP'].mean()) / 2
        print('Step:', step)
        print(total_avg, '\n')
       

 




if __name__ == "__main__":
    getAVGLength("CEU.csv")