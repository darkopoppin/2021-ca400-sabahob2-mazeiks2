FROM node

# install simple http server for serving static content
RUN npm install -g @ionic/cli@latest

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json /app/

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . /app/

EXPOSE 8100
CMD [ "ionic", "serve", "--external"]