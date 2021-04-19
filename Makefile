all: win-script-quizzer clean

win-script-quizzer: .FORCE
	./bin/win-pyinstaller/bin/pyinstaller.exe src/main.py -n win-script-quizzer -F
	chmod u+x dist/win-script-quizzer
	mv dist/win-script-quizzer ./win-script-quizzer

clean:
	rm -f win-script-quizzer.spec
	rm -r -f build
	rm -r -f dist

.FORCE: