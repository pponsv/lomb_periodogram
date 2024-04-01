# MAIN = lomb

# all: 
# 	$(MAKE) -C ./src/ all
# 	(cd .. ; pdoc --math $(MAIN) -o ./$(MAIN)/doc/docs)

# clean:
# 	rm -f *.so

MAIN = flomb
DIR  = $(shell basename $(CURDIR))

.PHONY : all clean doc compile

all: meson_configure meson_build

meson_init:
	meson bld

meson_configure:
	meson setup --wipe bld

meson_build:
	meson compile -C bld
	cp bld/$(MAIN).*.so ./src/

compile: ./src/lomb_fortran.f90
	python3 -m numpy.f2py -c --f90flags='-Wno-tabs -fopenmp -O2' --build-dir bld/ -lgomp -m $(MAIN) $<
	
clean:
	rm -rf ./*.so ./src/*.so ./bld

doc:
	(cd .. ; pdoc --math $(CURDIR) -o ./$(DIR)/doc/docs)
	echo $(DIR)
