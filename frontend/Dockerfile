# Etapa 1: Construção
FROM node:14 as build

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos package.json e package-lock.json
COPY package*.json ./

# Instale as dependências
RUN npm install

# Copie o restante dos arquivos da aplicação
COPY . .

# Compile a aplicação para produção
RUN npm run build

# Etapa 2: Servir o conteúdo estático
FROM nginx:alpine

# Copie os arquivos compilados para a pasta do nginx
COPY --from=build /app/build /usr/share/nginx/html

# Exponha a porta 80 para o tráfego HTTP
EXPOSE 80

# Comando para rodar o Nginx
CMD ["nginx", "-g", "daemon off;"]
