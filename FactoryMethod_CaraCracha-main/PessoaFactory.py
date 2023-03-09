#Primeiro, vamos definir a classe base "Pessoa", que contém as propriedades comuns entre todas:
class Pessoa:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, matrícula {self.matricula}"

#Em seguida, vamos definir as classes "Aluno", "Professor", "Coordenador", "Diretor", "Administrador" e "Vestibulando" que herdam da classe "Pessoa":
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade, matricula)
        self.curso = curso

    def __str__(self):
        return f"Aluno: {super().__str__()}, curso de {self.curso}"


class Professor(Pessoa):
    def __init__(self, nome, idade, matricula, disciplina):
        super().__init__(nome, idade, matricula)
        self.disciplina = disciplina

    def __str__(self):
        return f"Professor: {super().__str__()}, disciplina de {self.disciplina}"


class Coordenador(Pessoa):
    def __init__(self, nome, idade, matricula, curso, departamento):
        super().__init__(nome, idade, matricula)
        self.curso = curso
        self.departamento = departamento

    def __str__(self):
        return f"Coordenador: {super().__str__()}, curso de {self.curso}, departamento de {self.departamento}"


class Diretor(Pessoa):
    def __init__(self, nome, idade, matricula, setor):
        super().__init__(nome, idade, matricula)
        self.setor = setor

    def __str__(self):
        return f"Diretor: {super().__str__()}, setor de {self.setor}"


class Administrador(Pessoa):
    def __init__(self, nome, idade, matricula, cargo):
        super().__init__(nome, idade, matricula)
        self.cargo = cargo

    def __str__(self):
        return f"Administrador: {super().__str__()}, cargo de {self.cargo}"


class Vestibulando(Pessoa):
    def __init__(self, nome, idade, matricula, escola):
        super().__init__(nome, idade, matricula)
        self.escola = escola

    def __str__(self):
        return f"Vestibulando: {super().__str__()}, escola de {self.escola}"


#Agora, vamos criar a classe "PessoaFactory", que será responsável por criar instâncias de Aluno e Professor, dependendo dos parâmetros de entrada:
class PessoaFactory:
    @staticmethod
    def criar_pessoa(nome, idade, matricula, cargo, **kwargs):
        if cargo == "aluno":
            curso = kwargs.get("curso")
            return Aluno(nome, idade, matricula, curso)
        elif cargo == "professor":
            disciplina = kwargs.get("disciplina")
            return Professor(nome, idade, matricula, disciplina)
        elif cargo == "coordenador":
            curso = kwargs.get("curso")
            departamento = kwargs.get("departamento")
            return Coordenador(nome, idade, matricula, curso, departamento)
        elif cargo == "diretor":
            setor = kwargs.get("setor")
            return Diretor(nome, idade, matricula, setor)
        elif cargo == "administrador":
            cargo = kwargs.get("cargo")
            return Administrador(nome, idade, matricula, cargo)
        elif cargo == "vestibulando":
            escola = kwargs.get("escola")
            return Vestibulando(nome, idade, matricula, escola)
        else:
            raise ValueError("Cargo inválido!")


# Solicitando dados do usuário e criando um aluno
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
matricula = int(input("Digite a matrícula do aluno: "))
curso = input("Digite o curso do aluno: ")

factory = PessoaFactory()
aluno = factory.criar_pessoa(nome, idade, matricula, "aluno", curso=curso)
print(aluno)

# Solicitando dados do usuário e criando um professor
nome = input("Digite o nome do professor: ")
idade = int(input("Digite a idade do professor: "))
matricula = int(input("Digite a matrícula do professor: "))
disciplina = input("Digite a disciplina do professor: ")

professor = factory.criar_pessoa(nome, idade, matricula, "professor", disciplina=disciplina)
print(professor)

# Solicitando dados do usuário e criando um coordenador
nome = input("Digite o nome do coordenador: ")
idade = int(input("Digite a idade do coordenador: "))
matricula = int(input("Digite a matrícula do coordenador: "))
curso = input("Digite o curso do coordenador: ")
departamento = input("Digite o departamento do coordenador: ")

factory = PessoaFactory()
coordenador = factory.criar_pessoa(nome, idade, matricula, "coordenador", curso=curso, departamento=departamento)
print(coordenador)

# Solicitando dados do usuário e criando um Diretor
nome = input("Digite o nome do diretor: ")
idade = int(input("Digite a idade do diretor: "))
matricula = int(input("Digite a matrícula do diretor: "))
setor = input("Digite o setor do diretor: ")

factory = PessoaFactory()
diretor = factory.criar_pessoa(nome, idade, matricula, "diretor", setor=setor)
print(diretor)

# Solicitando dados do usuário e criando um Administrador
nome = input("Digite o nome do administrador: ")
idade = int(input("Digite a idade do administrador: "))
matricula = int(input("Digite a matrícula do administrador: "))
area = input("Digite o área do administrador: ")

factory = PessoaFactory()
administrador = factory.criar_pessoa(nome, idade, matricula, "administrador", area=area)
print(administrador)

# Solicitando dados do usuário e criando um Vestibulando
nome = input("Digite o nome do vestibulando: ")
idade = int(input("Digite a idade do vestibulando: "))
matricula = int(input("Digite a matrícula do vestibulando: "))
escola = input("Digite o escola do vestibulando: ")

factory = PessoaFactory()
vestibulando = factory.criar_pessoa(nome, idade, matricula, "vestibulando", escola=escola)
print(vestibulando)
