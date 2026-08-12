prof = [{
    "cod": "001",
    "nome": "Prof Thiago Paes"
}, {
    "cod": "002",
    "nome": "Prof Schalata"
}, {
    "cod": "003",
    "nome": "Prof Ignácio"
}, {
    "cod": "004",
    "nome": "Prof Ryan"
}, {
    "cod": "005",
    "nome": "Prof André"
}, {
    "cod": "006",
    "nome": "Profª Fabiana"
}, {
    "cod": "007",
    "nome": "Prof Alberto"
}, {
    "cod": "008",
    "nome": "Prof Juliano"
}, {
    "cod": "009",
    "nome": "Prof Thiago Waltrik"
}, {
    "cod": "010",
    "nome": "Prof João Eduardo"
}]

acesso = [{
    "lab": "Lab102",
    "profs": ["Prof Ignácio", "Prof Thiago Paes", "Prof Ryan", "Prof André", "Profª Fabiana"]
}, {
    "lab": "Lab103",
    "profs": ["Prof Alberto"]
}, {
    "lab": "Lab104",
    "profs": ["Prof Ryan", "Prof Juliano", "Prof Schalata", "Prof André"]
}, {
    "lab": "Lab105",
    "profs": ["Prof Ignácio", "Prof Alberto", "Prof Thiago Waltrik", "Prof Thiago Paes"]
}, {
    "lab": "Lab106",
    "profs": ["Prof Schalata", "Prof Ignácio", "Prof Thiago Waltrik", "Prof Thiago Paes"]
}, {
    "lab": "Lab107",
    "profs": ["Prof André", "Prof Schalata", "Prof Thiago Waltrik", "Prof Thiago Paes", "Prof João Eduardo"]
}]

opcao_escolhida = -1
while opcao_escolhida != 0:
    print("""Menu
        ----
        1 – Cadastrar professor;
        2 - Excluir professor;
        3 - Alterar professor;
        4 - Listar professores;
        5 - Labs: Adicionar profs;
        6 - Labs: Excluir profs;
        7 - Labs: Alterar profs;
        8 - Listar Laboratórios;
        0 - Sair.""")
    opcao_escolhida = int(input("Digite sua opcão: "))

    if opcao_escolhida == 1:
        print("Cadastrar")
        nome = input("Digite o nome do(a) professor(a):  ")
        cod = (input("Digite o código do(a) professor(a):  "))
        prof.append({
            "nome": nome, 
            "cod": cod,
        })

    elif opcao_escolhida == 2:
        print("Excluir")
        
        ######### Listar #########
        i = 0
        while i<len(prof):
            print(f'Código:{prof[i]["cod"]} - {prof[i]["nome"]}')
            i+=1
        #########################
        
        codigo_ser_procurado = input("Quem você deseja excluir? (informe o código) ")
        
        indice = 0
        while indice < len(prof):
            if prof[indice]["cod"] == codigo_ser_procurado:
                break
            indice+=1

        prof.pop(indice)

        print("Professor deletado com sucesso!")

    elif opcao_escolhida == 3:
        print("Alterar")
        i = 0
        while i<len(prof):
            print(f'Código:{prof[i]["cod"]} - {prof[i]["nome"]}')
            i+=1
        codigo_ser_procurado = input("Quem você deseja alterar? (informe o código) ")
        
        indice = 0
        while indice < len(prof):
            if prof[indice]["cod"] == codigo_ser_procurado:
                break
            indice+=1

        prof[indice]["cod"]=(input("Qual o novo código?  "))
        prof[indice]["nome"]=(input("Qual o novo nome?  "))


    elif opcao_escolhida == 4:
        print("Listar")
        if len(prof) == 0:
            print("A lista está vazia, cadastre algum professor.")
        else:
            i = 0
            while i<len(prof):
                print(f'Código:{prof[i]["cod"]} - {prof[i]["nome"]}')
                i+=1

    elif opcao_escolhida == 5:
        print("Cadastrar")
        i = 0
        while i<len(prof):
            print(f'Código:{prof[i]["cod"]} - {prof[i]["nome"]}')
            i+=1
        lab = input("Digite em qual laboratório deseja cadastrar os professores: ")
        profs = input("Digite o código dos professores: ")
        for laboratorio in acesso:
            if laboratorio["lab"] == lab:
                for codigo in profs.split(", "):
                    for professor in prof:
                        if professor["cod"] == codigo:
                            laboratorio["profs"].append(professor["nome"])

    elif opcao_escolhida == 6:
        print("Excluir")
        print("")
        print("Lista láboratorios: ")
        for laboratorio in acesso:
            print("- ", laboratorio["lab"])
        
        nome_laboratorio = input("Digite em qual laboratório deseja excluir os professores: ")

        indice = 0
        while indice < len(acesso):
            if(acesso[indice]["lab"] == nome_laboratorio):
                print("Encontrei o láboratorio: ", nome_laboratorio)
                print("Professores presentes: ")

                professores_presentes = []
                for profis in prof:
                    
                    if profis["nome"] in acesso[indice]["profs"]: # se o nome do professor está na lista de nomes que tem acesso
                        professores_presentes.append(profis)

                for presentes in professores_presentes:
                    print("- ", presentes["cod"], " - ", presentes["nome"])

                profs = input("Digite o código do professor: ")
            indice+=1







######### Listar #########
        i = 0
        while i<len(acesso):
            nomeS = ""
            for nome in acesso[i]["profs"]:
                nomeS+=nome+", "
############ arrumar a virgula no texto (Ele corta os dois ultimos caracteres)
            nomeS = nomeS[:-2] + "."
            
            print(f'{acesso[i]["lab"]} - {nomeS}')
            i+=1
############################################
        for laboratorio in acesso:
            if laboratorio["lab"] == lab:
                for codigo in profs.split(", "):
                    for professor in prof:
                        if professor["cod"] == codigo:
                            laboratorio["profs"].append(professor["nome"])
    # codigo_ser_procurado = input("Quem você deseja excluir? (informe o código) ")

    # indice = 0
    # while indice < len(prof):
    #     if prof[indice]["cod"] == codigo_ser_procurado:
    #         break
    #     indice+=1

    # prof.pop(indice)

        # print("Amigo deletado com sucesso!")

    elif opcao_escolhida == 7:
        print("Alterar")
        i = 0
        while i<len(prof):
            print(f'Código:{prof[i]["cod"]} - {prof[i]["nome"]}')
            i+=1
        codigo_ser_procurado = input("Quem você deseja alterar? (informe o código) ")
        
        indice = 0
        while indice < len(prof):
            if prof[indice]["cod"] == codigo_ser_procurado:
                break
            indice+=1

        prof[indice]["cod"]=(input("Qual o novo código?  "))
        prof[indice]["nome"]=(input("Qual o novo nome?  "))

    elif opcao_escolhida == 8:
        #####listar
        i = 0
        while i<len(acesso):
            nomeS = ""
            for nome in acesso[i]["profs"]:
                nomeS+=nome+", "
########### arrumar a virgula no texto (Ele corta os dois ultimos caracteres)
            nomeS = nomeS[:-2] + "."
            
            print(f'{acesso[i]["lab"]} - {nomeS}')
            i+=1 