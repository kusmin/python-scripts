import time

from tqdm import tqdm


def load():
    for _ in tqdm(range(100), desc="Loading ....", ascii=False, ncols=75):
        time.sleep(0.10)
    print("Loading Done!")


if __name__ == '__main__':
    load()
