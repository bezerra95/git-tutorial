# rename_tutorial.py
# Tutorial: Renomeando Arquivos no Git

# O Git possui um comando específico para renomear arquivos, chamado `git mv`.
# Esse comando não só renomeia o arquivo no sistema de arquivos, mas também registra essa alteração no índice do Git.

# 1. Renomear um Arquivo
# Para renomear um arquivo, basta usar o comando:
# git mv nome-antigo nome-novo

# Exemplo:
# git mv arquivo_antigo.txt arquivo_novo.txt

# 2. Renomear um Diretório
# Também é possível renomear um diretório da mesma maneira.
# Basta mover o diretório para um novo nome, e o Git tratará isso como uma renomeação:
# git mv antigo-diretorio novo-diretorio

# 3. Verificar as Alterações
# Após renomear um arquivo, você pode verificar as mudanças com:
# git status
# O Git mostrará que o arquivo foi renomeado.

# 4. Commitando a Renomeação
# Para confirmar a renomeação, é necessário fazer o commit das alterações:
# git commit -m "Renomeando arquivo de 'arquivo_antigo.txt' para 'arquivo_novo.txt'"

# 5. Renomeando Arquivos ou Diretórios Manualmente
# Caso você tenha renomeado ou movido arquivos manualmente (fora do Git), pode usar o comando `git add` para registrar as mudanças.
# git add nome-novo
# git rm nome-antigo
# git commit -m "Renomeando arquivo manualmente"
