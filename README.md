# flask-bot

## build image
docker build -t coda/flask-bot .

## create and run container
docker run --name flask-bot -v D:\Projects\flask-bot\templates:/app/templates -v D:\Projects\flask-bot\static:/app/static --env=OPENAI_API_KEY={OPENAI_API_KEY} --workdir=/app -p 8003:80 --restart=unless-stopped -d coda/flask-bot:latest
