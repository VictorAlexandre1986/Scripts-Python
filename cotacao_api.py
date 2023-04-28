import requests


class Cambio():
    
    def __init__(self):
        self.url = "https://economia.awesomeapi.com.br/last/"
    
    
    def get_value_dollar_api(self):
        requesicao =  requests.get(self.url+"USD-BRL")
        requesicao_dic = requesicao.json()
        cotacao_dolar = requesicao_dic["USDBRL"]["bid"]
        return cotacao_dolar
        
        
    def get_value_euro_api(self):
        requesicao =  requests.get(self.url+"EUR-BRL")
        requesicao_dic = requesicao.json()
        cotacao_euro = requesicao_dic["EURBRL"]["bid"]
        return cotacao_euro
                
if  __name__ == "__main__":
    obj = Cambio()
    valor = obj.get_value_euro_api()
    print(valor)
                