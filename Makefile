build:
	docker build -t version-store-backend .

run:
	docker run --rm -p 8000:8000 -t version-store-backend