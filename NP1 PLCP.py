#Menu

escolha = "m" #Declarada a variavel global escolha, ela recebe um valor aleatorio.
comecar = "g" #Declarada a variavel global comeca, ela recebe um valor aleatorio.
# Função do Modulo Menu, quando chamada exibe o Menu do programa
def Menu(): 
      print("\n================ Menu Principal ================\n")
      
      print("Bem vindo ao menu! Escolha a opção desejada: ")
      print(" 1 - Aprender (Acesse um texto informativo sobre Phyton)")
      print(" 2 - Quiz (Comece o Quiz de perguntas sobre Python)")
      print(" 3 - Sair (Encerra o programa)")
      return
# Função Quiz ou Menu, quando chamada no fim de qualquer conteuto sobre Python exibe a pergunta para o usuario se ele deseja fazer um quiz sobre o conteudo ou voltar ao menu
def quizOUmenu():
     print("\nDeseja fazer um Quiz sobre o conteúdo estudado ou voltar ao menu? ")
     #identifica escolha como global para a função       
     global escolha 
     escolha = input("Digite 1 para o Quiz e 2 para voltar ao menu: ")
     return
    
#Função sair. Quando chamada exibe a pergunta se o usuario realmente deseja sair do programa
def Sair():
    print("\nVocê escolheu sair do programa, tem certeza que deseja sair? ")
    ver = str(input("Digite sim para sair e não para voltar ao menu\n"))
     #verifica se o usuario quer mesmo sair do programa. Com o .lower o valor armazenado na var é forçado a ficar minusculo.   
    if ver.lower() == "sim":
        print("Encerrando o Programa. . .")
          
    elif ver.lower() == "não":
        Menu()
        Ifs()
    else:
        print("\nA opção escolhida é invalida, Digite conforme orientado.")
        Sair()
    return
