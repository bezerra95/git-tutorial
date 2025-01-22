# delete_tutorial.py
# Tutorial: Deletando Arquivos no Git

# No Git, o comando para remover arquivos do repositório é `git rm`.
# Esse comando remove o arquivo tanto do sistema de arquivos quanto do índice do Git, preparando a remoção para o próximo commit.

# 1. Deletar um Arquivo
# Para remover um arquivo do repositório, use o comando:
# git rm nome-do-arquivo

# Exemplo:
# git rm arquivo_a_ser_deletado.txt

# 2. Deletar um Arquivo Sem Remover do Sistema de Arquivos
# Se você quiser remover o arquivo do Git, mas mantê-lo no seu diretório local, use a opção `--cached`:
# git rm --cached nome-do-arquivo

# 3. Deletar um Arquivo com a Força (se ele estiver modificado)
# Se o arquivo foi modificado e você quer forçar a remoção, pode usar a opção `-f` (force):
# git rm -f nome-do-arquivo

# 4. Verificar as Alterações
# Após remover um arquivo, você pode verificar as mudanças com:
# git status
# O Git mostrará que o arquivo foi removido.

# 5. Commitando a Remoção
# Para confirmar a remoção, é necessário fazer o commit das alterações:
# git commit -m "Removendo o arquivo 'arquivo_a_ser_deletado.txt' do repositório"

# 6. Remover um Diretório
# Da mesma forma que arquivos individuais, você pode remover um diretório inteiro:
# git rm -r nome-do-diretorio

# 7. Cancelando a Remoção (Se ainda não cometeu)
# Se você removeu um arquivo, mas ainda não fez o commit, pode cancelar a remoção com:
# git checkout -- nome-do-arquivo
