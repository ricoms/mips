
// Aluno: Ricardo Manhães Savii
// RA: 92482

#include <fcntl.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>

#include <unistd.h>

#define LINE_BUFFER_SIZE 1024
#define TOK_BUFFER_SIZE 64

pid_t PID;

int change_directory(char* args[]){
    if (args[1] == NULL) {
        printf(" Needs path\n");
        return -1;
    }
    else{ 
        if (chdir(args[1]) == -1) {
            printf(" %s: no such directory\n", args[1]);
            return -1;
        }
    }
    return 0; 
}

void launch_command(char **args, int background){	 
    int err = -1;

    if((PID=fork())==-1){
        printf("Child process could not be created\n");
        return;
    }
    if(PID==0){
        // child: ignore SIGINT signals 
        signal(SIGINT, SIG_IGN);

        // end process if non-existing commands
        if (execvp(args[0],args)==err){
            printf("Command not found");
            kill(getpid(),SIGTERM);
        }
    }

    // parent
    if (background == 0){
        // wait
        waitpid(PID,NULL,0);
    }else{
        // SIGCHILD handler will take care of the childs returning values
        printf("Process created with PID: %d\n",PID);
    }	 
}


void file_IO(char * args[], char* input_file, char* output_file, int mode){

    int err = -1;

    int fileDescriptor;

    if((PID=fork())==-1){
        printf("Child process error\n");
        return;
    }
    if(PID==0){
        // output redirection
        if (mode == 0){
            fileDescriptor = open(output_file, O_CREAT | O_TRUNC | O_WRONLY, 0600); 
            dup2(fileDescriptor, STDOUT_FILENO); 
            close(fileDescriptor);
        // input and output redirection
        } else if (mode == 1) {
            fileDescriptor = open(input_file, O_RDONLY, 0600);  
            dup2(fileDescriptor, STDIN_FILENO);
            close(fileDescriptor);

            fileDescriptor = open(output_file, O_CREAT | O_TRUNC | O_WRONLY, 0600);
            dup2(fileDescriptor, STDOUT_FILENO);
            close(fileDescriptor);		 
        }

        if (execvp(args[0], args)==err) {
            printf("err");
            kill(getpid(), SIGTERM);
        }		 
    }
    waitpid(PID,NULL,0);
}

void pipe_handler(char * args[]){
    int filedes[2]; 
    int filedes2[2];
    int num_cmds = 0;
    char *command[256];

    pid_t pid;
    int err = -1;
    int end = 0;
    int i = 0, j = 0, k = 0, l = 0;

    while (args[l] != NULL){
        if (strcmp(args[l],"|") == 0){
            num_cmds++;
        }
        l++;
    }
    num_cmds++;

    while (args[j] != NULL && end != 1){
        k = 0;
        while (strcmp(args[j],"|") != 0){
            command[k] = args[j];
            j++;	
            if (args[j] == NULL){
                end = 1;
                k++;
                break;
            }
            k++;
        }
        command[k] = NULL;
        j++;		

        // connect the inputs and outputs 
        if (i % 2 != 0){
            pipe(filedes);
        }else{
            pipe(filedes2);
        }

        pid=fork();

        if(pid==-1){			
            if (i != num_cmds - 1){
                if (i % 2 != 0){
                    close(filedes[1]);
                }else{
                    close(filedes2[1]);
                } 
            }			
            printf("Child process error\n");
            return;
        }
        if(pid==0){
            if (i == 0){
                dup2(filedes2[1], STDOUT_FILENO);
            }
            // last on outputs in terminal
            else if (i == num_cmds - 1){
                if (num_cmds % 2 != 0){ 
                    dup2(filedes[0], STDIN_FILENO);
                } else {
                    dup2(filedes2[0], STDIN_FILENO);
                }
            } else {
                if (i % 2 != 0){
                    dup2(filedes2[0], STDIN_FILENO); 
                    dup2(filedes[1], STDOUT_FILENO);
                } else {
                    dup2(filedes[0], STDIN_FILENO); 
                    dup2(filedes2[1], STDOUT_FILENO);					
                } 
            }

            if (execvp(command[0],command)==err){
                kill(getpid(), SIGTERM);
            }		
        }

        // close descriptors on parent
        if (i == 0){
            close(filedes2[1]);
        }
        else if (i == num_cmds - 1){
            if (num_cmds % 2 != 0){					
                close(filedes[0]);
            }else{					
                close(filedes2[0]);
            }
        }else{
            if (i % 2 != 0){					
                close(filedes2[0]);
                close(filedes[1]);
            }else{					
                close(filedes[0]);
                close(filedes2[1]);
            }
        }
        waitpid(pid,NULL,0);
        i++;	
    }
}

int command_handler(char * args[]){
    int i = 0;
    int aux;
    int background = 0;

    char *args_aux[256];
    // look for the special characters and split the command
    while ( args[i] != NULL){
        if ( (strcmp(args[i],">") == 0) || (strcmp(args[i],"<") == 0)){
            break;
        }
        // background execution
        if ( (strcmp(args[i],"&") == 0)) {
            background = 1;
            break;
        }
        args_aux[i] = args[i];
        i++;
    }
    i = 0;
    if(strcmp(args[0], "exit") == 0) exit(0);
    else if (strcmp(args[0], "cd") == 0) change_directory(args);
    else {
        while (args[i] != NULL && background == 0){
            if (strcmp(args[i],"|") == 0){
                pipe_handler(args);
                return 1;
            // I/O redirection
            } else if (strcmp(args[i],"<") == 0){
                aux = i+1;
                if (args[aux] == NULL || args[aux+1] == NULL || args[aux+2] == NULL ){
                    printf("Not enough arguments\n");
                    return -1;
                } else {
                    if (strcmp(args[aux+1],">") != 0){
                        printf("Usage: Expected '>' and found %s\n",args[aux+1]);
                        return -2;
                    }
                }
                file_IO(args_aux, args[i+1], args[i+3], 1);
                return 1;
            } else if (strcmp(args[i],">") == 0){
                if (args[i+1] == NULL){
                    printf("Not enough arguments\n");
                    return -1;
                }
                file_IO(args_aux, NULL, args[i+1], 0);
                return 1;
            }
            i++;
        }
        args_aux[i] = NULL;
        launch_command(args_aux, background);
    }
    return 1;
}

// void test_tokenizer(char *tokens[], int numTokens) {
//     int i;
//     for (i=0; i<numTokens; i++){
//         printf("%s - ", tokens[i]);
//     }
//     printf("\n");
// }


int main(int argc, char *argv[]){
    char line[LINE_BUFFER_SIZE];
    char *tokens[TOK_BUFFER_SIZE];
    int i = 0;
    int j = 0;

    while (1) {
        printf("$ ");
        memset (line, '\0', LINE_BUFFER_SIZE);
        fgets(line, LINE_BUFFER_SIZE, stdin);
        if((tokens[0] = strtok(line," \n\t")) == NULL) continue;
        i=1;
        while((tokens[i] = strtok(NULL, " \n\t")) != NULL) i++;
        // test_tokenizer(tokens, i);
        command_handler(tokens);
    }
        
    return EXIT_SUCCESS;
}