#função onde está a estrutura condicional do programa
def Ifs():
    global escolha
    global comecar
    
    escolha = str(input("\nDigite o número referente a sua escolha para acessa-la: "))
    
    #Verifica qual modulo o usuário escolheu    
    if escolha == "1": 
        print ("\nOpção Aprender escolhida. Escolha qual conteúdo estudar: ")
        print(" 1 - Comando Print()")
        print(" 2 - Comando Input()")
        escolha = input("Digite o número referente ao conteudo que deseja estudar: ")
        
        #Verifica se foi o conteudo 1
        if escolha == "1": 
           
            #Mostra o conteudo
            print("\n================ Função print() ================\n") 
            print("A função print() em Python é uma função embutida que exibe mensagens na tela, como no console ou terminal.")
            print("É uma das funções mais usadas na linguagem.")
            print("\n""Explicação: \n")
            print("Para usar a função print(), basta escrever ""print()"" seguido dos valores que deseja imprimir.")
            print("Quando deseja exibir uma menssagem de texto, basta colocar a menssagem entre aspas dentro dos")
            print("paranteses, veja abaixo: ")
            print('print("")')
            print("Por exemplo: print(""Olá, Mundo!"""")""")
            print("O que a função print() pode exibir:")
            print("A função print() pode exibir qualquer tipo de dado,")
            print("incluindo textos(strings), números, resultados de operações ou qualquer outro objeto dentro de Python.")
            print("O conteúdo será sempre convertido a uma string para ser exibido.")
         
            quizOUmenu() #Chama a fução quizORmenu
            
            if escolha == "1":   
                #INICIA O QUIZ DA OP1
                print("\nIndentifique o erro de sintaxe no seguinte comando: ")
                print('print("Hello, World)')
                print(" A) - A lingua está em ingles") 
                print(" B) - O espaço depois da virgula") 
                print(" C) - Começar com letra maiuscula")
                print(" D) - As aspas não terem sido fechadas")
                #Var local recebe a resposta
                RespQ = "h"    
                RespQ = str(input("A, B, C ou D? "))
                
                #verifica se a resposta está correta
                if RespQ.upper() == "D":
                  print("Resposta Correta! Parabéns !\n")
                else:
                  print("Você errou")
                  
            #Verifica se fo iescolhido voltar ao menu apartir dp conteudo 1    
            elif escolha == "2":
                Menu() #função menu chamada
                #se nao for 1 nem 2 é opção invalida
            else: 
                print("opção invalida")
            
        
        #verifica se o conteudo 2 foi selecionado 
        elif escolha == "2":  
            
            #mostra o conteudo 2
            print("\n================ Função input() ================")
            print("\nA função input() do Python permite que o programa receba dados do utilizador.") 
            print("É uma função built-in da linguagem ,ou seja, não é preciso instalá-la ou importá-la.\n")
            print("Como funciona:\n")
            print("A função é invocada com os parênteses ao final.")
            print("O programa abre para a entrada padrão, que é o terminal, o utilizador digita algo.")
            print("A função retorna os dados como string para a saída padrão.\n") 
            print("Exemplos:")
            print("1 - input(""Digite algo: "") ")
            print("2 - n = input(""Por favor digite o seu nome:"")")
            print("3 - umNome = input('Por favor digite o seu nome: ')")
            print("\nConsiderações:")
            print("Por padrão, a função input() armazena os dados como strings.") 
            print("Para armazenar um número inteiro digitado pelo utilizador, pode-se usar o comando (int) antes do input.")
            print("É possível fazer validações para verificar se o utilizador digitou algo ou não.")
            
            quizOUmenu()
        
            if escolha == "1":
                print("\nO seguinte o comando esta dando erro:")
                print("int(input(input(""Digite sua senha""))""")
                print("A)Não deveria ter Aspas")
                print("B)int só é valido com numeros")
                print("C)Não é necessario o input duas vezes")
                print("D)O certo seria (Digite sua senha)")
             
            elif escolha == "2":
                Menu()
                Ifs()
            else:
                print("Opção invalida. Insira 1 ou 2 conforme foi informado.")
            
    elif escolha == "2":

        print("\n================ Quiz de Python ================\n")
        print("Deseja começar? ")
        
        comecar = str(input("Sim - Não: "))
        
        if comecar.lower() == "sim":  
            print("\nQue ano o Python foi criado?")
            print(" A) - 2022")
            print(" B) - 1989")
            print(" C) - 1979")
            print(" D) - 1995")
            R1 = str(input("A, B, C ou D? "))
                
            if R1.upper() == "B":
               print("\n""Resposta Correta! Parabéns!")
            else:
               print ("Errouuuu!!!")
        
            print("\n""Segunda pergunta: O nome Python foi inspirado em um")
            print(" A) - Nome de um algoritmo romano")
            print(" B) - Grupo de escola de samba")
            print(" C) - Grupo de comédia")
            print(" D) - Nome do pai do criador")
            R2 = str(input("A, B, C ou D? "))
            
            if R2.upper() == "C":
                print("Resposta Correta! Parabéns!")
            else:
                print("Errouuuu!!!")
                  
            print("\n""Terceira pergunta: Indentifique o erro de sintaxe no seguinte comando")
            print("print(Hello, World)")
            print(" A) - A lingua está em ingles") 
            print(" B) - O espaço depois da virgula") 
            print(" C) - Começar com letra maiuscula")
            print(" D) - As aspas não terem sido fechadas")
            R3 = str(input("A, B, C ou D? "))
            
            if R3.upper() == "D":
                print("Resposta Correta! Parabéns !")
            else:
                print("Errouuuu!!!")
            
          
            print("\n""Quarta e ultima pergunta parabénss!: O seguinte o comando esta dando erro: int(input(input(""Digite sua senha"")) qual alternativa abaixo corrige o erro")
            print(" A) - Não deveria ter Aspas")
            print(" B) - Não é necessario o input duas vezes")
            print(" C) - int só é valido com numeros")
            print(' D) - O certo seria int(input(input(Digite sua senha)))')
            R4 = str(input("A, B, C ou D? "))
 
            if R4.upper() == "B":
                print("Resposta Correta! Parabéns !")
            else:
                print("Errouuu!!!")
        
        elif comecar.lower() == "nao":
            print("\nVocê escolheu não fazer o QUIZ, iremos te direcionar ao MENU.\n")
            Menu()
            Ifs()
        else:
            print("\nOpção invalida, estamos te direcionando ao MENU.\n")
            
    elif escolha == "3":
            Sair()
    else:   
        print("\nOpção invalida\n")
        Menu()
        Ifs()
    return

