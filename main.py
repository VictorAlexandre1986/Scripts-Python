#pip install googlesearch-python
from googlesearch import search

query='terra'

result= list(
    search(
        query,
        lang='pt-br',
        num_results=5
)
)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
