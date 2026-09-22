# 1. Inicializa o repositório Git local
git init

# 2. Adiciona todos os arquivos ao histórico
git add .

# 3. Cria o primeiro ponto de salvamento (commit)
git commit -m "feat: adiciona simulador de forca bruta com contador de progresso"

# 4. Define a ramificação principal como 'main'
git branch -M main

# 5. Vincula o seu código ao link do seu repositório do GitHub 
# (Substitua o LINK_DO_SEU_REPOSITORIO pelo link real criado no GitHub)
git remote add origin LINK_DO_SEU_REPOSITORIO

# 6. Envia os arquivos definitivamente para a nuvem
git push -u origin main
