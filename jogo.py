from funcao import user, mostraCar, mostraMini, text_objects,message_display, batida_car, escrevePlacar, game_loop
if __name__ == "__main__":
    nome = user()
    arquivo = open("emails.txt","r")
    emails = arquivo.readlines()
    emails.append(nome)
    emails.append("\n")
    arquivo = open("emails.txt","w")
    arquivo.writelines(emails)

    arquivo = open("emails.txt","r")
    texto = arquivo.readlines()
    for line in texto:
        print(line)
    arquivo.close()
game_loop()
