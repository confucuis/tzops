PEX := pex
TARGET := taoist
ENTRYPOINT := taoist.main:main


build:
	$(PEX) -r requirements.txt -e $(ENTRYPOINT) -D src -o $(TARGET)

.PHONY: all clean

clean:
	rm -fr $(TARGET)
