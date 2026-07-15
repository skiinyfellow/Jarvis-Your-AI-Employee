.PHONY: help install up down logs clean test lint format

help:
	@echo "Jarvis AI Employee - Development Commands"
	@echo ""
	@echo "Usage:"
	@echo "  make install    - Install dependencies"
	@echo "  make up         - Start Docker containers"
	@echo "  make down       - Stop Docker containers"
	@echo "  make logs       - View container logs"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linters"
	@echo "  make format     - Format code"
	@echo "  make clean      - Clean up temporary files"

.PHONY: install
install:
	pip install -r requirements.txt

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f openjarvis

test:
	pytest tests/ -v

lint:
	black --check .
	pylint core/ modules/
	mypy core/ modules/

format:
	black .

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	rm -rf .mypy_cache
