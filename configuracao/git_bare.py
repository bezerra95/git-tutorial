# git_bare_repository_tutorial.py
# Tutorial Didático: Usando um Repositório Bare no Git

# Cenário:
# Um repositório "bare" (nu) é utilizado principalmente para colaboração.
# Ele não contém um diretório de trabalho (working tree) e não é usado para desenvolvimento direto.
# É ideal para configurar um repositório central em um servidor para que múltiplos desenvolvedores possam enviar e buscar alterações.

# Passo 1: Criando um Repositório Bare
# Para criar um repositório bare, use o comando:
# git init --bare nome-do-repositorio.git
# Exemplo:
# No servidor ou local onde você deseja armazenar o repositório central:
"""
git init --bare meu-projeto.git
"""


# Resultado:
# Um novo diretório chamado "meu-projeto.git" será criado.
# Este diretório conterá os arquivos de configuração do Git, mas não terá uma cópia dos arquivos do projeto.

# Passo 2: Clonando o Repositório Bare
# Após criar o repositório bare, os desenvolvedores podem clonar o repositório para suas máquinas locais.
# Exemplo:
"""
git clone caminho/para/meu-projeto.git
"""


# Nota:
# Substitua "caminho/para/meu-projeto.git" pelo caminho completo ou URL do repositório bare.

# Passo 3: Adicionando Arquivos no Repositório Local
# Após clonar, você terá um repositório completo com um diretório de trabalho.
# Adicione arquivos no repositório local:
# Exemplo:
"""
echo "Meu primeiro arquivo" > arquivo.txt
git add arquivo.txt
git commit -m "Adiciona o primeiro arquivo"
"""

# Passo 4: Enviando Alterações para o Repositório Bare
# Use o comando "git push" para enviar as alterações para o repositório bare.
"""
git push origin main
"""

# Nota:
# Substitua "main" pelo nome do branch principal, caso seja diferente.

# Passo 5: Atualizando o Repositório Local a Partir do Repositório Bare
# Para obter as alterações de outros desenvolvedores que enviaram para o repositório bare, use:
"""
git pull origin main
"""

# Nota:
# Substitua "main" pelo nome do branch que deseja atualizar.

# Passo 6: Configurando Permissões
# Certifique-se de que todos os desenvolvedores tenham permissões adequadas no servidor onde está o repositório bare.
# Isso pode envolver:
# - Configurar permissões de leitura/escrita no sistema de arquivos.
# - Usar SSH ou HTTPS para acesso seguro ao repositório.

# Passo 7: Verificando o Histórico no Repositório Bare
# Um repositório bare não possui um diretório de trabalho, mas você ainda pode verificar o histórico de commits.
# Navegue até o repositório bare e execute:
"""
git log
"""

# Nota:
# Para um fluxo colaborativo eficiente, todos os desenvolvedores devem sincronizar regularmente as alterações com o repositório bare.

# Conclusão:
# O repositório bare é uma ferramenta poderosa para colaboração em projetos Git.
# Siga os passos acima para configurar e usar um repositório bare de forma eficaz.

# Fim do Tutorial
