FROM node:lts-trixie
WORKDIR /app
COPY . .
RUN npm install
ENTRYPOINT ["npm", "run", "dev","--", "--host"]