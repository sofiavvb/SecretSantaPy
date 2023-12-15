import random

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
    name = input("Digite o nome: ").replace(" ", "").lower()
    #ver em como garantir que o email é válido
    email = input("Digite o email: ").replace(" ", "").lower()
    participants[name] = email, None

def display_participants(participants):
    print("------------------------------------")
    for person in participants:
        print(f"Nome: {person} - Email: {participants[person][0]}")
    print("------------------------------------")

def secret_santa(participants):
    control = []
    i = 0
    #copia os participantes para uma lista de controle
    for participante in participants:
        control[i] = participante
        i += 1
    
    for participante in participants:
        escolheu = False
        aux = random.randint(0, len(control) - 1)

        while not escolheu:
            sorteado = control[aux]

            if sorteado != participante and sorteado != 0:
                escolheu = True
                participants[participante][1] = sorteado
    