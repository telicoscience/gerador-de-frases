from fasthtml.common import *
import requests 
app, rt = fast_app(hdrs=(picolink))
from googletrans import Translator

# Função para traduzir do inglês para o português
def traduzir_para_portugues(texto_ingles):
    # Inicializa o tradutor
    tradutor = Translator()
    
    # Traduz do inglês para o português
    traducao = tradutor.translate(texto_ingles, src='en', dest='pt')
    
    # Retorna o texto traduzido
    return traducao.text


url = "https://api.adviceslip.com/advice"
response = requests.get(url)
data = response.json()

@rt("/")
def get():
    return (
      
        Container(
            Card(
                Group(
                    P(
                        traduzir_para_portugues(data['slip']['advice'])
                    ),
                ),
                header=(Titled("Gerador de frases")),
                footer=(
                    P(                    )
                ),
            ),
        ),
    )


serve()
