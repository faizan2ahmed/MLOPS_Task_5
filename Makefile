install:
	pip install -r requirements.txt

flask:
	python Backend.py

compose:
	docker-compose build --no-cache

run: 
	docker-compose up


