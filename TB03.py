class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class RedeColaboracaoAcademica:
    def __init__(self):
        self.alunos = {}
        self.union_find = None
        self.counter = 0

    def adicionar_aluno(self, nome, disciplinas):
        self.alunos[self.counter] = {
            "nome": nome,
            "disciplinas": disciplinas,
        }
        self.counter += 1
        if self.union_find is None:
            self.union_find = UnionFind(self.counter)
        else:
            self.union_find.parent.append(self.counter - 1)
            self.union_find.rank.append(1)

    def unir_alunos_por_disciplina(self, disciplina):
        for i in range(self.counter):
            for j in range(i + 1, self.counter):
                if disciplina in self.alunos[i]['disciplinas'] and disciplina in self.alunos[j]['disciplinas']:
                    self.union_find.union(i, j)

    def verificar_conexao(self, aluno1, aluno2):
        id1 = self.buscar_aluno_por_nome(aluno1)
        id2 = self.buscar_aluno_por_nome(aluno2)
        if id1 is not None and id2 is not None:
            return self.union_find.find(id1) == self.union_find.find(id2)
        return False

    def buscar_aluno_por_nome(self, nome):
        for id, dados in self.alunos.items():
            if dados['nome'] == nome:
                return id
        return None

    def exibir_grupo(self, nome):
        id = self.buscar_aluno_por_nome(nome)
        if id is not None:
            grupo = self.union_find.find(id)
            print(f"Grupo de {nome}:")
            for i in range(self.counter):
                if self.union_find.find(i) == grupo:
                    print(f"  - {self.alunos[i]['nome']}")
        else:
            print(f"Aluno {nome} não encontrado.")

def menu_interativo():
    rede = RedeColaboracaoAcademica()

    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Unir alunos por disciplina")
        print("3. Verificar se alunos estão no mesmo grupo")
        print("4. Exibir grupo de um aluno")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            disciplinas = input("Disciplinas (separadas por vírgula): ").split(',')
            rede.adicionar_aluno(nome, disciplinas)
            print(f"Aluno {nome} adicionado com sucesso!")

        elif opcao == "2":
            disciplina = input("Disciplina para unir alunos: ")
            rede.unir_alunos_por_disciplina(disciplina)
            print(f"Alunos com a disciplina {disciplina} foram unidos.")

        elif opcao == "3":
            aluno1 = input("Nome do primeiro aluno: ")
            aluno2 = input("Nome do segundo aluno: ")
            if rede.verificar_conexao(aluno1, aluno2):
                print(f"{aluno1} e {aluno2} estão no mesmo grupo.")
            else:
                print(f"{aluno1} e {aluno2} NÃO estão no mesmo grupo.")

        elif opcao == "4":
            nome = input("Nome do aluno: ")
            rede.exibir_grupo(nome)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu_interativo()
