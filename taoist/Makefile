# taoist 项目打包
# python setup.py develop 

PYTHON := .venv/bin/python
ENVPYTHON := "/usr/bin/env python"
BUILD := build
TARGET := taoist.pyz
SRC := src/*
ENTRYPOINT := taoist.main:main
LIBS := .venv/lib/python3.12/*

build:
	[ ! -d $(BUILD) ] && mkdir $(BUILD)
	cp -r $(SRC) $(BUILD)
	cp -r $(LIBS) $(BUILD)
	$(PYTHON) -m zipapp $(BUILD) -p $(ENVPYTHON) -c -m $(ENTRYPOINT) -o $(TARGET)

.PHONY: all clean

clean:
	rm -fr $(BUILD) $(TARGET)
