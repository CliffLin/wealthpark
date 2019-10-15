test:
	ENV=TEST pytest -s

dev-server:
	./bin/api

prod-server:
	ENV=prod ./bin/api
