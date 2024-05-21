PEX := pex
TARGET := zombie
ENTRYPOINT := zombie.main:main


build:
	$(PEX) -r requirements.txt --timeout 360 -e $(ENTRYPOINT) -D src -o $(TARGET)
check:
	@[ -f $(PEX) ] && echo $(PEX) exist. || echo $(PEX) not exist.

.PHONY: all clean

clean:
	rm -fr $(TARGET)
