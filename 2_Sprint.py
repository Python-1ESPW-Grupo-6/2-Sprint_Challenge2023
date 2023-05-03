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

print('Bem-vido ao nosso projeto "GaloGuard", sistema preventivo para alagamentos nas vias urbanas')
print('')
while True:
    print('Seja bem vindo ao hub do nosso site!')
    print('')
    print('1 - Saber bairros com maior risco')
    print('2 - Notifique algum bairro de risco')
    print('3 - Conheça mais sobre o projeto')
    print('4 - Sair')
    print('')
    menu = int(input('Insira o número referente ao parte que quer acessar: '))
    print('')
    if menu == 1:
        print('Opção (1 - Saber bairros com maior risco) escolhida!')
        print('')
        while True:
            engano_1 = input('Entrou por engano? Se sim, deseja sair? (sim/não)').lower()
            if engano_1 == 'não':
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
                break
            elif engano_1 == 'sim':
                print('Ok, voltando para o menu!')
                print('')
                break
            else:
                print('Opção invalida! Tente novamente!')
                print('')
    elif menu == 2:
        print('Opção (2 - Notifique alguma area de risco) escolhida!')
        print('')
        while True:
            engano_2 = input('Entrou por engano? Se sim, deseja sair? (sim/não)').lower()
            print('')
            if engano_2 == 'não':
                notificacao_area = input('Notifique qual o bairro de risco! ')
                notificacao_bairro.append(notificacao_area)
                causa = input('Se souber qual poderia ser a causa de uma possivel enchente, podeiria descreve-la para nós? ')
                causa_risco.append(causa)
                print('')
                print('Obrigado pela notificação, voltando para o menu!')
                print('')
                break
            elif engano_2 == 'sim':
                print('Ok, voltando para o menu!')
                print('')
                break
            else:
                print('Opção invalida! Tente novamente!')
                print('')
    elif menu == 3:
        print('Opção (3 - Conheça mais sobre o projeto) escolhida!')
        print('')
        print('Um pouco sobre a história do nosso projeto:')
        print('')
        print('bla bla bla')
        print('')
        while True:
            voltar_menu = input('Quando quiser voltar para o menu apenas digite (voltar): ')
            print('')
            if voltar_menu == 'voltar':
                break
            else:
                print('Opção invalida! Tente novamente!')
                print('')
    elif menu == 4:
        print('Obrigado pelo seu acesso!')
        print('')
        print('Esse é o seu histório no nosso site:')
        print('')
        print(f'Procurou esses bairros: {bairro_pesquisados} ')
        print(f'Nesses respectivos meses: {meses_pesquisados} ')
        print('')
        print('Além de fazer essas notificações: ')
        print(f'{notificacao_bairro}')
        print(f'{causa_risco}')
        break
    else:
        print('Opção não encontrada! Tente novamente.')
        print('')