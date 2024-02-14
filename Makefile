# MAIN = lomb

# all: 
# 	$(MAKE) -C ./src/ all
# 	(cd .. ; pdoc --math $(MAIN) -o ./$(MAIN)/doc/docs)

# clean:
# 	rm -f *.so

MAIN = flomb
DIR  = $(shell basename $(CURDIR))

.PHONY : all clean doc compile

all: compile doc

compile: ./src/lomb_fortran.f90
	cd src/ && python3 -m numpy.f2py -c --f90flags='-Wno-tabs -fopenmp -O2' --build-dir bld/ -lgomp -m $(MAIN) ../$<
	
clean:
	rm -f ./*.so ./src/*.so

doc:
	(cd .. ; pdoc --math $(CURDIR) -o ./$(DIR)/doc/docs)
	echo $(DIR)
