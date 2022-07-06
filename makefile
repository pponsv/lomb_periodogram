MAIN = flomb

all: 
	$(MAKE) -C ./src/ all

clean:
	rm -f *.so
