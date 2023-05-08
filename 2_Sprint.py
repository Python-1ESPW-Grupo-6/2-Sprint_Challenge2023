#lista de bairros que tendem a alagar em época de chuva intesa (verão)
# https://imoveis.estadao.com.br/noticias/saiba-quais-sao-os-bairros-mais-suscetiveis-a-enchentes-e-alagamentos-em-sao-paulo/

bairros_alagados = ['Mooca', 'Vila Prudente', 'Tatuapé', 'Belenzinho', 'Bela Vista', 'Casa Verde',
                    'Vila Leopoldina', 'Cidade Jardim', 'Chácara Santo Antônio', 'Bosque da Saúde']

#principais meses de chuva intensa
meses_temporal = ['Dezembro', 'Janeiro', 'Fevereiro', 'Março']
#demais meses para consulta
demais_meses = ['Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro']

#Histórico de pesquisa dos possiveis alagamentos em bairros
bairro_pesquisados = []
meses_pesquisados = []

#Histórico de notificação de bairros
notificacao_bairro = []
causa_risco = []

print('-------------------------------------------------------------------------------------------')
print('Bem-vido ao projeto "Galo Weather", sistema preventivo para alagamentos nas vias urbanas')
print('-------------------------------------------------------------------------------------------')
print('')
while True:
    print('------------------------------------')
    print('Seja bem vindo ao hub da Galo Weather!')
    print('------------------------------------')
    print('')
    print('1 - Consultar bairros com maior risco')
    print('2 - Notifique algum bairro de risco')
    print('3 - Conheça mais sobre o projeto')
    print('4 - Sair')
    print('')
    try:
        menu = int(input('Insira o número referente a parte que quer acessar: '))
        print('')
        match menu:
            case 1:
                print('--------------------------------------------------------')
                print('Opção (1 - Consultar bairros com maior risco) escolhida!')
                print('--------------------------------------------------------')
                print('')
                while True:
                    print('Consultar bairros')
                    print('')
                    print('1 - Consulte um bairro')
                    print('2 - Voltar')
                    print('')
                    try:
                        menu2 = int(input('Insira o número referente ao local que quer ir: '))
                        print('')
                        if menu2 == 1:
                            print (f'Bairros cadastrados: {bairros_alagados}')
                            print('')
                            bairro_user = input('Digite o bairro que queira consultar: ').lower() #input e normalização do dado para evitar erros de sintaxe
                            bairro_pesquisados.append(bairro_user)
                            if bairro_user in [bairro.lower() for bairro in bairros_alagados]: #verificação do input e normalização da lista
                                while True:
                                    mes_user = input('Digite o nome do mês corrente: ').lower()
                                    meses_pesquisados.append(mes_user)
                                    print('')
                                    if mes_user in [mes.lower() for mes in meses_temporal]:
                                        print (f'O bairro {bairro_user.capitalize()} tende a alagar no mês de {mes_user.capitalize()}. Tome cuidado!')
                                        print('')
                                        break
                                    elif mes_user in [mes.lower() for mes in demais_meses]:
                                        print (f'O bairro {bairro_user.capitalize()} não tende a alagar no mês de {mes_user.capitalize()}. Fique tranquilo!')
                                        print('')
                                        break
                                    else:
                                        print('')
                                        print('Mês não encontrado, verifique se contém abreviação ou erro ortográfico') #mensagem de erro ao usuário
                                        print('')
                            else:
                                print('')
                                print('Bairro não encontrado, verifique se contém abreviação ou erro ortográfico')
                                print('')
                        elif menu2 == 2:
                            print('Ok, voltando para o menu!')
                            print('')
                            break
                        else:
                            print('--------------------------------')
                            print('Opção invalida! Tente novamente!')
                            print('--------------------------------')
                            print('')
                    except ValueError:
                        print('---------------------------------')
                        print('Opção invalida! Digite um número!')
                        print('---------------------------------')
                        print('')
            case 2:
                print('-----------------------------------------------------')
                print('Opção (2 - Notifique alguma area de risco) escolhida!')
                print('-----------------------------------------------------')
                print('')
                while True:
                    print('Notificação')
                    print('')
                    print('1 - Mandar uma Notificação')
                    print('2 - Voltar')
                    print('')
                    try:
                        menu3 = int(input('Insira o número referente ao local que quer ir: '))
                        print('')
                        if menu3 == 1:
                            notificacao_area = input('Notifique qual o bairro de risco! ')
                            notificacao_bairro.append(notificacao_area)
                            causa = input('Se souber qual poderia ser a causa de uma possivel enchente, podeiria descreve-la para nós? ')
                            causa_risco.append(causa)
                            print('')
                            print('Obrigado pela notificação, voltando para o menu de Notificações!')
                            print('')
                        elif menu3 == 2:
                            print('Ok, voltando para o menu!')
                            print('')
                            break
                        else:
                            print('--------------------------------')
                            print('Opção invalida! Tente novamente!')
                            print('--------------------------------')
                            print('')
                    except ValueError:
                        print('---------------------------------')
                        print('Opção invalida! Digite um número!')
                        print('---------------------------------')
                        print('')
            case 3:
                print('---------------------------------------------------')
                print('Opção (3 - Conheça mais sobre o projeto) escolhida!')
                print('---------------------------------------------------')
                print('')
                print('Um pouco sobre a história do nosso projeto:')
                print('')
                print('bla bla bla')
                print('')
                while True:
                    voltar_menu = input('Quando quiser voltar para o menu apenas digite (voltar): ').lower()
                    print('')
                    if voltar_menu == 'voltar':
                        break
                    else:
                        print('Opção invalida! Tente novamente!')
                        print('')
            case 4:
                while True:
                    sair = input('Tem certeza que quer sair? (sim/não) ').lower()
                    print('')
                    if sair == 'sim':
                        print('-------------------------')
                        print('Obrigado pelo seu acesso!')
                        print('-------------------------')
                        print('')
                        if len(bairro_pesquisados) == 0 and len(notificacao_bairro) == 0:
                            break
                        elif len(bairro_pesquisados) >= 1 and len(notificacao_bairro) == 0:
                            print('Esse é o seu histório no nosso site:')
                            print('')
                            print(f'Procurou esses bairros: {bairro_pesquisados} ')
                            print(f'Nesses respectivos meses: {meses_pesquisados} ')
                            break
                        elif len(bairro_pesquisados) == 0 and len(notificacao_bairro) >= 1:
                            print('Esse é o seu histório no nosso site:')
                            print('')
                            print(f'{notificacao_bairro}')
                            print(f'{causa_risco}')
                            break
                        else:
                            print('Esse é o seu histório no nosso site:')
                            print('')
                            print(f'Procurou esses bairros: {bairro_pesquisados} ')
                            print(f'Nesses respectivos meses: {meses_pesquisados} ')
                            print('')
                            print('Além de fazer essas notificações: ')
                            print('')
                            print(f'{notificacao_bairro}')
                            print(f'{causa_risco}')
                            break
                    elif sair == 'não' or 'nao':
                        print('Ok, voltando para o menu!')
                        print('')
                        break
                    else:
                        print('--------------------------------------')
                        print('Opção não encontrada! Tente novamente.')
                        print('--------------------------------------')
                        print('')
                break
            case _:
                print('--------------------------------------')
                print('Opção não encontrada! Tente novamente.')
                print('--------------------------------------')
                print('')
    except ValueError:
        print('')
        print('---------------------------------')
        print('Opção invalida! Digite um número!')
        print('---------------------------------')
        print('')