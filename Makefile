install:
	pip install -r requirements.txt

docker-up:
	docker compose up -d

docker-down:
	docker compose down

run:
	python telegram/bot.py