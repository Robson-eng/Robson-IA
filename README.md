# Robson-IA

Aluno: Robson Marciel

Objetivo do projeto é implementar tipos de buscas para o PAC-MAN encontra comida em diferentes labirintos que são gerados a partir de comandos. 

Comando para busca DFS

python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent

Comando BFS

python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

Comando UCS

python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

Comando A* search

python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
python pacman.py -l trickySearch -p AStarFoodSearchAgent

Videos

Video DFS: https://drive.google.com/open?id=1f6SHm-nub_ybD0W5Bq4YAHG0Z2n4r-9B

Video BFS: https://drive.google.com/open?id=1ybrzXHbcf65y7tr9f4m64rJie-_Es_fI

Video UCS: https://drive.google.com/open?id=1zovYanYh_qL5EL4k_7baOk6Z0WVSlhfZ

Video A* search: https://drive.google.com/open?id=1IBs80rVB_Dx-GrQyArshxeMzHHfNnVcC


PERGUNTAS 

(Pergunta 1) A ordem de exploração foi de acordo com o esperado? O Pacman realmente passa por todos os estados explorados no seu caminho para o objetivo?

(Pergunta 2) Essa é uma solução ótima? Senão, o que a busca em profundidade está fazendo de errado?

(Pergunta 3) A busca BFS encontra a solução ótima? Senão, verifique a sua implementação. Se o seu código foi escrito de maneira correta, ele deve funcionar também para o quebra-cabeças de 8 peças (seção 3.2 do livro-texto) sem modificações.


(Pergunta 4) O que acontece em openMaze para as várias estratégias de busca?
