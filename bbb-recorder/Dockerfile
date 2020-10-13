# Wrap bbb-export into a docker image for use re-rencoding pyconza videos

FROM node:latest

# We don't worry too much about image size issues here
RUN apt update && apt dist-upgrade -y

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add

RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

RUN apt update && apt install -y google-chrome-stable git ffmpeg xvfb vim

# Via https://packages.debian.org/buster/fonts-noto-color-emoji. A buster package, but useable on sid
COPY fonts-noto-color-emoji.deb /

RUN dpkg -i fonts-noto-color-emoji.deb

RUN su -c 'cd /home/node && git clone https://github.com/jibon57/bbb-recorder' node

RUN cp /home/node/bbb-recorder/.env.example /home/node/bbb-recorder/.env

RUN chown node:node /home/node/bbb-recorder/.env

RUN su -c 'sed -ie "s#copyToPath=.*#copyToPath=/data/#" /home/node/bbb-recorder/.env' node

RUN su -c 'cd /home/node/bbb-recorder && npm install' node

WORKDIR /home/node/bbb-recorder/

ENTRYPOINT ["runuser", "-u", "node", "--", "node", "export.js"]

