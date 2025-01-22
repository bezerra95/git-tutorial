# 1. **Introdução aos Branches**
# Branches permitem trabalhar em funcionalidades separadas
# ou testar código sem impactar o branch principal.
# Geralmente, o branch principal é chamado de `main` ou `master`.


# 2. **Criar um Novo Branch**
# Para criar um novo branch:
# git branch nome-do-branch
# Exemplo:
# git branch nova-funcionalidade


# 3. **Listar Branches**
# Para ver todos os branches no repositório:
# git branch
# Branches com um `*` indicam o branch atual.


# 4. **Alternar Entre Branches**
# Para mudar para outro branch:
# git checkout nome-do-branch
# Ou, com o comando mais moderno:
# git switch nome-do-branch


# 5. **Criar e Mudar para um Novo Branch**
# Combine criação e troca de branch em um único comando:
# git checkout -b nome-do-branch
# Ou:
# git switch -c nome-do-branch

# 5.1 **Ver nome da branch atual
# git rev-parse --abbrev-ref HEAD

# 6. **Excluir um Branch**
# Para excluir um branch que não é mais necessário:
# git branch -d nome-do-branch
# Use `-D` para forçar a exclusão:
# git branch -D nome-do-branch


# 7. **Salvar Alterações Temporárias (Stash)**
# Para salvar alterações atuais sem fazer um commit:
# git stash
# Isso limpa o diretório de trabalho e permite alternar para outro branch.
# Para recuperar as alterações:
# git stash pop
# Para listar stashes salvos:
# git stash list


# 8. **Mesclar Branches**
# Para integrar alterações de outro branch no branch atual:
# git merge nome-do-branch
# Resolva conflitos manualmente se necessário, e finalize o merge com:
# git commit


# 9. **Comparar Branches**
# Para verificar as diferenças entre dois branches:
# git diff nome-do-branch-1 nome-do-branch-2
# Exemplo:
# git diff main nova-funcionalidade


# 10. **Renomear um Branch**
# Para renomear o branch atual:
# git branch -m novo-nome
# Para renomear um branch específico:
# git branch -m nome-antigo novo-nome


# 11. **Trabalhar com o Branch Principal**
# Para mudar para o branch principal (`main` ou `master`):
# git checkout main   # ou git checkout master
# Ou:
# git switch main     # ou git switch master


# 12. **Definir o Branch Padrão**
# Para definir `main` como o branch principal:
# git branch -M main


# 13. Trabalhar com o Branch Principal
# Para mudar para o branch principal ("main" ou "master"):
# git checkout main   # ou git checkout master
# Ou:
# git switch main     # ou git switch master


# 14. Definir o Branch Padrão
# Para definir "main" como o branch principal:
# git branch -M main


# 15. Entendendo o Git Rebase
# O `git rebase` é um comando usado para reaplicar commits de um branch em cima de outro,
# reorganizando o histórico. Ele é útil para manter um histórico linear, facilitando
# a leitura e entendimento do código.

#Exemplo Prático:

# Cenário:
# Você tem dois branches: `feature` e `main`. No branch `feature`,
# você fez alguns commits enquanto o branch `main`
# foi atualizado com novos commits.
# Agora você quer aplicar os commits do branch `feature` no topo do branch `main`.

# Certifique-se de estar no branch "feature":
# git checkout feature

# Execute o rebase com o branch "main":
# git rebase main

#Isso reaplicará os commits do branch `feature` no topo do branch `main`.

# Resolver conflitos (se existirem):
# Durante o rebase, pode ocorrer conflitos. Se isso acontecer:
# - Edite os arquivos conflitantes para resolver os problemas.
# - Depois, marque o conflito como resolvido:

# git add <arquivo-conflitante>

# - Continue o rebase com:

#  git rebase --continue

# Se precisar cancelar o rebase em andamento:
#  git rebase --abort

###################################################################################################################

# Tutorial: Como Usar o Comando git pull no Git

# O comando git pull é usado para sincronizar seu repositório local
# com o repositório remoto. Ele faz o download das alterações
# do repositório remoto e tenta mesclá-las no branch atual.

# Cenário:
# Imagine que você está trabalhando em um projeto em equipe.
# Seus colegas fizeram alterações no branch remoto, e você precisa
# trazê-las para o seu repositório local antes de continuar.

# Passo 1: Certifique-se de que está no branch correto
# Antes de executar o comando git pull, verifique em qual branch
# você está trabalhando:
# git status

# Para mudar para o branch desejado, use:
# git checkout nome-do-branch   # ou
# git switch nome-do-branch

# Passo 2: Execute o git pull
# Para baixar e mesclar as alterações do branch remoto no branch atual:
# git pull origin nome-do-branch

# Se você estiver no branch principal (main ou master):
# git pull origin main
# ou
# git pull origin master

# O git pull faz dois passos internamente:
# 1. git fetch: Baixa as alterações do repositório remoto.
# 2. git merge: Mescla as alterações no branch atual.

# Passo 3: Resolva conflitos, se houver
# Se houver conflitos durante o git pull, o Git informará os arquivos
# que precisam ser resolvidos manualmente.
# - Edite os arquivos para corrigir os conflitos.
# - Após resolver, adicione os arquivos corrigidos:
#   git add arquivo1 arquivo2
# - Finalize a mesclagem:
#   git commit -m "Resolve conflitos durante o pull"

# Observação: Caso você não queira que o git pull execute a mesclagem automaticamente,
# use o comando fetch separadamente:
# git fetch origin nome-do-branch
# Depois, faça a mesclagem manualmente:
# git merge origin/nome-do-branch

# Dica adicional:
# Se você quiser manter seu branch sempre atualizado,
# faça o git pull regularmente, especialmente antes de iniciar novas alterações.