Menu()
Ifs()



#Menu

escolha = "m" #Declarada a variavel global escolha, ela recebe um valor aleatorio.
comecar = "g" #Declarada a variavel global comeca, ela recebe um valor aleatorio.
# Função do Modulo Menu, quando chamada exibe o Menu do programa
def Menu(): 
      print("================ Menu Principal ================")
      print("Bem vindo ao menu! Escolha a opção desejada: ")
      print(" 1 - Aprender (Acesse um texto informativo sobre Phyton)")
      print(" 2 - Quiz (Comece o Quiz de perguntas sobre Python)")
      print(" 3 - Sair (Encerra o programa)")
      return
# Função Quiz ou Menu, quando chamada no fim de qualquer conteuto sobre Python exibe a pergunta para o usuario se ele deseja fazer um quiz sobre o conteudo ou voltar ao menu
def quizOUmenu():
     print("\nDeseja fazer um Quiz sobre o conteúdo estudado ou voltar ao menu? ")
     #identifica escolha como global para a função       
     global escolha 
     escolha = input("Digite 1 para o Quiz e 2 para voltar ao menu ")
     return
    
#Função sair. Quando chamada exibe a pergunta se o usuario realmente deseja sair do programa
def Sair():
    print("\nVocê escolheu sair do programa, tem certeza que deseja sair? ")
    ver = str(input("Digite sim para sair e não para voltar ao menu\n"))
     #verifica se o usuario quer mesmo sair do programa. Com o .lower o valor armazenado na var é forçado a ficar minusculo.   
    if ver.lower() == "sim":
        print("\nVocê saiu do programa")
          
    elif ver.lower() == "não":
        Menu()
        Ifs()
    else:
        print("\nA opção escolhida é invalida, Digite conforme orientado.")
        Sair()
    return
