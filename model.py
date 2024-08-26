class Pessoa:
    def __init__ (self, nome,rg,endereco,telefone):
        self._nome=nome
        self._rg=rg
        self._endereco=endereco
        self._telefone=telefone
    
    def __str__(self):
        return f"nome: {self._nome}\nrg: {self._rg}\nendereço: {self._endereco}\ntelefone: {self._telefone}"
    
class Funcionario_atendimento(Pessoa):
    def __init__(self, nome, rg, endereco, telefone, ano_conclusao, faculdade, titulo_tcc):
        super().__init__(nome, rg, endereco, telefone)
        self._ano_conclusao = ano_conclusao
        self._faculdade = faculdade
        self._titulo_tcc = titulo_tcc

    def __str__(self):
        return f"{super().__str__()}\nano_conclusao: {self._ano_conclusao}\nfaculdade: {self._faculdade}\ntitulo_tcc: {self._titulo_tcc}"

class Funcionario_limpeza(Pessoa):
    def __init__(self, nome, rg, endereco, telefone, produto_limpeza):
        super().__init__(nome, rg, endereco, telefone)
        self._produto_limpeza = produto_limpeza

    def obter_produto_limpeza(self):
        return f"{self._nome} está usando {self._produto_limpeza} para limpar."

    def __str__(self):
        informacoes_pessoa = super().__str__()
        informacoes_limpeza = f"Produto de Limpeza: {self._produto_limpeza}"
        return f"{informacoes_pessoa}\n{informacoes_limpeza}"
        
class Medico(Pessoa):
    def __init__(self, nome, rg, endereco, telefone, crm, convenio=None):
        super().__init__(nome, rg, endereco, telefone)
        self._crm = crm
        self._convenio = convenio

    def __str__(self):
        convenio_info = f"\nConvênio: {self._convenio}" if self._convenio else ""
        return f"{super().__str__()}\nCRM: {self._crm}{convenio_info}"

    def associar_convenio(self, convenio):
        self._convenio = convenio
    
class Consulta:
    def __init__(self, data, descricao, valor, medico, paciente):
        self._data = data
        self._descricao = descricao
        self._valor = valor
        self._medico = medico
        self._paciente = paciente
        self._pago = False  # Inicializa como não pago

    def marcar_como_pago(self):
        self._pago = True

    def __str__(self):
        status_pagamento = "Pago" if self._pago else "Não Pago"
        return f"Data: {self._data}\nDescrição: {self._descricao}\nValor: {self._valor}\nMédico: {self._medico}\nPaciente: {self._paciente}\nStatus de Pagamento: {status_pagamento}"
    
class Paciente(Pessoa):
    def __init__(self, nome, rg, endereco, telefone, estado_saude):
        super().__init__(nome, rg, endereco, telefone)
        self._estado_saude = estado_saude

    def __str__(self):
        return f"{super().__str__()}\nEstado de Saúde: {self._estado_saude}"

class Convenio:
    def __init__(self, sigla, nome, telefone, hospital):
        self._sigla = sigla
        self._nome = nome
        self._telefone = telefone
        self._hospital = hospital

    def __str__(self):
        return f"Sigla: {self._sigla}\nNome: {self._nome}\nTelefone: {self._telefone}\nHospital: {self._hospital}"

class Endereco: 
    def __init__(self, rua, bairro, cidade):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        
    def __str__(self):
        return f"Rua: {self.rua}\nBairro: {self.bairro}\nCidade: {self.cidade}"

class Empresa:
    def __init__(self, nome,cnpj,endereco):
        self.nome=nome
        self.cnpj=cnpj
        self.endereco=endereco
        self.lista_funcionario = []
        self.lista_medico=[]
        
    def cadastrar_funcionario_atendimento(self, nome, rg, endereco, telefone, ano_conclusao, faculdade, titulo_tcc):
        funcionario = Funcionario_atendimento(nome, rg, endereco, telefone, ano_conclusao, faculdade, titulo_tcc)
        self.lista_funcionario.append(funcionario)
        
    def cadastrar_funcionario_limpeza(self, nome, rg, endereco, telefone, produto_limpeza):
        funcionario = Funcionario_limpeza(nome, rg, endereco, telefone, produto_limpeza)
        self.lista_funcionario.append(funcionario) 
        
    def exibir_funcionario(self, rg):
        for funcionario in self.lista_funcionario:
            if funcionario._rg == rg:
                return funcionario
        return None
    
    def get_funcionario(self, rg):
        for funcionario in self.lista_funcionario:
            if funcionario._rg == rg:
                return funcionario
        return None  
    
    def editar_funcionario(self, rg, novo_rg=None, novo_nome=None, novo_telefone=None, novo_endereco=None,
                       novo_ano_conclusao=None, nova_faculdade=None, novo_titulo_tcc=None,
                       novo_produto_limpeza=None):
        funcionario = self.get_funcionario(rg)

        if funcionario:
            if novo_nome is not None:
                funcionario._nome = novo_nome
            if novo_telefone is not None:
                funcionario._telefone = novo_telefone
            if novo_endereco is not None:
                funcionario._endereco = novo_endereco
            if novo_rg is not None:
                funcionario._rg = novo_rg

            if isinstance(funcionario, Funcionario_atendimento):
                funcionario._ano_conclusao = novo_ano_conclusao
                funcionario._faculdade = nova_faculdade
                funcionario._titulo_tcc = novo_titulo_tcc

            elif isinstance(funcionario, Funcionario_limpeza):
                if novo_produto_limpeza is not None:
                    funcionario._produto_limpeza = novo_produto_limpeza

            return True

        return False
    
    def remover_funcionario(self, rg):
        funcionario = self.get_funcionario(rg)
        if funcionario:
            self.lista_funcionario.remove(funcionario)
            return True  
        return False

    def exibir_todos_funcionarios(self):
        return self.lista_funcionario
        
    def cadastrar_medico(self, medico, convenio=None):
        medico.associar_convenio(convenio)
        self.lista_medico.append(medico)
    
    def exibir_medico(self, rg):
        for medico in self.lista_medico:
            if medico._rg == rg:
                return medico
        return None
    
    def editar_medico(self, rg_busca, novo_nome, novo_rg, novo_telefone, novo_endereco, novo_crm):
        medico = self.get_medico(rg_busca)
        if medico is not None:
            medico._nome = novo_nome
            medico._rg = novo_rg
            medico._telefone = novo_telefone
            medico._endereco = novo_endereco
            medico._crm = novo_crm
            return True
        return False

    def remover_medico(self, rg_remove):
        medico = self.get_medico(rg_remove)
        if medico:
            self.lista_medico.remove(medico)
            return True
        return False
    
    def get_medico(self, rg):
        for medico in self.lista_medico:
            if medico._rg == rg:  
                return medico
        return None
    
    def exibir_todos_medicos(self):
        return self.lista_medico
    
class Autenticacao:
    def __init__(self, arquivo_path):
        self.arquivo_path = arquivo_path
        
    def ler_credenciais(self):
        try:
            with open(self.arquivo_path, 'r') as arquivo:
                linhas = arquivo.readlines()
                if(len(linhas) == 2):
                    login_salvo = linhas[0].strip()
                    senha_salva = linhas[1].strip()
                    return login_salvo, senha_salva
                else:
                    print("Erro: O arquivo não contém as informações esperadas.")
                    return None, None
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.arquivo_path}' não foi encontrado.")
            return None, None