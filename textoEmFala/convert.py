import pyttsx3

# Carregando a lib
engine = pyttsx3.init()

# texto que vai ser reproduziso
engine.say('Olá, como você esta ?')
engine.say('Em qual linguagem você programa ?')

# executa

engine.runAndWait()
