from flask import Flask, render_template, jsonify
from pilha_lista import NodoLista,ListaLikes, novoPerfil, Pilha

app = Flask(__name__)

pilha = Pilha()


pilha.inserir_novo("Raquel")

pilha.inserir_novo("Camila")

pilha.inserir_novo("Roberta")

# print(pilha.topo.nome)

# print(pilha)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/topo', methods=['GET'])
def get_topo():
    topo = pilha.topo.nome if pilha.topo else "A pilha está vazia"
    return jsonify({"nome": topo})


@app.route('/api/dislike', methods=['POST'])
def desempilhar():
    topo_removido = pilha.dislike()
    if topo_removido:
        return jsonify({"sucesso": True, "valor_removido": topo_removido})
    else:
        return jsonify({"sucesso": False, "mensagem": "A pilha está vazia"}), 400



if __name__ == '__main__':
    app.run(debug=True)