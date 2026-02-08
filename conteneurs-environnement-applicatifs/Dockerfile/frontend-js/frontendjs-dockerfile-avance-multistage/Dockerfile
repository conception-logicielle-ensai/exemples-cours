# ----------------------------
# Image avancée avec multistage d'abord node
# ----------------------------
# Etape 1 build
FROM node:lts-trixie AS build
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
# Etape 2 on met le livrable qu'on a construit dans un serveur statique qui porte les pages construites
FROM nginx:alpine AS serveur_final
# C'est cette ligne qui est cruciale, on met ici le fichier construit via node, dans un serveur de page html (nginx)
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80 
# on accéde au serveur sur le port 80
CMD ["nginx", "-g", "daemon off;"]