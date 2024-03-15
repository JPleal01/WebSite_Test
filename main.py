#A ideia é ser um chat ao vivo, sem salvamento de mensagens

#Definir se vai usar flat ou flask - fazer dois modelos, um com flet(esse) Outro com flask
#Criar pagina 
#Criar icones da primeira pagina
    #Botão que gera caixa pra login
#Atualizar pagina de maneira que não recarregue-a inteira
#Criar conexão com a rede, de modo que estejam simuntaneas

import flet as ft

def main(pagina):
    pagina.title = "TestZap"
    texto =ft.Text("TestZap")
    pagina.add(texto)
    
    
    botao_entrar_chat= ft.ElevatedButton("Entrar no chat")

    pagina.add(botao_entrar_chat)

ft.app(target=main, view= ft.AppView.WEB_BROWSER) # Com o port = 8000 e sem o "AppView." ficou mais rapido no primeiro teste