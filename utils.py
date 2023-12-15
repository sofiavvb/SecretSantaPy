#name: email
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
    participants[name] = email

def display_participants(participants):
    for person in participants:
        print(f"Nome: {person} - Email: {participants[person]}")

def secret_santa(participants):
    pass