install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_main.py

format:
	black *.py

run:
	python main.py

run-uvicorn:
	uvicorn main:app --reload

killweb:
	sudo killall uvicorn

lint:
	pylint --disable=R,C main.py

push:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 589637869505.dkr.ecr.us-east-1.amazonaws.com
	docker build -t ids706-week4 .
	docker tag ids706-week4:latest 589637869505.dkr.ecr.us-east-1.amazonaws.com/ids706-week4:latest
	docker push 589637869505.dkr.ecr.us-east-1.amazonaws.com/ids706-week4:latest

all: install lint