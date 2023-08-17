.PHONY: build
build:
	docker build --tag my-scratch-image .

# Have to authenticate to dockerhub and create repo first:
# https://docs.docker.com/engine/reference/commandline/login/
.PHONY: push-dockerhub
push-dockerhub:
	docker tag my-scratch-image anuragb98/test1_repo
	docker push anuragb98/test1_repo

	docker tag my-scratch-image anuragb98/test1_repo:abc-123
	docker push anuragb98/test1_repo:abc-123

.PHONY: push-github-packages
push-github-packages:
	docker push ghcr.io/anuragbambardekar/test:latest