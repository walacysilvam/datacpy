/*
 *  OBS::
 *	!! < NECESSARIO GNU LIB C >
 * 		INFELIZMENTE FOI NECESSARIO USAR A GLIBC,
 * 		O QUE COMPROMETE O SCRIPT PARA USO EM OUTRAS PLATAFORMAS
 *	
 *  OBS2::
 *		ESTA ACONTECENDO UMA PERCA GRADUAL DE DADOS AO PERCORRER
 *		O ARQUIVO ORIGINAL E FORMAR O ARQUIVOU DE SAIDA. NAO SEI
 *		AO CERTO O PORQUÊ...
 *
 *  DESC::
 * 		GLIBC POSSUI UM BUFFER DINAMICO, O QUE E
 * 		OTIMO PARA LER O ARQUIVO, QUE E GRANDE 
 * 		DEMAIS E TRAVA OS BUFFERS TESTADOS ANTERIORMENTE,
 * 		GERANDO ERROS (PYTHON)
 * 
*/

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

int main(int argc, char **argv) {
	//abre o arquivo original para leitura
	FILE *f = fopen("data.ESTABELE", "r");
	size_t len = 100;
	int p = 50000;
	char *linha = malloc(len);
	
	if (!f) {
		perror("data.ESTABELE");
		exit(1);
	}
	//criacao do arquivo de saida
	//e insercao de 50000 empresas nele.
	FILE *out;
	out = fopen("./dataOut/data_001.csv", "wt");
	if (out == NULL) {
		printf("Problemas na CRIAÇÃO do arquivo.\n");
	}

	for (int i= 0; getline(&linha, &len, f) > 0; i++) {
		if ( i <= p ) {
			char *j = strtok(linha, "'");
			int result = fputs(j, out);
			if (result == EOF) {
				printf("Erro na gravação");
			}

		} else {
			break;
		}
	}

	fclose(out);
	fclose(f);
	printf("[!] Arquivo de entrada finalizado com sucesso!\n");
	printf("[!] Arquivo de saída finalizado com sucesso!\n");
	printf("[!] Arquivo gravado em: dataOut/\n");
	if (linha) {
		free(linha);
	}
	
	return 0;
}
