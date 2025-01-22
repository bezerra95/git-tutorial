# Para desfazer o commit que você acabou de realizar e voltar
# ao estado anterior, siga os passos abaixo:

# Desfaça o último commit (mantendo as alterações no stage):
# Execute o comando abaixo para desfazer o commit, mas preservar
# as mudanças que foram adicionadas ao stage:


# Copiar código
# git reset --soft HEAD~1
# Isso reverterá o commit, mas as alterações continuarão
# prontas para serem commitadas novamente, caso necessário.

# Verifique o status: Confirme que as alterações ainda estão no stage:

#Copiar código
# git status
# #Remova as alterações do stage (se necessário): Para remover
# os arquivos do stage e devolvê-los ao estado de alterações não rastreadas:

# Copiar código
# git restore --staged .
# Confirme que o repositório voltou ao estado correto:
# Após restaurar, verifique o status novamente:

# Copiar código
# git status