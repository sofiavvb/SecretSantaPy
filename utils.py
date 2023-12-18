import random
import smtplib
from email.message import EmailMessage
from config import *

#name: (email, sorteado)
participants = {}

def get_choice():
    while True:
        try:
            choice = input("Escolha o que realizar (1/2/3): ").replace(" ", "")
            if choice not in ["1", "2", "3"]:
                raise ValueError("Opção inválida! Tente novamente.\n")
            else: 
                return choice
        except ValueError as error:
                print(error)

def get_participant():
    name = input("Digite o nome: ").trim().lower()
    #ver em como garantir que o email é válido
    email = input("Digite o email: ").trim().lower()
    participants[name] = [email, None]

def display_participants(participants):
    print("------------------------------------")
    for person in participants:
        print(f"Nome: {person} - Email: {participants[person][0]}")
    print("------------------------------------")

def send_email(participante, email, amigo_secreto):
    msg = EmailMessage()
    msg['Subject'] = 'Amigo Secreto'
    msg['From'] = EMAIL_HOST
    msg['To'] = email
    msg.set_content(f'Olá {participante}! Seu amigo secreto é {amigo_secreto}! Divirta-se!')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_HOST, SENHA)
        smtp.send_message(msg)
    
    
def secret_santa(participants):
    #copia os participantes do amigo secreto
    control = list(participants.keys())

    for participante in participants:
        escolheu = False

        while not escolheu:
            aux = random.randint(0, len(control) - 1)
            sorteado = control[aux]

            if sorteado != participante and sorteado != None:
                escolheu = True
                participants[participante][1] = sorteado
                control[aux] = None

    for participante in participants:
        send_email(participante, participants[participante][0], participants[participante][1])