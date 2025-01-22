
# **Tutorial Profissional: Git – Operações Locais**

# Este tutorial cobre operações locais no Git, como configurar nome e e-mail, iniciar um repositório,
# trabalhar com commits e rebase. Ideal para consulta em projetos locais.

# ----------------------------------------------------
# 1. Configuração de Nome e E-mail do Usuário no Git
# ----------------------------------------------------
# O Git utiliza o nome e o e-mail do usuário para identificar quem realizou cada commit.

# Configuração Global:
# Define o nome e o e-mail para todos os repositórios no sistema:
# git config --global user.name "Seu Nome"
# git config --global user.email "seuemail@exemplo.com"

# Configuração Local:
# Define o nome e o e-mail para um repositório específico:
# git config user.name "Nome Local"
# git config user.email "emaillocal@exemplo.com"

# Verificando Configurações:
# Globais: git config --global --list
# Locais: git config --list

# ----------------------------------------------------
# 2. Inicializando um Repositório Local
# ----------------------------------------------------
# Para começar a usar o Git em um projeto local:
# git init

# Após inicializar:
# 1. Adicione arquivos para o controle de versão:
#    git add nome-do-arquivo  # ou git add .
# 2. Faça o commit inicial:
#    git commit -m "Mensagem do commit"

# ----------------------------------------------------
# 3. Trabalhando com Commits
# ----------------------------------------------------
# Adicionando Arquivos ao Stage:
# git add nome-do-arquivo  # Adiciona arquivos específicos
# git add .  # Adiciona todos os arquivos modificados

# Criando Commits:
# git commit -m "Mensagem descrevendo as alterações"

# Modificando o Último Commit:
# Para ajustar a mensagem ou adicionar arquivos ao último commit:
# git commit --amend -m "Nova mensagem"

# ----------------------------------------------------
# 4. Uso Profissional do Comando `git rebase`
# ----------------------------------------------------
# O rebase reescreve o histórico de commits e ajuda a alinhar branches de forma linear.

# Rebase em Relação a Outra Branch:
# git checkout sua-branch
# git rebase main
# Isso aplica os commits de `sua-branch` sobre os commits mais recentes da branch `main`.

# Rebase Interativo:
# Para editar, combinar ou reorganizar commits:
# git rebase -i HEAD~n  # Substitua `n` pelo número de commits que deseja revisar.

# Resolvendo Conflitos Durante o Rebase:
# 1. Resolva os conflitos nos arquivos afetados.
# 2. Marque os arquivos como resolvidos:
#    git add nome-do-arquivo
# 3. Continue o rebase:
#    git rebase --continue

# Cancelando um Rebase:
# Para cancelar o processo e voltar ao estado anterior:
# git rebase --abort

# ----------------------------------------------------
# Boas Práticas Locais
# ----------------------------------------------------
# - Realize commits frequentes com mensagens claras.
# - Use rebase para manter o histórico limpo, mas evite em branches compartilhadas.
# - Sempre sincronize seu trabalho local com as alterações remotas antes de usar merge ou rebase.

# ----------------------------------------------------
# Fim do Tutorial Local
