
ano_escolaridade = input('Digite o ano de escolaridade:')

if ano_escolaridade != '6' and ano_escolaridade != '7' and ano_escolaridade != '8' and ano_escolaridade != '9' and ano_escolaridade != '1' and ano_escolaridade != '2' and ano_escolaridade != '3':
    print("Ano de escolaridade incorreto")
    exit()
else:
    dados_tabela = open('Entrada.txt', 'r')
    turma_A = open('matriculas/' + str(ano_escolaridade) + 'A.txt', 'r')
    turma_B = open('matriculas/' +str(ano_escolaridade) + 'B.txt', 'r')
    plan_A = open('notas/plan_' + str(ano_escolaridade) + 'A.txt', 'w' )
    plan_B = open('notas/plan_' + str(ano_escolaridade) + 'B.txt', 'w')


    ''' 
    Tentar refinar Código
    def busca_turma(linha):

        #Comparaçã
        linha0 = linha.split()

        for matricula in turma_B:
            print("B")
            if linha0[0] == matricula.strip():
                print("ADD B")
                plan_B.write(linha)

        for matricula in turma_A:
            print("A")
            if linha0[0] == matricula.strip():
                print ( "ADD A" )
                plan_A.write(linha)

        return '''

    qtd_alunos =0
    qtdA = 0
    qtdB = 0

    lista_alunos = []
    lista_mat_A = []
    lista_mat_B = []

    for linha in dados_tabela:
        qtd_alunos += 1
        lista_alunos.append(linha)

    for qtd in turma_A:
        qtdA += 1
        lista_mat_A.append(qtd)

    for qtd in turma_B:
        qtdB += 1
        lista_mat_B.append(qtd)

    for item in range(qtd_alunos):
        for item2 in range(qtdA):
            matricula = lista_alunos[item].split()
            num_matricula = lista_mat_A[item2]
            alunoM = matricula[0]
            if num_matricula.strip() == alunoM.strip():
                plan_A.write(lista_alunos[item])

    for item in range ( qtd_alunos ):
        for item2 in range ( qtdB ) :
            matricula = lista_alunos[item].split ()
            num_matricula = lista_mat_B[item2]
            alunoM = matricula[0]
            if num_matricula.strip () == alunoM.strip () :
                plan_B.write ( lista_alunos[item] )

    turma_A.close()
    turma_B.close()
    plan_A.close()
    plan_B.close()

'''linha = '50002038    Henrique Vasconcelos Costa  7,63'
  matricula = '50002038'

  print(linha.find(matricula))'''

''' for linha in dados_tabela:
     for matricula in turma_A:
         print(linha, matricula)'''




