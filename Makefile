all:
	make clean
clean:
	find . -iname  *#* -exec rm -f {} \;
	find . -iname  *~ -exec rm -f {} \;
