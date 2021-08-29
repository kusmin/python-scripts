import email
import imaplib

EMAIL = "email"
PASSWORD = "senha"
SERVER = "imap.gmail.com"

# Monta a conexão
mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')
status, data = mail.search(None, 'ALL')
mail_ids = []

for block in data:
    mail_ids += block.split()
