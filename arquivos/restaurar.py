# 1. **O que é o `git restore`?**
# O comando `git restore` é usado para descartar alterações em arquivos ou restaurar arquivos para um estado anterior.
# Ele substitui parte das funções do comando `git checkout` e é mais específico para restaurações.

# 2. **Descartar Alterações no Working Directory**
# Se você fez alterações em um arquivo e quer descartá-las antes de adicioná-las ao stage:
# git restore nome-do-arquivo
# Exemplo:
# git restore main.py

# 3. **Descartar Alterações em Todos os Arquivos**
# Para desfazer alterações em todos os arquivos não comitados:
# git restore .
# Isso reverte o estado de todos os arquivos no working directory para o último commit.

# 4. **Restaurar Arquivos do Stage**
# Se você adicionou um arquivo ao stage com `git add` mas quer removê-lo sem perder as alterações:
# git restore --staged nome-do-arquivo
# Exemplo:
# git restore --staged main.py

# 5. **Restaurar Arquivos para um Commit Específico**
# Você pode restaurar um arquivo para o estado em um commit anterior.
# Use o hash do commit para isso:
# git restore --source=<hash-do-commit> nome-do-arquivo
# Exemplo:
# git restore --source=abc123 main.py

# 6. **Restaurar Arquivos Específicos do Repositório**
# Para restaurar um arquivo completamente removido do repositório, use:
# git restore --source=HEAD nome-do-arquivo
# Exemplo:
# git restore --source=HEAD config.json

# 7. **Descartar Alterações e Confirmações (Cuidado!)**
# Para desfazer alterações permanentemente (sem enviar para o stash ou stage), use:
# git restore nome-do-arquivo
# Atenção: Esse comando descarta mudanças sem chance de recuperação.

# 8. **Opções Úteis do `git restore`**
# - `--source=<commit>`: Escolhe um commit específico como base para a restauração.
# - `--staged`: Remove o arquivo do stage, mas mantém as alterações no working directory.
# - `--worktree`: Aplica as mudanças diretamente no diretório de trabalho.

# 9. **Diferença Entre `git restore` e `git reset`**
# - `git restore`: Focado em restaurar arquivos individuais ou suas alterações.
# - `git reset`: Reverte o estado do repositório inteiro (pode afetar o stage e commits).

# 10. **Exemplos Práticos**
# - **Exemplo 1**: Descartar alterações locais em todos os arquivos:
# git restore .
#
# - **Exemplo 2**: Remover um arquivo do stage, mas manter as alterações no working directory:
# git restore --staged main.py
#
# - **Exemplo 3**: Restaurar um arquivo para o estado do último commit:
# git restore main.py
#
# - **Exemplo 4**: Restaurar um arquivo para um commit anterior:
# git restore --source=abc123 main.py


# Tutorial: Usando `git checkout` para Refazer Alterações no Git

# 1. **O que é `git checkout`?**
# O comando `git checkout` é usado para:
# - Navegar entre branches.
# - Restaurar arquivos para um estado anterior.
# - Reverter o estado de todo o working directory.

# 2. **Descartar Alterações em um Arquivo**
# Se você fez alterações em um arquivo e quer restaurá-lo para o estado do último commit:
# git checkout nome-do-arquivo
# Exemplo:
# git checkout main.py

# 3. **Descartar Alterações em Todos os Arquivos**
# Para desfazer alterações em todos os arquivos do working directory:
# git checkout .
# Isso restaura todos os arquivos para o estado do último commit.

# 4. **Refazer um Arquivo Deletado**
# Se você deletou um arquivo do working directory, mas ele ainda está no último commit:
# git checkout HEAD nome-do-arquivo
# Exemplo:
# git checkout HEAD config.json

#Reverter ao Último Commit Confirmado no Branch Atual
#Se você fez alterações, mas não as confirmou, e quer voltar para o último commit confirmado, você pode usar:
# Exemplo:
#git reset --hard HEAD

# 5. **Refazer o Working Directory para um Commit Específico**
# Se você quer restaurar o working directory inteiro para um commit anterior:
# git checkout <hash-do-commit>
# Isso muda todo o projeto para o estado do commit escolhido.
# Exemplo:
# git checkout abc123

# Atenção: Essa ação coloca o repositório em estado "detached HEAD".
# Para voltar ao branch principal depois, use:
# git checkout main

# 6. **Refazer um Arquivo para um Commit Específico**
# Para restaurar um arquivo específico para o estado de um commit anterior:
# git checkout <hash-do-commit> -- nome-do-arquivo
# Exemplo:
# git checkout abc123 -- main.py

# 7. **Refazer Alterações Sem Perder as Mudanças no Stash**
# Se você quer salvar alterações antes de refazer, use `git stash`:
# git stash
# Em seguida, restaure os arquivos:
# git checkout .
# Depois, recupere suas mudanças com:
# git stash pop

# 8. **Descartar Alterações em Branches**
# Para descartar alterações locais em um branch e voltar ao último commit:
# git checkout nome-do-branch
# Exemplo:
# git checkout main

# 9. **Migrar para um Branch e Restaurar Alterações**
# Se você está em um branch e deseja recomeçar o trabalho:
# git checkout nome-do-branch
# git checkout .
# Agora você pode recomeçar com o branch limpo.

# 10. **Evite Confusões:**
# - `git checkout` funciona para restaurar arquivos e mudar de branch.
# - Para uso exclusivo de restauração de arquivos, prefira o comando moderno `git restore`.

# Exemplo Prático: Refazer o Último Commit
# 1. Faça alterações em um arquivo (ex: `main.py`).
# 2. Para desfazer as mudanças:
# git checkout main.py
#
# 3. Para desfazer em todos os arquivos:
# git checkout .

# Lembre-se: `git checkout` descarta alterações sem salvar. Use com cuidado!
