# Quake game parser log

<p align="center">
Construa um parser para o arquivo de log games.log.

O arquivo games.log é gerado pelo servidor de quake 3 arena. Ele registra todas as informações dos jogos, quando um jogo começa, quando termina, quem matou quem, quem morreu pq caiu no vazio, quem morreu machucado, entre outros.

O parser deve ser capaz de ler o arquivo, agrupar os dados de cada jogo, e em cada jogo deve coletar as informações de morte.

### Requirements

1. Python3

### How to run the development mode

<step-by-step>

**Example run Backend:**

1. Clone o repositorio `git clone git@github.com:felipefln/enextChallenge.git`
2. Acesse a pasta clonada `cd enextChallenge`
3. Crie uma virtualEnv para instalar o python3, ou se preferir, instale Python3 em sua maquina e execute o run.py com os comandos abaixos:

4. Comando para executar em modo detalhado `python3 run.py -f games.log -v`
5. Comando para executar em modo relatório no final do console `python3 run.py -f games.log -r`
6. Comando para executar em modo relatório com armas no final do console `python3 run.py -f games.log -r -p`

## More info

By Felipe Weiduschadt de Carvalho
