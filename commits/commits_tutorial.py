# 1. **Commits**
"""
Um commit é um ponto no tempo no qual você salva o estado do repositório.
Cada commit contém um registro de todas as mudanças feitas nos arquivos do repositório desde o último commit.

Para criar um commit:
1. Faça alterações no repositório.
2. Adicione essas mudanças ao stage (veja a seção **Stage**).
3. Confirme as mudanças com `git commit`.

Cada commit tem:
- Um identificador único (hash).
- Uma mensagem que descreve as alterações.

### Comando para criar um commit:
git commit -m "Descrição das mudanças"
```

### Corrigindo o último commit:
Se você esquecer de adicionar algo ou quiser editar a mensagem do último commit:
git commit --amend -m "Nova descrição das mudanças"
```
Isso reescreve o último commit com as mudanças atuais no stage e uma nova mensagem, se especificada.
---
"""

# 2. **Stage (Índice)**
"""
O stage, ou índice, é onde você coloca as mudanças antes de fazer um commit. 
Ele funciona como uma área intermediária para preparar as alterações.

### Comando para adicionar mudanças ao stage:
- Para um arquivo específico:
  git add nome-do-arquivo
  ```
- Para todos os arquivos alterados:
  git add .
---
"""

# 3. **Verificar Diferenças**
"""
### Entre Stage e o Último Commit:
Para comparar o que está no stage com o último commit:
git diff --cached
```

### Entre Dois Commits:
Você pode comparar dois commits para ver as mudanças entre eles:
git diff <commit-hash-1> <commit-hash-2>
```

### Entre Working Directory e Stage:
Se você fez alterações nos arquivos e deseja ver o que mudou em relação ao que está no stage:
git diff
---
"""

# 4. **Histórico de Commits**
"""
### Visualizar o Histórico Completo:
git log

### Resumo Compacto (uma linha por commit):
git log --oneline

### Histórico com Gráfico de Branches:
git log --graph --oneline --all
---
"""

# 5. **Revertendo Mudanças**
"""
### Reverter o Último Commit (mantendo as mudanças no stage):
git reset --soft HEAD~1
```
### Resetar ao Estado de um Commit Específico:
git reset --hard <hash-do-commit>

### Criar um Novo Commit Revertendo um Commit Anterior:
Isso mantém o histórico intacto, criando um novo commit que desfaz as mudanças de um commit específico:
git revert <hash-do-commit>
---
"""

# 6. **Visualização do Histórico**
"""
Podemos ver o histórico de commits em uma representação visual com:
git log --graph --oneline --all
```
### Explicação dos Símbolos:
- `*`: Indica um commit específico no histórico.
- `(branch_name)`: Indica o branch e a origem relacionados ao commit.
- `|`: Linha de continuidade do branch atual.
- `|/` ou `|\`: Ponto de junção ou separação de branches.
- `Merge branch 'nome-do-branch' into 'main'`: Indica a união de um branch secundário com o branch principal (`main`).
"""