import time 
from tqdm import tqdm

def loading():
    for _ in tqdm(range(100), desc='Loading...', ascii=False,ncols=100):
        time.sleep(0.1)
    print('Loading Done!!!')


if __name__=='__main__':
    loading()    