# My shell

Aluno: Ricardo Savii
RA: 92482

## About

Shell criada para disciplina de Sistemas Operativos Modernos

## How to use

Makefile has the compile command `make shell` and tests implemented.

Observations:

* `make test4` is not working properly due to bad tockenization.

* `make test5` is not working properly as `make` command already creates a background process and I think it's messing with m background implementation. Nonetheless this test works if run outside make by running inside the implemented shell like this:

    1. `make .shell`
    2. `sleep 40 && tail -f teste.txt > background_test &`

Although the warning created (`printf("Process created with PID: %d\n",PID);`) is not properly printed. :/

## About implementation

To implement this piece of code I used code provided by the teacher, book and basically Stackoverflow searching for "how to deal with pipes in a c shell", "how to background command in a c shell". So it's like a Frankenstein code with many edits from other codes. I reall hope it'll not be considered plagiarism, thanks nonetheless this task was very challenging and made me remember a lot about c programming.