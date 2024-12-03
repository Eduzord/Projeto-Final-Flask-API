from flask import Flask, render_template, jsonify
from pilha_lista import NodoLista,ListaLikes, novoPerfil, Pilha

app = Flask(__name__)

pilha = Pilha()


pilha.inserir_novo("Raquel")

pilha.inserir_novo("Camila")

pilha.inserir_novo("Roberta")

pilha.inserir_novo("Alice")

pilha.inserir_novo("Andrea")

pilha.inserir_novo("Maria")

pilha.inserir_novo("Isabela")

# print(pilha.topo.nome)

# print(pilha)

@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/api/topo', methods=['GET'])
def get_topo():
    topo = pilha.topo.nome if pilha.topo else "A pilha está vazia"
    likes = pilha.Likes.cabeca.nome if pilha.Likes.cabeca else "A lista está vazia"
    return jsonify({"nome": topo, "like":likes})


@app.route('/api/dislike', methods=['POST'])
def desempilhar():
    topo_removido = pilha.dislike()
    if topo_removido:
        return jsonify({"sucesso": True, "valor_removido": topo_removido})
    else:
        return jsonify({"sucesso": False, "mensagem": "A pilha está vazia"}), 400
    
@app.route('/api/like', methods = ['POST','GET'])
def dar_like():
    like = pilha.like()
    if like:
        return jsonify({"sucesso": True, "valor_removido": like})
        
    else:
        return jsonify({"sucesso": False, "mensagem": "A pilha está vazia"}), 400

@app.route('/likes')
def likes():
    return render_template('likes.html')  # Página de destino



if __name__ == '__main__':
    app.run(debug=True)