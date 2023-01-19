# # automation_guilherme


# # Desafio Técnico - RPA

Seja bem vindo(a) ao processo seletivo do Data Opportunity

# Instruções

## Introdução
Esta etapa do desafio consiste em automatizar uma parte de um processo que coleta dados de produção de açúcar no México, efetua a leitura dos dados de um pdf e salvar de forma organizada em um documento excel

O processo deve ser organizado em dois arquivos:

-Biblioteca de leitura Pdf

-Script de Automação

### Biblioteca de leitura Pdf
Criar uma simples biblioteca com funções de leitura de pdf, para ser importada e utilizada no script de automação

Essa biblioteca pode utilizar-se de bibliotecas third-party já consagradas de leitura de arquivos em pdf

Deve seguir, preferencialmente, a metodologia de Programação Orientada a Objetos

### Script de Automação
Esse script deve conter as etapas de acesso ao site que contêm as informações, download e leitura de arquivos pdf, encontrar a tabela desejada, transportar os dados para um dataframe, efetuar pequenas alterações e salvar localmente

O processo é detalhado logo abaixo

### Detalhamento do Processo

-Acessar ao site https://www.gob.mx/conadesuca/documentos/dieproc-reportes-de-avance-de-produccion-ciclo-azucarero-2020-2021?state=published



-Fazer o download e leitura dos arquivos referentes aos reportes (apenas os 5 últimos são suficientes: report 40, 39, 38, 37, 36)

-Efetuar a leitura da tabela com o nome "Cuadro 7", seu algoritmo deve identificar automaticamente a tabela correta, pois podem estar em páginas diferentes dependendo do report

-Transcrever os dados dessas tabelas para um dataframe

-Montar um DataFrame que contenha as colunas: Ingenio, Data do Report, Superficie Industrializada, Cana Molida, Azucar Blanco Especial

-A Data do Report deve ser extraída da própria tabela, no caso abaixo a data seria: "31 de julio de 2021"

![image](https://user-images.githubusercontent.com/67006061/135717642-f003e418-0334-4aff-9794-5b9c02b66f30.png)


-Salvar os dados dos reports localmente em um único arquivo excel

### Dúvidas

Caso tenha qualquer tipo de dúvida, não hesite em contatar o seu ponto focal na Data Opportunity

Boa Sorte!!
