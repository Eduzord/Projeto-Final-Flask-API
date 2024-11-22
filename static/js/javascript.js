async function carregarDados() {
    try {
        const response = await fetch('/api/topo');
        const data = await response.json();
        document.getElementById('nome').innerText = data.nome;
        document.getElementById('like-nome').innerText = data.like;
    } catch (error) {
        console.error("Erro ao carregar os dados: ", error);
    }
}
// Função para remover o topo da pilha
async function dislike() {
    try {
        const response = await fetch('/api/dislike', {
            method: 'POST', // Requisição POST
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();
        
        if (data.sucesso) {
            ;
            // alert("Elemento removido: " + data.topo_removido);
        } else {
            alert("Erro: " + data.mensagem);
        }

        // Atualiza o topo da pilha após remoção
        carregarDados();
    } catch (error) {
        console.error("Erro ao remover o topo da pilha: ", error);
    }
}

async function like() {
    try{
        const response = await fetch('/api/like', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();

        if (data.sucesso) {
            ;
        } else {
            alert("Erro: " + data.mensagem);
        }

        carregarDados();
    } catch(error) {
        console.error("Erro ao remover o topo da pilha: ", error)
    }
}
window.onload = carregarDados;


