class UnionFind:
    def __init__(self):
        self.pai = {}
        self.rank = {}

    def adicionar(self, aluno):
        if aluno not in self.pai:
            self.pai[aluno] = aluno
            self.rank[aluno] = 0

    def encontrar(self, aluno):
        if self.pai[aluno] != aluno:
            self.pai[aluno] = self.encontrar(self.pai[aluno])
        return self.pai[aluno]

    def unir(self, aluno1, aluno2):
        raiz1 = self.encontrar(aluno1)
        raiz2 = self.encontrar(aluno2)

        if raiz1 != raiz2:
            if self.rank[raiz1] > self.rank[raiz2]:
                self.pai[raiz2] = raiz1
            elif self.rank[raiz1] < self.rank[raiz2]:
                self.pai[raiz1] = raiz2
            else:
                self.pai[raiz2] = raiz1
                self.rank[raiz1] += 1

    def verificar_mesmo_grupo(self, aluno1, aluno2):
        return self.encontrar(aluno1) == self.encontrar(aluno2)

    def exibir_grupo(self, aluno):
        raiz = self.encontrar(aluno)
        return [a for a in self.pai if self.encontrar(a) == raiz]


class GerenciadorDisciplinas:
    def __init__(self):
        self.union_find_disciplinas = {}
        self.alunos_disciplinas = {}

    def adicionar_aluno(self, nome, disciplinas):
        if nome not in self.alunos_disciplinas:
            self.alunos_disciplinas[nome] = set(disciplinas)
        else:
            self.alunos_disciplinas[nome].update(disciplinas)

        # Adicionar aluno ao Union-Find de cada disciplina
        for disciplina in disciplinas:
            if disciplina not in self.union_find_disciplinas:
                self.union_find_disciplinas[disciplina] = UnionFind()
            self.union_find_disciplinas[disciplina].adicionar(nome)

    def unir_por_disciplina(self, disciplina):
        if disciplina not in self.union_find_disciplinas:
            print(f"Disciplina '{disciplina}' não encontrada.")
            return
        
        alunos_na_disciplina = [aluno for aluno, d in self.alunos_disciplinas.items() if disciplina in d]
        if len(alunos_na_disciplina) > 1:
            uf = self.union_find_disciplinas[disciplina]
            for i in range(1, len(alunos_na_disciplina)):
                uf.unir(alunos_na_disciplina[i - 1], alunos_na_disciplina[i])
            print(f"Alunos na disciplina '{disciplina}' foram unidos.")
        else:
            print(f"Não há alunos suficientes para unir na disciplina '{disciplina}'.")

    def verificar_mesmo_grupo(self, aluno1, aluno2, disciplina):
        if disciplina not in self.union_find_disciplinas:
            raise ValueError(f"Disciplina '{disciplina}' não encontrada.")
        uf = self.union_find_disciplinas[disciplina]
        return uf.verificar_mesmo_grupo(aluno1, aluno2)

    def exibir_grupo(self, aluno, disciplina):
        if disciplina not in self.union_find_disciplinas:
            raise ValueError(f"Disciplina '{disciplina}' não encontrada.")
        uf = self.union_find_disciplinas[disciplina]
        grupo = uf.exibir_grupo(aluno)
        return grupo


def menu_interativo():
    gd = GerenciadorDisciplinas()

    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Unir alunos por disciplina")
        print("3. Verificar se alunos estão no mesmo grupo")
        print("4. Exibir grupo de um aluno por disciplina")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ").strip()
            disciplinas = input("Disciplinas (separadas por vírgula): ").strip().split(',')
            disciplinas = [disciplina.strip() for disciplina in disciplinas if disciplina.strip()]

            if not disciplinas:
                print("Erro: o aluno deve estar registrado em pelo menos uma disciplina.")
                continue

            gd.adicionar_aluno(nome, disciplinas)
            print(f"Aluno {nome} adicionado com sucesso!")

        elif opcao == "2":
            disciplina = input("Disciplina para unir alunos: ").strip()
            try:
                gd.unir_por_disciplina(disciplina)
            except ValueError as e:
                print(f"Erro: {str(e)}")

        elif opcao == "3":
            aluno1 = input("Nome do primeiro aluno: ").strip()
            aluno2 = input("Nome do segundo aluno: ").strip()
            disciplina = input("Disciplina: ").strip()

            try:
                if gd.verificar_mesmo_grupo(aluno1, aluno2, disciplina):
                    print(f"{aluno1} e {aluno2} estão no mesmo grupo na disciplina {disciplina}.")
                else:
                    print(f"{aluno1} e {aluno2} NÃO estão no mesmo grupo na disciplina {disciplina}.")
            except ValueError as e:
                print(f"Erro: {str(e)}")

        elif opcao == "4":
            aluno = input("Nome do aluno: ").strip()
            disciplina = input("Disciplina: ").strip()

            try:
                grupo = gd.exibir_grupo(aluno, disciplina)
                print(f"Grupo de {aluno} na disciplina {disciplina}:")
                for a in grupo:
                    print(f"  - {a}")
            except ValueError as e:
                print(f"Erro: {str(e)}")

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")


menu_interativo()
