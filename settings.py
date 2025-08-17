URLS = { 
    'url_google': 'https://images.google.com',
}

VARIAVEIS_GERAIS ={
    'pasta': 'ProjetoPY',
    'nome_arquivo': 'Cachorro.jpg',
    'pesquisa': 'Cachorro engracado'
}

XPATH = {
    'input_pesquisa': '/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea',
    'input_imagem_pequena': '/html/body/div[3]/div/div[15]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div[2]/h3/a/div/div/div/g-img/img',
    'input_imagem_baixar': '/html/body/div[14]/div[2]/div[3]/div/div/c-wiz/div/div[2]/div[2]/div/div[2]/c-wiz/div/div[2]/div[1]/a/img[1]'
}

TIPOS = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.txt', '.docx', '.doc'],
    'Planilhas': ['.xlsx', '.csv'],
    'PDFs': ['.pdf'],
    'Compactados': ['.zip', '.rar'],
    'Executáveis': ['.exe'],
    'Python': ['.py'],
    'Outros': [] #*  se nao for nem um dos outras opcoes
    }