#função onde está a estrutura condicional do programa
def Ifs():
    global escolha
    global comecar
    
    escolha = str(input("\nDigite sua escolha: "))
    
    #Verifica qual modulo o usuário escolheu    
    if escolha == "1": 
        print ("\nOpção Aprender escolhida. Escolha qual conteúdo estudar: ")
        print(" 1 - Comando Print()")
        print(" 2 - Comando Input()")
        escolha = input("Digite o número referente ao conteudo: ")
        
        #Verifica se foi o conteudo 1
        if escolha == "1": 
           
            #Mostra o conteudo
            print("\n================ Função print() ================\n") 
            print("A função print() em Python é uma função embutida que exibe mensagens na tela, como no console ou terminal.")
            print("É uma das funções mais usadas na linguagem.")
            print("\n""Explicação: \n")
            print("Para usar a função print(), basta escrever ""print()"" seguido dos valores que deseja imprimir.")
            print("Quando deseja exibir uma menssagem de texto, basta colocar a menssagem entre aspas dentro dos paranteses:")
            print('print("")')
            print("Por exemplo: print(""Olá, Mundo!"""")""")
            print("O que a função print() pode exibir:")
            print("A função print() pode exibir qualquer tipo de dado,")
            print("incluindo textos(strings), números, resultados de operações ou qualquer outro objeto dentro de Python.")
            print("O conteúdo será sempre convertido a uma string para ser exibido.")
         
            quizOUmenu() #Chama a fução quizORmenu
            
            if escolha == "1":   
                #INICIA O QUIZ DA OP1
                print("\nIndentifique o erro de sintaxe no seguinte comando: ")
                print('print("Hello, World)')
                print(" A) - A lingua está em ingles") 
                print(" B) - O espaço depois da virgula") 
                print(" C) - Começar com letra maiuscula")
                print(" D) - As aspas não terem sido fechadas")
                #Var local recebe a resposta
                RespQ = "h"    
                RespQ = str(input("A, B, C ou D? "))
                
                #verifica se a resposta está correta
                if RespQ.upper() == "D":
                  print("Resposta Correta! Parabéns !\n")
                else:
                  print("Você errou")
                  
            #Verifica se fo iescolhido voltar ao menu apartir dp conteudo 1    
            elif escolha == "2":
                Menu() #função menu chamada
                #se nao for 1 nem 2 é opção invalida
            else: 
                print("opção invalida")
            
        
        #verifica se o conteudo 2 foi selecionado 
        elif escolha == "2":  
            
            #mostra o conteudo 2
            print("\n================ Função input() ================")
            print("\nA função input() do Python permite que o programa receba dados do utilizador.") 
            print("É uma função built-in da linguagem ,ou seja, não é preciso instalá-la ou importá-la.\n")
            print("Como funciona:\n")
            print("A função é invocada com os parênteses ao final.")
            print("O programa abre para a entrada padrão, que é o terminal, o utilizador digita algo.")
            print("A função retorna os dados como string para a saída padrão.\n") 
            print("Exemplos:")
            print("1 - input(""Digite algo: "") ")
            print("2 - n = input(""Por favor digite o seu nome:"")")
            print("3 - umNome = input('Por favor digite o seu nome: ')")
            print("\nConsiderações:")
            print("Por padrão, a função input() armazena os dados como strings.") 
            print("Para armazenar um número inteiro digitado pelo utilizador, pode-se usar o comando (int) antes do input.")
            print("É possível fazer validações para verificar se o utilizador digitou algo ou não.")
            
            quizOUmenu()
        
            if escolha == "1":
                print("\nO seguinte o comando esta dando erro:")
                print("int(input(input(""Digite sua senha""))""")
                print("A)Não deveria ter Aspas")
                print("B)int só é valido com numeros")
                print("C)Não é necessario o input duas vezes")
                print("D)O certo seria (Digite sua senha)")
             
            elif escolha == "2":
                Menu()
                Ifs()
            else:
                print("Opção invalida. Insira 1 ou 2 conforme foi informado.")
            
    elif escolha == "2":

        print("\n================ Quiz de Python ================\n")
        print("Deseja começar? ")
        
        comecar = str(input("Sim - Não: "))
        
        if comecar.lower() == "sim":  
            print("\nQue ano o Python foi criado?")
            print(" A) - 2022")
            print(" B) - 1989")
            print(" C) - 1979")
            print(" D) - 1995")
            R1 = str(input("A, B, C ou D? "))
                
            if R1.upper() == "B":
               print("\n""Resposta Correta! Parabéns!")
            else:
               print ("Errouuuu!!!")
        
            print("\n""Segunda pergunta: O nome Python foi inspirado em um")
            print(" A) - Nome de um algoritmo romano")
            print(" B) - Grupo de escola de samba")
            print(" C) - Grupo de comédia")
            print(" D) - Nome do pai do criador")
            R2 = str(input("A, B, C ou D? "))
            
            if R2.upper() == "C":
                print("Resposta Correta! Parabéns!")
            else:
                print("Errouuuu!!!")
                  
            print("\n""Terceira pergunta: Indentifique o erro de sintaxe no seguinte comando")
            print("print(Hello, World)")
            print(" A) - A lingua está em ingles") 
            print(" B) - O espaço depois da virgula") 
            print(" C) - Começar com letra maiuscula")
            print(" D) - As aspas não terem sido fechadas")
            R3 = str(input("A, B, C ou D? "))
            
            if R3.upper() == "D":
                print("Resposta Correta! Parabéns !")
            else:
                print("Errouuuu!!!")
            
          
            print("\n""Quarta e ultima pergunta parabénss!: O seguinte o comando esta dando erro: int(input(input(""Digite sua senha"")) qual alternativa abaixo corrige o erro")
            print(" A) - Não deveria ter Aspas")
            print(" B) - Não é necessario o input duas vezes")
            print(" C) - int só é valido com numeros")
            print(' D) - O certo seria int(input(input(Digite sua senha)))')
            R4 = str(input("A, B, C ou D? "))
 
            if R4.upper() == "B":
                print("Resposta Correta! Parabéns !")
            else:
                print("Errouuu!!!")
        
        elif comecar.lower() == "nao":
            print("\nVocê escolheu não fazer o QUIZ, iremos te direcionar ao MENU.\n")
            Menu()
            Ifs()
        else:
            print("\nOpção invalida, estamos te direcionando ao MENU.\n")
            
    elif escolha == "3":
            Sair()
    else:   
        print("\nOpção invalida\n")
        Menu()
        Ifs()
    return

Menu()
Ifs()



