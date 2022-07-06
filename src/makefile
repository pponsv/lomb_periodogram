MAIN = flomb

all: main.f90
	f2py3 -c --f90flags='-Wno-tabs -fopenmp -O2' -lgomp -m $(MAIN) $<
	cp ./$(MAIN).cpython* ../

clean:
	rm -f *.so
