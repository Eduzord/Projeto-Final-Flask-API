## Uma pilha pode ser aplicada num cenário de um App de relacionamento, que põe os perfis dos usuários em uma pilha
## E dependendo da opção do usuário, deslike ou like, descarta o perfil ou move o perfil para uma lista de possiveis "matchs" do usuário
class NodoLista:
    """Esta classe representa um noo ded uma lista encadeada."""

    def __init__(self, nome=" ", proximo_nodo=None):
        self.nome = nome
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.nome, self.proximo)


class ListaLikes:
    "Representa a lista"

    def __init__(self):
        self.cabeca = None

    def insere_inicio(self, novo_dado):
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo

    def remove(self):
        assert self.cabeca, "Impossível remover de lista vazia"
        self.cabeca = self.cabeca.proximo

    def __repr__(self):
        return "[" + str(self.cabeca) +"]"
class novoPerfil:
    """Esta classe representa um nodo de uma estrutura encadeada"""
    def __init__(self, nome = " ", nodo_anterior = None):
        self.nome = nome
        self.anterior = nodo_anterior

    def __repr__(self):
        return "%s -> %s" %(self.nome,self.anterior)

class Pilha:

    def __init__(self):
        self.topo = None
        self.Likes = ListaLikes()

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def inserir_novo(self, nome):
        # Cria um novo nodo com o dado a ser armazenado.

        novo_nodo = novoPerfil(nome)

        # Faz com que o novo nodo seja o topo da pilha.

        novo_nodo.anterior = self.topo

        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo



    def dislike(self):
        assert self.topo, "Impossível remover valor de pilha vazia."
        valor = self.topo.nome
        self.topo = self.topo.anterior
        return valor

    # Remove o perfil da pilha de perfis e o adiciona numa lista de "likes"
    def like(self):
        self.Likes.insere_inicio(self.topo.nome)
        self.topo = self.topo.anterior

    def mostrar_likes(self):
        print(self.Likes)


pilha = Pilha()

# print("Inserindo perfis na pilha de perfis")
# pilha.inserir_novo("Raquel")
#
# pilha.inserir_novo("Camila")
#
# pilha.inserir_novo("Roberta")
# print(f"Perfis inseridos: {pilha} \n ")
#
# print(f"Dando dislike (removendo o último da pilha)" )
# pilha.dislike()
# print(f"Pilha atual")
# print(pilha)
# print("\n")
# pilha.like()
# print(f"Dando like (movendo o último para a lista de likes)")
# print(f"Mostrando a pilha de perfis")
# print(pilha)
# print(f"\n")
# print(f"Mostrando a lista de likes")
# pilha.mostrar_likes()

