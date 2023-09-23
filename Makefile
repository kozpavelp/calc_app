IMAGE_NAME = my_test_task
CONTAINER_NAME = my_test_task_container

PORT = 8000

up: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)


down: stop rm clean

stop:
	docker stop $(CONTAINER_NAME)

rm:
	docker rm $(CONTAINER_NAME)

clean:
	docker rmi $(IMAGE_NAME)
