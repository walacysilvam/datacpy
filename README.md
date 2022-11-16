# DATA { C , PY }<br>
## Data miner in c and python<br> <br>
<p> { DATASCRIPT.C }:: Script escrito em C, faz a leitura do arquivo data.ESTABELE(numero 04) da receita e salva em um novo arquivo de saida.<br> Foi necessario pois o python se mostrou lento e incapaz de abrir o arquivo, retornando erros em ponteiros/memoria e por vezes em caracteres, se mostrou bastante volatil.<br> Ultilizando C foi possivel alocar ponteiros e libera-los, o que permitiu correr o arquivo sem problemas. Este script gera um novo arquivo com 50.000 linhas contendo dados de uma empresa em cada. Ele pode percorrer todo o arquivo original, mas para uso nesse programa, 50,000 linhas é suficiente para testar.</p>
<p> { MAIN.PY }:: Script em Python que lê e gerencia o banco de dados(Mongo Atlas). Esse script faz a leitura do arquivo gerado por datascript.c e sobe para o banco de dados com os devidos campos formatados. Também substitui os campos em branco pela palavra "VAZIO" antes de enviar ao Atlas. É possivel escolher o que deseja executar atraves de um Menu simples contendo 5 opções.<p>

### MELHORIAS
- Necessario implementar a função export() para gravar a busca feita no atlas em excel e csv.
- Necessario melhorar a função busca_ativos() para melhorar a qualidade da pesquisa bem como o calculo %.
- Necessario melhorar a função busca_res_ano() para buscar e retornar empresas pelo ano.
- Necessario implementar um Cmake ou Shell para rodar os dois scripts em sequencia, primeiro o C depois o Py.
