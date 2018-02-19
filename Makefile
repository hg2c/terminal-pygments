test:
	sudo python3 setup.py develop
	pygmentize -O full -f html -o test.html test.terminal
