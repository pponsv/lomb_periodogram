MAIN = lomb

all: 
	$(MAKE) -C ./src/ all
	(cd .. ; pdoc --math $(MAIN) -o ./$(MAIN)/doc/docs)

clean:
	rm -f *.so
