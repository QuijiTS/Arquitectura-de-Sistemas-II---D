# Etapa 1: Construcción (Build) de la aplicación Vite
FROM node:20-alpine as build
WORKDIR /app
# Copiar solo los archivos de dependencias primero (aprovecha la caché de Docker)
COPY package*.json ./
RUN npm install
# Copiar el resto del código y compilar
COPY . .
RUN npm run build

# Etapa 2: Servidor Web (Nginx) para servir la página
FROM nginx:alpine
# Copiar los archivos compilados de la etapa 1 a la carpeta que lee Nginx
COPY --from=build /app/dist /usr/share/nginx/html
# Exponer el puerto 80 (el estándar para web)
EXPOSE 80
# Iniciar Nginx
CMD ["nginx", "-g", "daemon off;"]