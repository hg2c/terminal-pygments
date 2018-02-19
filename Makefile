test:
	sudo python3 setup.py develop
	pygmentize -O full -f html -o test/test.html test/test.terminal

.PHONY: test
