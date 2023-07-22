# flask-telebot

## build image
docker build -t coda/flask-bot .

## create and run container
docker run --name flask-bot  -v D:\Projects\flask-bot\templates:/app/templates  --env=OPENAI_API_KEY=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 --workdir=/app -p 8003:80 --restart=unless-stopped -d coda/flask-bot:latest
