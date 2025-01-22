# Tutorial: Trabalhando com Tags no Git

# Cenário: Você está desenvolvendo um software e deseja marcar pontos importantes na história do projeto, como versões estáveis (v1.0, v2.0, etc.) ou momentos significativos no desenvolvimento. As tags ajudam a identificar commits específicos de forma clara e rastreável.

# 1. **Criando uma Tag**
#
# Digamos que você acabou de realizar um commit importante e quer criar uma tag para identificá-lo.
# Primeiro, confirme o estado do repositório:
# git status

# Em seguida, crie a tag:
# git tag v1.0
# "v1.0" é o nome da tag que identifica este commit.

# Para adicionar uma descrição ou mensagem à tag:
# git tag -a v1.0 -m "Primeira versão estável do projeto"

# 2. **Listando Tags Existentes**
#
# Você pode visualizar todas as tags criadas no repositório com o comando:
# git tag

# Para mais detalhes sobre uma tag específica:
# git show v1.0

# 3. **Trabalhando com Tags Retroativas**
#
# Se precisar criar uma tag para um commit antigo, encontre o hash do commit:
# git log --oneline

# Em seguida, crie a tag para o hash especificado:
# git tag v0.9 <hash_do_commit>

# 4. **Subindo Tags para o Repositório Remoto**
#
# Por padrão, as tags não são enviadas ao repositório remoto automaticamente. Para subir uma tag específica:
# git push origin v1.0

# Para subir todas as tags:
# git push --tags

# 5. **Deletando uma Tag**
#
# Para deletar uma tag localmente:
# git tag -d v1.0

# Para deletar uma tag no repositório remoto:
# git push origin --delete v1.0

# 6. **Cenário de Uso**
# Imagine que você esteja trabalhando em uma aplicação e lançou a versão v1.0. Após algumas correções, você decide criar a tag v1.1.
#
# Passo a passo:
# a) Confirme o commit das correções:
# git commit -m "Corrige bugs para versão 1.1"

# b) Crie a tag com descrição:
# git tag -a v1.1 -m "Correções menores e melhorias de performance"

# c) Suba a tag para o repositório remoto:
# git push origin v1.1

# 7. **Comparando Tags**
#
# Para ver as diferenças entre dois commits marcados com tags:
# git diff v1.0 v1.1

# 8. **Checkout de uma Tag**
#
# Você pode fazer checkout de uma tag para analisar o estado do projeto naquele ponto:
# git checkout v1.0
# Note que isso coloca seu repositório em um estado de "detached HEAD". Para voltar ao branch principal:
# git checkout main

# 9. **Automatizando Tags com Versões**
# Se você está em um projeto onde as versões são frequentes, você pode automatizar usando "SemVer". Ferramentas como `npm version` ou `bumpversion` ajudam a gerar tags automaticamente.
