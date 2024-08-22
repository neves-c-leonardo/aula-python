# Comandos Git

### Link GitHub:
- github.com.br

### Clonar o repositório criado no GitHub (Vai rodar somente 1 vez)
- git clone <url.repositorio>

### Fazer Login no Git Bash
- git config --global user.name "NOME_USUARIO"
- git config --global user.email "EMAIL@EMAIL.COM"

### Comando para verificar o status do projeto, validar se existe arquivo criado/deletado/modificado, sempre usar para toda ação para ver como esta o status do projeto
- git status

### Adicionar arquivo a fila para commit. Com '.' ele adiciona todos os arquivos modificados, se quiser colocar na fila somente arquivo especifico é só digitar o arquivo. (git add README.md)
- git add . 

### Enviar arquivo para a linha de envio ao GitHub
- git commit -m 'DESCRIÇÃO DO COMMIT'

### Processar o commit no GitHub
- git push

# Comandos fora do Git

### Abrir o VSCODE
- code . 

### Entrar em pasta
- cd <nome-pasta>

### Sair da pasta
- cd .

# Sequencia padrão Git
- git status
- git add .
- git commit -m 'DESCRIÇÃO DO COMMIT'
- git push