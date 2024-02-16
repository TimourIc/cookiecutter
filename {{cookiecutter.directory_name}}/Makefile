venv: 
	python -m venv venv
requirements:
	pip install -r requirements.txt
clean:
	black src
	black scripts
	isort src
	isort scripts
clear_logs:	
	rm -f logs/* 
