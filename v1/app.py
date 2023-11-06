import csv
import time
import requests

class Organizador():

    def __init__(self, name):
        self.name = name
        self.nomes = [] 

    def leitorNome(self):
        
        print("Seja bem-vindo ao Organizador!\nEstou aqui para ajudar você a organizar as pastas em ordem alfabética.")
        print()
        print("------------------------------------------------------------------------------------------")
        
        n = int(input("Por favor, digite quantos nomes deseja inserir para ser organizados: "))
        
        print()
        print("------------------------------------------------------------------------------------------")
        
        for _ in range(n):
            nome = input("Digite o nome: ")
            self.nomes.append(nome)
        
        print()
        print("------------------------------------------------------------------------------------------")
    
    def nomesOrganizados(self):

        self.nomes.sort()
        print("Nomes organizados em ordem alfabética: ")

        for nome in self.nomes:
            print(nome)
    
    def csvNomes(self):
        
        try:
            with open('nomes.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nomes"])
                for nome in self.nomes:
                    writer.writerow([nome])
            print()
            print("------------------------------------------------------------------------------------------")
            print("Arquivo CSV 'nomes.csv' criado com sucesso.")

        except Exception as e:
            print()
            print("------------------------------------------------------------------------------------------")
            print(f"Ocorreu um erro ao criar o arquivo CSV: {e}")
    
    def enviarNomes(self):

        print()
        print("------------------------------------------------------------------------------------------")

        # Substitua pelo token do seu bot
        bot_token = "TOKEN"
        
        # Substitua pelo chat_id do usuário ou grupo para o qual deseja enviar a mensagem
        chat_id = "CHAT_ID"
        
        # Enviar a lista de nomes para o bot no Telegram
        mensagem1 = "Olá!\nSegue a lista de nomes em ordem alfabética: "
        mensagem2 = "\n".join(self.nomes)
        mensagem_completa = mensagem1 + mensagem2

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        params = {"chat_id": chat_id, "text": mensagem_completa}
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            print("Lista de nomes enviada para o Telegram com sucesso.")
        else:
            print(f"Erro ao enviar a mensagem: {response.text}")
        
        


organizar = Organizador("Minha organização")
organizar.leitorNome()
organizar.nomesOrganizados()
organizar.csvNomes()
organizar.enviarNomes()