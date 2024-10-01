// Funções de abertura e fechamento do modal
function openModal(modalId) {
    console.log('Abrindo modal:', modalId);
    document.getElementById(modalId).style.display = 'block';
    document.body.style.overflow = 'hidden'; // Desabilita o scroll do fundo
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
    document.body.style.overflow = ''; // Habilita o scroll do fundo
}

// Fecha o modal ao clicar fora dele
window.onclick = function(event) {
    const modals = document.getElementsByClassName('modal');
    for (let i = 0; i < modals.length; i++) {
        if (event.target === modals[i]) {
            closeModal(modals[i].id);
        }
    }
}

// Função para alternar detalhes do usuário
function toggleDetails(contentId, arrowId) {
    var content = document.getElementById(contentId);
    var arrow = document.getElementById(arrowId);
    
    // Verifica se o conteúdo está escondido
    var isHidden = window.getComputedStyle(content).display === "none";

    if (isHidden) {
        // Se estiver escondido, mostra o conteúdo
        content.style.display = "block";
        arrow.textContent = "▲"; // Altera o símbolo da seta
    } else {
        // Se estiver visível, esconde o conteúdo
        content.style.display = "none";
        arrow.textContent = "▼"; // Altera o símbolo da seta
    }
}

// Código a ser executado quando o DOM estiver completamente carregado
document.addEventListener('DOMContentLoaded', function () {
    // Função para exibir a seta de voltar (a seta sempre estará visível)
    function showBackArrow() {
        document.getElementById('backArrow').style.display = 'block'; // Exibe a seta (garantido)
    }

    // Função para resetar os cards (a seta continuará visível após o reset)
    function resetCards() {
        const userCards = document.querySelectorAll('.user-card');
        userCards.forEach(function (card) {
            card.style.display = 'block'; // Exibe todos os cards
        });

        // Remove a mensagem de "nenhum resultado", se estiver visível
        document.getElementById('noResultsMessage').style.display = 'none';
        document.getElementById('searchInput').value = ''; // Limpa o campo de pesquisa
    }

    // Adicionar evento de clique à seta de voltar (não oculta a seta)
    document.getElementById('backArrow').addEventListener('click', function () {
        resetCards(); // Reseta os resultados, mas a seta continua visível
    });

    // Adicionar evento de clique ao botão de pesquisa
    document.getElementById('searchBtn').addEventListener('click', function () {
        filterUsers(); // Filtra os usuários
        showBackArrow(); // Sempre exibe a seta de voltar após a pesquisa
    });

    // Adicionar evento de input ao campo de pesquisa
    document.getElementById('searchInput').addEventListener('input', function () {
        filterUsers(); // Filtra os usuários conforme o texto digitado
        showBackArrow(); // Sempre exibe a seta de voltar ao digitar na pesquisa
    });

    // Função para filtrar os usuários
    function filterUsers() {
        const searchText = document.getElementById('searchInput').value.toLowerCase().trim();
        const userCards = document.querySelectorAll('.user-card');
        let hasResults = false;

        userCards.forEach(function (card) {
            const userName = card.querySelector('.user-details h3').textContent.toLowerCase();

            if (userName.includes(searchText)) {
                card.style.display = 'block'; // Exibe o card se o nome corresponder
                hasResults = true;
            } else {
                card.style.display = 'none'; // Oculta o card se o nome não corresponder
            }
        });

        // Exibe a mensagem "nenhum resultado" se nenhum usuário for encontrado
        if (!hasResults) {
            document.getElementById('noResultsMessage').style.display = 'block';
        } else {
            document.getElementById('noResultsMessage').style.display = 'none';
        }
    }

    // Exibe a seta de voltar ao carregar a página
    showBackArrow();
});


