def main():
    ## ALUNOS CADASTRADOS NO SISTEMA
    global removerev
    alunos = {'Amanda': ['Amanda Thayane de Andrade Siqueira', 'Sistemas para internet', 'Noite', '20192007034', '103.629.444-74'],
              'Hélio': ['Helio Gomes Gabi Filho', 'Sistemas para internet', 'Noite', '20192007036', '105.679.122-69'],
              'Matheus': ['Matheus Gonçalves de Oliveira Antunes', 'Sistemas para internet', 'Noite', '20192007033','215.246.728-97']}
    funcionario = {'Izabel': ['Izabel Borba', 'RH', '10522864742'],
                   'Aline': ['Aline Morais', 'Professora', '20654378992'],
                   'Paulo': ['Paulo Castro', 'Estacionamento', '12345678983']}
    eventos = {}
    veiculo = {}
    ocorrencia = {}
    cadvisitante = {}

    print('\033[47m' + '\033[1m' + '\033[30m' + '-' * 63 + '\033[0;0m')
    print('\033[47m' + '\033[1m' + '\033[30m' + '                     ESTACIONAMENTO UNIESP                     ' + '\033[0;0m')
    print('\033[47m' + '\033[1m' + '\033[30m' + '-' * 63 + '\033[0;0m')
    print()

    ## INFORMAÇÕES DE LOGIN
    ##aluno = {'Amanda Siqueira': ['amanda123']}
    ##funcionariorh = {'Izabel Borba': ['iza123']}
    ##funcionarioest = {'Paulo Castro': ['paulo123']}

    while True:
        try:
            fazerlogin = str(input('Você já é cadastrado?'))

            ## EFETUANDO LOGIN
            if fazerlogin == str('sim'):
                login = (str(input('Login: ')))
                senha = (str(input('Senha: ')))


                ##LOGIN FUNCIONÁRIO
                if login == str('Izabel') and senha == str('iza123'):
                    print()
                    print("Você está no sistema da Uniesp")
                    print('\033[34m' + f'Informações de {login}: {funcionario[login]}' + '\033[0;0m')
                    print()

                    cadast = str('sim')
                    while cadast == str('sim'):
                        cadast = str(input('Deseja realizar outro cadastro? [Sim/Não]'))
                        if cadast == str('sim'):
                            al_fun = str(input('Deseja realizar cadastro de aluno ou funcionário? '))


                            ##CADASTRO ALUNO
                            if al_fun == str('aluno'):
                                print('\033[47m' + '\033[1m' + '\033[30m' + '-' * 63 + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '                     CADASTRO ALUNO                     ' + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '-' * 63 + '\033[0;0m')
                                print()

                                print('\033[35m'+'\033[1m'+f"Alunos cadastrados: {alunos}" + '\033[0;0m')
                                print()

                                inserira = str(input('Deseja inserir aluno? '))

                                if inserira == str('sim'):
                                    n = int(input('Quantos alunos vc deseja inserir? '))
                                    print()

                                    for i in range(n):
                                        nome = input('Digite o nome do aluno que você deseja inserir: ')
                                        alunos[nome] = [str(input('Nome completo: ')),
                                                        str(input('Curso: ')),
                                                        str(input('Turno: ')),
                                                        int(input('Matrícula: ')),
                                                        int(input('CPF: '))]

                                    print('\033[35m'+'\033[1m'+f"Alunos cadastrados: {alunos}" + '\033[0;0m')
                                    print()


                            ##CADASTRO FUNCIONÁRIO
                            if al_fun == str('funcionário'):
                                print('\033[47m' + '\033[1m' + '\033[30m' + '-' * 62 + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '                     CADASTRO FUNCIONÁRIO                     ' + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '-' * 62 + '\033[0;0m')
                                print()

                                print('\033[35m'+'\033[1m'+f"Funcionários cadastrados: {funcionario}" + '\033[0;0m')
                                print()

                                inserirf = str(input('Deseja inserir funcionário? '))

                                if inserirf == str('sim'):
                                    n = int(input('Quantos funcionários vc deseja inserir? '))
                                    print()

                                    for i in range(n):
                                        funcionarioINS = input('Digite o nome do funcionário que você deseja inserir: ')
                                        funcionario[funcionarioINS] = [str(input('Nome completo: ')),
                                                                       str(input('Cargo: ')),
                                                                       int(input('CPF: '))]

                                    print('\033[35m'+'\033[1m'+f"Funcionários cadastrados: {funcionario}" + '\033[0;0m')
                                    print()

                        else:
                            print()
                            print('\033[31m'+'\033[1m'+'Seção finalizada'+ '\033[0;0m')
                            break





                ##LOGIN FUNCIONÁRIO ESTACIONAMENTO
                if login == str('Paulo') and senha == str('paulo123'):
                    print()
                    print("Você está no sistema da Uniesp")
                    print('\033[34m' + f'Informações de {login}: {funcionario[login]}' + '\033[0;0m')
                    print()

                    cad = str('sim')
                    while cad == str('sim'):
                        cad = str(input('Deseja realizar alguma atividade no sistema?'))
                        if cad == str('sim'):


                            opc = str(input('Escolha uma das atividades: '
                                            'cadastrar veículo, '
                                            'remover veículo,'
                                            'cadastrar ocorrencia,'
                                            'cadastrar evento,'
                                            'remover evento'))



                           ## CADASTRO VEÍCULO (FEITO POR FUNCIONÁRIO DO ESTACIONAMENTO)
                            if opc == str('cadastrar veículo'):

                                print('\033[47m' + '\033[1m' + '\033[30m' + ' ' * 63 + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '                     CADASTRO VEÍCULO                     ' + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + ' ' * 63 + '\033[0;0m')
                                print()

                                print('\033[35m'+'\033[1m'+f"Alunos com cadastro: {alunos}"+ '\033[0;0m')
                                print('\033[35m'+'\033[1m'+f"Funcionários com cadastro: {funcionario}" + '\033[0;0m')
                                print('\033[35m'+'\033[1m'+f"Veículos cadastrados: {veiculo}" + '\033[0;0m')
                                print()


                                cadastroveiculo = str(input('O proprietário do veículo está cadastrado?'))
                                if cadastroveiculo == str('sim'):
                                    nome = input('Digite o nome do aluno/funcionário que você deseja cadastrar veículo: ')

                                    if nome in alunos.keys():
                                        veiculo[nome] = [str(input('Tipo de Veículo: ')),
                                                         str(input('Marca: ')),
                                                         str(input('Modelo: ')),
                                                         int(input('Ano: ')),
                                                         str(input('Placa: '))]
                                        print('\033[35m'+'\033[1m'+f"{nome}: {alunos[nome]}, possui veículo com as seguinte informações: {veiculo}" + '\033[0;0m')
                                        print()


                                    if nome in funcionario.keys():
                                        veiculo[nome] = [str(input('Tipo de Veículo: ')),
                                                         str(input('Marca: ')),
                                                         str(input('Modelo: ')),
                                                         int(input('Ano: ')),
                                                         str(input('Placa: '))]
                                        print('\033[35m'+'\033[1m'+f"{nome}: {funcionario[nome]}, possui veículo com as seguinte informações: {veiculo}" + '\033[0;0m')
                                        print()


                                else:
                                    n = int(input('Quantos visitantes vc deseja inserir?'))
                                    for i in range(n):
                                        visitante = input('Digite o nome do visitante que você deseja inserir: ')
                                        cadvisitante[visitante] = {str(input('CPF: ')),
                                                                   str(input('Tipo de veículo: ')),
                                                                   str(input('Marca: ')),
                                                                   str(input('Modelo: ')),
                                                                   int(input('Ano: ')),
                                                                   str(input('Placa: '))}
                                        print(cadvisitante)
                                        print()

                                print(veiculo)





                            ## REMOVER VEÍCULO
                            if opc == str('remover veículo'):

                                print('\033[47m' + '\033[1m' + '\033[30m' + ' ' * 63 + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '                     REMOVER VEÍCULO                     ' + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + ' ' * 63 + '\033[0;0m')
                                print()

                                remover = str(input('Deseja remover algum veículo? '))

                                if remover == str('sim'):
                                    removerveic = input("Nome do proprietário que deseja remover: ")
                                    if removerveic in veiculo.keys():
                                        veiculo.pop(removerveic)

                                    print('\033[35m'+'\033[1m'+f"Veículos cadastrados: {veiculo}" + '\033[0;0m')





                            ## CADASTRAR OCORRÊNCIA
                            if opc == str('cadastrar ocorrência'):

                                print('\033[47m' + '\033[1m' + '\033[30m' + ' ' * 63 + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '                     CADASTRAR OCORRÊNCIA                     ' + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + ' ' * 63 + '\033[0;0m')
                                print()

                                print('\033[35m'+'\033[1m'+f"Ocorrências cadastradas: {ocorrencia}" + '\033[0;0m')
                                print()

                                inserioc = str(input('Deseja cadastrar nova ocorrência? '))

                                if inserioc == str('sim'):
                                    oc = str(input('Irá precisar do espaço do estacionamento? '))
                                    if oc == str('sim'):
                                        n = int(input('Quantas ocorrências deseja inserir? '))
                                        print()
                                        for i in range(n):
                                            oco = input('Proprietário do veículo: ')
                                            ocorrencia[oco] = [str(input('Local da ocorrência: ')),
                                                               str(input('Data da ocorrência: ')),
                                                               str(input('Placa do veículo: ').split(','))]

                                            print('\033[35m'+'\033[1m'+f"Ocorrências cadastradas: {ocorrencia}" + '\033[0;0m')
                                            print()
                                else:
                                    print('\033[35m'+'\033[1m'+f"Ocorrências cadastradas: {ocorrencia}" + '\033[0;0m')
                                    print('\033[35m'+'\033[1m'+'Nenhuma ocorrência foi cadastrada'+ '\033[0;0m')







                            ## CADASTRAR EVENTO (FEITO POR FUNCIONÁRIO RH)
                            if opc == str('cadastrar evento'):
                                print('\033[47m' + '\033[1m' + '\033[30m' + '-' * 63 + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '                     CADASTRO EVENTO                     ' + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '-' * 63 + '\033[0;0m')
                                print()

                                print('\033[35m'+'\033[1m'+f"Eventos cadastrados: {eventos}" + '\033[0;0m')
                                print()

                                inserirf = str(input('Deseja cadastrar evento? '))

                                if inserirf == str('sim'):
                                    eventoest = str(input('Irá precisar do espaço do estacionamento? '))

                                    if eventoest == str('sim'):
                                        n = int(input('Quantos eventos deseja inserir? '))
                                        print()
                                        for i in range(n):
                                            evento = input('Título do evento: ')
                                            eventos[evento] = [str(input('Quantos dias de evento? ').split('-')),
                                                               str(input('Data de início do evento: (separe por barra : dia/mes/ano) ').split('/')),
                                                               str(input('Data de fim do evento: (separe por barra : dia/mes/ano) ').split('/')),
                                                               str(input('Cursos ao qual esse evento se aplica: (no caso de mais de 1 curso, separe por vírgula) ').split(','))]

                                            print('\033[35m'+'\033[1m'+f"Eventos cadastrados: {eventos}" + '\033[0;0m')
                                            print()
                                else:
                                    print('\033[35m'+'\033[1m'+f"Eventos cadastrados: {eventos}" + '\033[0;0m')
                                    print('\033[35m'+'\033[1m'+'Nenhum evento foi cadastrado'+ '\033[0;0m')






                            ## REMOVER EVENTO
                            if opc == str('remover evento'):

                                print('\033[47m' + '\033[1m' + '\033[30m' + ' ' * 63 + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + '                     REMOVER EVENTO                     ' + '\033[0;0m')
                                print('\033[47m' + '\033[1m' + '\033[30m' + ' ' * 63 + '\033[0;0m')
                                print()

                                print('\033[35m'+'\033[1m'+f"Eventos cadastrados: {eventos}" + '\033[0;0m')

                                removerevento = str(input('Deseja remover algum evento? '))

                                if removerevento == str('sim'):
                                    removerev = input("Nome do evento que deseja remover: ")
                                    if removerev in eventos.keys():
                                        eventos.pop(removerev)

                                print('\033[35m'+'\033[1m'+f"Eventos cadastrados: {eventos}" + '\033[0;0m')

                            sair = input('Você deseja sair do sistema?')
                            if sair == 'sim':
                                print()
                                print('\033[31m'+'\033[1m'+'Seção finalizada!!!'+ '\033[0;0m')
                                print()
                                break




                ##LOGIN ALUNO
                if login == str('Amanda') and senha == str('amanda123'):
                    print()
                    print("Você está no sistema da Uniesp")
                    print('\033[34m'+f'Informações de {login}: {alunos[login]}'+'\033[0;0m')
                    print()




            else:
                print()
                print('Apenas um funcionário da UNIESP pode fazer o cadastro, se possível, procure um funcionário para realizá-lo')
                break

        except IOError:
            print('Operação não realizada!!')

main()
