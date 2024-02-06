CC=gcc
CFLAGS=-O3 -std=c99 -w
TARGET=akms
all: $(TARGET)

$(TARGET): akms.c
	$(CC) akms.c $(CFLAGS) -o $(TARGET)

clean:
	$(RM) $(TARGET)
