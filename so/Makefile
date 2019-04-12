

.shell:
	gcc -o shell shell.c && \
	./shell

test1:
	ls -la
	ls -la > teste.txt

test2:
	ls -la | grep teste
	ls -la | grep teste | grep x 

test3: # not working
	ls la | grep teste | awk '{print $9}' > out
	sort < out > out_ord

test4:
	sort < teste.txt | grep x > novo_teste.txt

test5: # if tested with make the output happens, but the background warning does not appear
	sleep 40 && tail -f teste.txt > background_test &