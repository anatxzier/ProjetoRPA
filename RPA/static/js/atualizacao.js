let arquivosAnteriores = []; // Variável para armazenar o estado anterior dos arquivos
let erroAnteriorData = document.getElementById('erro-data') ? document.getElementById('erro-data').textContent.trim() : null; // Pega a data do erro renderizada no template
console.log('Erro anterior data:', erroAnteriorData);


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
        .catch(error => console.error('Erro ao verificar atualizações de arquivos:', error));
}

// Função para formatar a data no formato yyyy-mm-dd-hh-minmin
function formatarDataParaPadrão(data) {
    const date = new Date(data);
    const ano = date.getFullYear();
    const mes = String(date.getMonth() + 1).padStart(2, '0');
    const dia = String(date.getDate()).padStart(2, '0');
    const hora = String(date.getHours()).padStart(2, '0');
    const minuto = String(date.getMinutes()).padStart(2, '0');

    return `${ano}-${mes}-${dia}-${hora}-${minuto}`;
}

// Função para verificar novo erro
function verificarAtualizacaoErro() {
    fetch('/api/erro/')  // URL da API que retorna os dados do erro mais recente
        .then(response => response.json())
        .then(data => {
            if (data && data.length > 0) {
                // Pegando a data do erro mais recente da API
                const erroAtualData = new Date(data[0].data_criacao); // A API retorna a data no formato ISO 8601
                // console.log('Erro atual data (sem segundos):', formatarDataParaPadrão(erroAtualData));

                // Verifica se erroAnteriorData tem valor
                if (erroAnteriorData) {
                    try{// Converte erroAnteriorData (do template) para o formato de Date
                        const dataParts = erroAnteriorData.split(' ')[0].split('/'); // Parte da data (dd/mm/yyyy)
                        const timeParts = erroAnteriorData.split(' ')[1].split(':'); // Parte da hora (hh:mm)
    
                        if (dataParts.length === 3 && timeParts.length === 2) {
                            // Converte erroAnteriorData para o formato ISO 8601 (yyyy-mm-ddTHH:mm:ss)
                            const erroAnteriorDate = new Date(
                                `${dataParts[2]}-${dataParts[1]}-${dataParts[0]}T${timeParts[0]}:${timeParts[1]}:00`
                            );
    
                            // console.log('Erro anterior data (sem segundos):', formatarDataParaPadrão(erroAnteriorDate));
    
                            // Comparação entre as datas (sem segundos)
                            if (formatarDataParaPadrão(erroAtualData) > formatarDataParaPadrão(erroAnteriorDate)) {
                                console.log('Novo erro encontrado, recarregando página...');
                                location.reload(); // Atualiza a página para exibir o erro mais recente
                            } else {
                                console.log('Erro atual não é mais recente.');
                            }
                        } else {
                            console.error('Formato de data inválido:', erroAnteriorData);
                        }}catch{
                            if (formatarDataParaPadrão(erroAtualData) > formatarDataParaPadrão(erroAnteriorData)) {
                                console.log('Novo erro encontrado, recarregando página...');
                                location.reload(); // Atualiza a página para exibir o erro mais recente
                            } else {
                                console.log('Erro atual não é mais recente.');
                            }
                        }
                    
                } else {
                    if (erroAtualData){
                        location.reload();
                    }else{
                        console.log('Não existe erro')
                    }
                }

                // Atualiza a data anterior com a data do erro mais recente
                erroAnteriorData = erroAtualData;
            }
        })
        .catch(error => console.error('Erro ao verificar atualizações de erro:', error));
}

// Inicializa arquivos e erro ao carregar a página
window.onload = function() {
    inicializarArquivos(); // Preenche arquivosAnteriores na carga inicial


    // Verifica a cada 5 segundos para arquivos e erros
    setInterval(verificarAtualizacao, 5000); // Verifica a cada 5 segundos para arquivos
    setInterval(verificarAtualizacaoErro, 5000); // Verifica a cada 5 segundos para erros
};
