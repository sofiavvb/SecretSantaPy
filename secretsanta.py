from utils import *

def main():

    while True:
        print("############################")
        print("1 - Adicionar participante\n2- Mostrar participantes\n3- Executar sorteio")
        print("############################")
        #User's choice#
        choice = get_choice()

        if choice == "1":
            get_participant()
        elif choice == "2":
            display_participants(participants)
        elif choice == "3":
            if len(participants) >= 2:
                secret_santa(participants)
                break
            else:
                print("É preciso pelo menos dois participantes no amigo secreto! Tente Novamente!")

if __name__ == "__main__":
    main()
