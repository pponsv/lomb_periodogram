# MAIN = lomb

# all: 
# 	$(MAKE) -C ./src/ all
# 	(cd .. ; pdoc --math $(MAIN) -o ./$(MAIN)/doc/docs)

# clean:
# 	rm -f *.so

MAIN = flomb
DIR  = $(shell basename $(CURDIR))

.PHONY : all clean doc

all: ./src/main.f90
	f2py3 -c --f90flags='-Wno-tabs -fopenmp -O2' -lgomp -m $(MAIN) $<
	@$(MAKE) doc

clean:
	rm -f *.so

doc:
	(cd .. ; pdoc --math $(CURDIR) -o ./$(DIR)/doc/docs)
	echo $(DIR)