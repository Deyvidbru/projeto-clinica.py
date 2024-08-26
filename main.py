from model import *

arquivo_path = 'login.txt'

autenticacao = Autenticacao(arquivo_path)
login_salvo, senha_salva = autenticacao.ler_credenciais()

if login_salvo is not None and senha_salva is not None:
    login_usuario = input("Digite o login: ")
    senha_usuario = input("Digite a senha: ")

    if login_usuario == login_salvo and senha_usuario == senha_salva:
        print("Autenticação feita com sucesso!")
        MENU=f"""
        1...........Cadastrar Funcionário 
        2...........Exibir Dados Funcionário
        3...........Editar Dados Funcionário
        4...........Remover Funcionário
        5...........Exibir Todos os Funcionários
        6...........Cadastrar Médico
        7...........Exibir Todos os Médicos
        8...........Editar Dados Médico
        9..........Remover Médico
        10..........Exibir Dados Médico
        11..........Cadastrar paciente
        12..........Exibir todos os pacientes
        13..........Editar Dados paciente
        14..........Remover Dados paciente
        15..........Exibir Dados paciente
        16..........Adicionar Consulta
        17..........Marcar Consulta como Paga
        18..........Adicionar Evolução do Paciente
        19..........Listar Evolução do Paciente 
        20..........Listar Consultas Pendentes de Pagamento
        0...........Sair do Programa
        """
        nome="clinica oxi"
        cnpj="11111111"
        endereco="rua: mangueira, bairro:ivan bezerra, cidade:Parelhas "
        empresa=Empresa(nome,cnpj,endereco)

        opcao=""
        while opcao!=0:
            print(MENU)
            opcao=input("digite sua opção: ")
            if opcao=="1":
                tipo_funcionario = input("Digite o tipo de funcionário (atendimento/limpeza): ")

                nome = input("Nome: ")
                rg = input("RG: ")
                rua=input("Rua: ")
                bairro=input("Bairro: ")
                cidade=input("Cidade: ")
                telefone=input("Telefone: ")

                if tipo_funcionario == "atendimento":
                    ano_conclusao = input("Ano de conclusão do curso: ")
                    faculdade = input("Nome da faculdade cursada: ")
                    titulo_tcc = input("Título do TCC: ")

                    empresa.cadastrar_funcionario_atendimento(
                        nome, rg, Endereco(rua, bairro, cidade), telefone, ano_conclusao, faculdade, titulo_tcc
                    )
                    print("Funcionário de atendimento cadastrado com sucesso")
                elif tipo_funcionario == "limpeza":
                    produto_limpeza = input("Produto de Limpeza: ")
                    empresa.cadastrar_funcionario_limpeza(
                        nome, rg, Endereco(rua, bairro, cidade), telefone, produto_limpeza
                    )
                    print("Funcionário de limpeza cadastrado com sucesso")
                else:
                    print("Tipo de funcionário inválido.")
            elif opcao=="2":
                rg = input("Digite o RG do funcionário que deseja exibir: ")
                funcionario = empresa.exibir_funcionario(rg)
                if funcionario is not None:
                    print(funcionario)
                else:
                    print("Funcionário não encontrado.")
            elif opcao == "3":
                rg_editar = input("Digite o RG do funcionário que deseja editar: ")
                funcionario_editar = empresa.get_funcionario(rg_editar)

                if funcionario_editar is not None:
                    novo_rg = input("Digite o novo RG: ")
                    novo_nome = input("Digite o novo nome: ")
                    novo_telefone = input("Digite o novo telefone: ")
                    nova_rua = input("Rua: ")
                    novo_bairro = input("Bairro: ")
                    nova_cidade = input("Cidade: ")

                    if isinstance(funcionario_editar, Funcionario_atendimento):
                        novo_ano_conclusao = input("Digite o novo ano de conclusão do curso: ")
                        nova_faculdade = input("Digite a nova faculdade cursada: ")
                        novo_titulo_tcc = input("Digite o novo título do TCC: ")

                        empresa.editar_funcionario(
                            rg_editar,
                            novo_rg,
                            novo_nome,
                            novo_telefone,
                            Endereco(nova_rua, novo_bairro, nova_cidade),
                            novo_ano_conclusao,
                            nova_faculdade,
                            novo_titulo_tcc,
                        )
                        print("Funcionário de atendimento editado com sucesso")

                    elif isinstance(funcionario_editar, Funcionario_limpeza):
                        novo_produto_limpeza = input("Digite o novo produto de limpeza: ")

                        empresa.editar_funcionario(
                            rg_editar,
                            novo_rg,
                            novo_nome,
                            novo_telefone,
                            Endereco(nova_rua, novo_bairro, nova_cidade),
                            novo_produto_limpeza=novo_produto_limpeza,
                        )
                        print("Funcionário de limpeza editado com sucesso")

                    else:
                        empresa.editar_funcionario(
                            rg_editar,
                            novo_rg,
                            novo_nome,
                            novo_telefone,
                            Endereco(nova_rua, novo_bairro, nova_cidade)
                        )
                        print("Funcionário editado com sucesso")
                else:
                    print("Funcionário não encontrado.")
            elif opcao=="4":
                rg = input("Digite o RG do funcionário que deseja remover: ")
                if empresa.remover_funcionario(rg):
                    print("Funcionário removido com sucesso.")
                else:
                    print("Funcionário não encontrado.")     
            elif opcao == "5":
                funcionarios = empresa.exibir_todos_funcionarios() 
                if funcionarios:
                    for funcionario in funcionarios:
                        print(funcionario)
                else:
                    print("Nenhum funcionário cadastrado.")
            elif opcao == "6":
                nome = input("Nome: ")
                rg = input("RG: ")
                telefone = input("Telefone: ")

                rua = input("Rua: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")

                crm = input("Crm: ")

                sigla_convenio = input("Sigla do Convênio (ou deixe em branco): ")
                convenio = None
                if sigla_convenio:
                    nome_convenio = input("Nome do Convênio: ")
                    telefone_convenio = input("Telefone do Convênio: ")
                    hospital_convenio = input("Hospital do Convênio: ")
                    convenio = Convenio(sigla_convenio, nome_convenio, telefone_convenio, hospital_convenio)

                empresa.cadastrar_medico(Medico(nome, rg, Endereco(rua, bairro, cidade), telefone, crm, convenio))
                print("Médico cadastrado com sucesso.")
            elif opcao == "7":
                medicos = empresa.exibir_todos_medicos()
                if medicos:
                    for medico in medicos:
                        print(medico)
                else:
                    print("Nenhum médico cadastrado.")
            elif opcao=="8":
                rg = input("Digite o RG do médico que deseja editar: ")
                novo_nome = input("Digite o novo nome: ")
                novo_rg = input("Digite o novo RG: ")
                novo_telefone = input("Digite o novo telefone: ")
                nova_rua = input("Rua: ")
                novo_bairro = input("Bairro: ")
                nova_cidade = input("Cidade: ")
                novo_crm = input("Digite o novo CRM: ")

                if empresa.editar_medico(rg, novo_nome, novo_rg, novo_telefone, Endereco(nova_rua, novo_bairro, nova_cidade), novo_crm):
                    print("Médico editado com sucesso.")
                else:
                    print("Médico não encontrado.")
            elif opcao=="9":
                rg = input("Digite o RG do médico que deseja remover: ")
                if empresa.remover_medico(rg):
                    print("Médico removido com sucesso.")
                else:
                    print("Médico não encontrado.")
            elif opcao=="10":
                rg = input("Digite o RG do médico que deseja exibir: ")
                medico = empresa.exibir_medico(rg)
                if medico is not None:
                    print(medico)
                else:
                    print("Médico não encontrado.")
            elif opcao == "11":
                nome = input("Nome: ")
                rg = input("RG: ")
                rua = input("Rua: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                telefone = input("Telefone: ")
                estado_saude = input("Estado de Saúde: ")

                empresa.cadastrar_paciente(nome, rg, Endereco(rua, bairro, cidade), telefone, estado_saude)

            elif opcao == "12":
                pacientes = empresa.exibir_todos_pacientes()
                if pacientes:
                    for paciente in pacientes:
                        print(paciente)
                else:
                    print("Nenhum paciente cadastrado.")

            elif opcao == "13":
                rg_editar = input("Digite o RG do paciente que deseja editar: ")
                paciente_editar = empresa.get_paciente(rg_editar)

                if paciente_editar is not None:
                    novo_nome = input("Digite o novo nome: ")
                    novo_telefone = input("Digite o novo telefone: ")
                    nova_rua = input("Rua: ")
                    novo_bairro = input("Bairro: ")
                    nova_cidade = input("Cidade: ")
                    novo_estado_saude = input("Digite o novo estado de saúde: ")

                    empresa.editar_paciente(
                        rg_editar,
                        novo_nome,
                        novo_telefone,
                        Endereco(nova_rua, novo_bairro, nova_cidade),
                        novo_estado_saude,
                    )
                    print("Paciente editado com sucesso.")

                else:
                    print("Paciente não encontrado.")

            elif opcao == "14":
                rg = input("Digite o RG do paciente que deseja remover: ")
                if empresa.remover_paciente(rg):
                    print("Paciente removido com sucesso.")
                else:
                    print("Paciente não encontrado.")

            elif opcao == "15":
                rg = input("Digite o RG do paciente que deseja exibir: ")
                paciente = empresa.exibir_paciente(rg)
                if paciente is not None:
                    print(paciente)
                else:
                    print("Paciente não encontrado.")
            elif opcao == "16":
                data = input("Data da consulta: ")
                descricao = input("Descrição da consulta: ")
                valor = input("Valor da consulta: ")
                medico_rg = input("RG do médico: ")
                paciente_rg = input("RG do paciente: ")

                medico = empresa.exibir_medico(medico_rg)
                paciente = empresa.exibir_paciente(paciente_rg)

                if medico and paciente:
                    consulta = empresa.cadastrar_consulta(data, descricao, valor, medico, paciente)
                    empresa.lista_consultas.append(consulta)
                    print("Consulta cadastrada com sucesso.")
                else:
                    print("Médico ou paciente não encontrado.")
            elif opcao == "17":
                num_consulta = int(input("Número da consulta a ser marcada como paga: ")) - 1

                if 0 <= num_consulta < len(empresa.lista_consultas):
                    consulta = empresa.lista_consultas[num_consulta]
                    consulta.marcar_como_pago()
                    print("Consulta marcada como paga.")
                else:
                    print("Número de consulta inválido.")
            elif opcao == "18":
                paciente_rg = input("RG do paciente: ")
                evolucao = input("Evolução do paciente: ")

                paciente = empresa.exibir_paciente(paciente_rg)

                if paciente:
                    paciente.adicionar_evolucao(evolucao)
                    print("Evolução do paciente adicionada com sucesso.")
                else:
                    print("Paciente não encontrado.")
            elif opcao == "19":
                consultas_pendentes = empresa.listar_consultas_pendentes()

                if consultas_pendentes:
                    for i, consulta in enumerate(consultas_pendentes, 1):
                        print(f"{i}. {consulta}")
                else:
                    print("Não há consultas pendentes de pagamento.")
            elif opcao == "20":
                paciente_rg = input("RG do paciente: ")
                paciente = empresa.exibir_paciente(paciente_rg)

                if paciente:
                    evolucoes = paciente.listar_evolucao()
                    if evolucoes:
                        for evolucao in evolucoes:
                            print(evolucao)
                    else:
                        print("Não há evolução registrada para o paciente.")
                else:
                    print("Paciente não encontrado.")
            elif opcao == "0":
                print("Saindo do programa.")
            else:
                print("Opção inválida. Tente novamente.")
                
    else:
        print("Erro: Credenciais Inválidas. Finalizando o programa.")
else:
    print("Erro ao ler as credenciais. Encerrando o programa")