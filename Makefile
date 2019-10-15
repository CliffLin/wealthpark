LINT_FILES := $(shell find wealthpark -type f -name '*.py'  -prune | sort)


test:
	ENV=TEST pytest -s

lint:
	pylint --rcfile=$(CURDIR)/pylintrc \
		--msg-template='{path}:{line}: {msg_id}: {msg}' \
		--generated-members join \
		--load-plugins pylint_quotes,pylint_flask,pylint_flask_sqlalchemy $(LINT_FILES)


dev-server:
	./bin/api

prod-server:
	ENV=prod ./bin/api
