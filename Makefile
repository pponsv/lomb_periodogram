# MAIN = lomb

# all: 
# 	$(MAKE) -C ./src/ all
# 	(cd .. ; pdoc --math $(MAIN) -o ./$(MAIN)/doc/docs)

# clean:
# 	rm -f *.so

MAIN = flomb
DIR  = $(shell basename $(CURDIR))

.PHONY : all clean install meson_configure

all: install

bld:
	meson bld

meson_configure: bld
	meson setup --wipe bld

install: meson_configure
	meson install -C bld

clean:
	rm -rf ./*.so ./src/*.so ./bld ./bin/*.so
