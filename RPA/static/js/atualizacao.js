let arquivosAnteriores = []; // Variável para armazenar o estado anterior dos arquivos

// Função para inicializar os arquivos já existentes na página
function inicializarArquivos() {
    fetch('/api/concluido/')  // URL da API que retorna os dados dos Finished_file
        .then(response => response.json())
        .then(data => {
            // Preenche a lista de arquivos já existentes
            arquivosAnteriores = data.map(file => file.id); // Preenche com os IDs dos arquivos existentes
        })
        .catch(error => console.error('Erro ao inicializar arquivos:', error));
}

function verificarAtualizacao() {
    fetch('/api/concluido/')  // URL da API que retorna os dados dos Finished_file
        .then(response => response.json())
        .then(data => {
            // Verifica se há novos arquivos
            const novosArquivos = data.filter(file => !arquivosAnteriores.includes(file.id)); // Assumindo que cada arquivo tem um ID único

            if (novosArquivos.length > 0) {
                // Se novos arquivos foram encontrados, recarrega a página
                location.reload(); // Atualiza a página
            }

            // Atualiza o estado anterior dos arquivos
            arquivosAnteriores = data.map(file => file.id); // Atualiza a lista de IDs
        })
        .catch(error => console.error('Erro ao verificar atualizações:', error));
}

// Inicializa os arquivos ao carregar a página
window.onload = function() {
    inicializarArquivos(); // Preenche arquivosAnteriores na carga inicial
    setInterval(verificarAtualizacao, 5000); // Verifica a cada 5 segundos
};
