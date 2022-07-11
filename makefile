MAIN = lomb

all: 
	$(MAKE) -C ./src/ all
	(cd .. ; pdoc $(MAIN) -o ./$(MAIN)/doc/docs)

clean:
	rm -f *.so
