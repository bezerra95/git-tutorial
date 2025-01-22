# Tutorial: Criando um Repositório no GitHub com README.md

# 1. **Acessar sua conta no GitHub**
#    - Abra o navegador e acesse: https://github.com
#    - Faça login na sua conta.


# 2. **Criar um novo repositório**
#    - No canto superior direito da página, clique no botão com um ícone de "+".
#    - Escolha "New repository" (Novo repositório).


# 3. **Preencher os detalhes do repositório**
#    - **Repository name (Nome do Repositório):** Escolha um nome único e representativo.
#      Exemplo: "meu-projeto-exemplo".
#    - **Description (Descrição):** Opcional, mas ajuda a explicar o propósito do repositório.
#      Exemplo: "Este é um exemplo de repositório com README inicializado".
#    - **Public ou Private:** Escolha se o repositório será público (qualquer pessoa pode ver)
#      ou privado (somente você e colaboradores autorizados podem ver).


# 4. **Adicionar o arquivo README.md**
#    - Marque a caixa "Add a README file" (Adicionar um arquivo README).
#      - Isso criará um arquivo básico para descrever o repositório.


# 5. **Selecionar uma licença (Opcional)**
#    - Se necessário, escolha uma licença adequada para o seu projeto em "Add a license".
#    - Isso adicionará um arquivo LICENSE ao repositório.


# 6. **Criar o repositório**
#    - Clique no botão "Create repository" (Criar repositório).
#    - Pronto! Seu repositório está criado e contém um arquivo README.md inicializado.


# 7. **Editar o arquivo README.md**
#    - No seu editor de texto ou IDE, abra o arquivo README.md.
#    - Adicione informações sobre o projeto:
#      ```
#      # Meu Projeto Exemplo
#      Este é um exemplo de como criar e inicializar um repositório com README.md.
#      ```


# 8. **Fazer alterações e enviar para o GitHub**
#    - Após editar o README.md, salve o arquivo e envie as alterações:
#      git init
#      git add README.md
#      git commit -m "Atualizar README com informações do projeto"
#      git remote add origin `https://github.com/seu-usuario/meu-projeto-exemplo.git`.
#      git push -u origin master
#    - **Dica:** Durante o comando `git push -u origin`, você pode ser solicitado a fornecer
#      o nome de usuário e a senha do GitHub.
#      - **Nome de Usuário:** Digite seu nome de usuário do GitHub. = "git config user.name "julio"
#      - **Senha:** Digite sua senha do GitHub ou, se estiver usando autenticação = "git config user.senha "123"
#        baseada em tokens, insira o **Token de Acesso Pessoal** no lugar da senha.
#      - Dica para autenticação via token:
#        - No GitHub, acesse **Settings > Developer settings > Personal Access Tokens**.
#        - Gere um token com as permissões necessárias e use-o no lugar da senha.


# 9. **Clonar o repositório (Opcional, para usar localmente)**
#    - Copie a URL do repositório (HTTPS, SSH ou GitHub CLI):
#      - No GitHub, acesse a página do repositório que você deseja clonar.
#      - Clique no botão verde "Code" no canto superior direito.
#      - Escolha o método de clonagem:
#        - HTTPS: Exemplo de URL: `https://github.com/seu-usuario/meu-projeto-exemplo.git`.
#        - SSH: Exemplo de URL: `git@github.com:seu-usuario/meu-projeto-exemplo.git`.
#        - GitHub CLI: Exemplo de comando: `gh repo clone seu-usuario/meu-projeto-exemplo`.

#    - No terminal, navegue até o diretório onde deseja salvar o repositório localmente:
#      Exemplo:
#      cd /caminho/para/o/diretorio

#    - Use o comando para clonar o repositório:
#      git clone <URL_DO_REPOSITORIO>
#      - Substitua `<URL_DO_REPOSITORIO>` pela URL copiada.

#    - Exemplo com HTTPS:
#      git clone https://github.com/seu-usuario/meu-projeto-exemplo.git

#    - Verificar se já está vinculado
#    - git remote -v   "Se estiver a mensagem é "nothing to commit, working tree clean"

#  Caso precise registrar usuario:
#       "git config user.name "julio"
#       "git config user.senha "123"
#        baseada em tokens, insira o **Token de Acesso Pessoal** no lugar da senha.

#    - Após executar o comando, você verá a mensagem:
#      "Cloning into 'meu-projeto-exemplo'..."
#      Isso indica que o repositório está sendo copiado para o seu computador.

#    - Quando o processo for concluído, entre no diretório clonado:
#      cd meu-projeto-exemplo

#    - Pronto! O repositório foi clonado e você pode começar a trabalhar nele localmente.


# Front-end:git remote

#    - No terminal, navegue até o diretório onde deseja salvar o repositório localmente:
#      Exemplo:
#      cd /caminho/para/o/diretorio

#    - Use o comando para clonar o repositório:
#      git clone <URL_DO_REPOSITORIO>it
#      - Substitua `<URL_DO_REPOSITORIO>` pela URL copiada.

#    - Exemplo com HTTPS:
#      git clone https://github.com/seu-usuario/meu-projeto-exemplo.git

#    - Verificar se já está vinculado
#    - git remote -v   "Se estiver a mensagem é "nothing to commit, working tree clean"

#  Caso precise registrar usuario:
#       "git config user.name "julio"
#       "git config user.senha "123"
#        baseada em tokens, insira o **Token de Acesso Pessoal** no lugar da senha.

#    - Após executar o comando, você verá a mensagem:
#      "Cloning into 'meu-projeto-exemplo'..."
#      Isso indica que o repositório está sendo copiado para o seu computador.

#    - Quando o processo for concluído, entre no diretório clonado:
#      cd meu-projeto-exemplo
#      pnpm install
#      pnpm dev

#    - Pronto! O repositório foi clonado e você pode começar a trabalhar nele localmente.

