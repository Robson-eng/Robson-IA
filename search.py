# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  """
  "*** YOUR CODE HERE ***"

  Fronteira = util.Stack()
  Visitado = []
  Fronteira.push((problem.getStartState(), []))
  Visitado.append(problem.getStartState())

  while Fronteira.isEmpty() == 0:
      state, actions = Fronteira.pop()

      for next in problem.getSuccessors(state):
          num_estado = next[0]
          num_direc = next[1]
          if num_estado not in Visitado:
              if problem.isGoalState(num_estado):

                  return actions + [num_direc]
              else:
                  Fronteira.push((num_estado, actions + [num_direc]))
                  Visitado.append(num_estado)

  util.raiseNotDefined()


def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  Fronteira = util.Queue()
  Visitado = []
  Fronteira.push((problem.getStartState(), []))
  # print 'Start',problem.getStartState()
  # Visitado.append( problem.getStartState() )

  while Fronteira.isEmpty() == 0:
      state, actions = Fronteira.pop()

      for next in problem.getSuccessors(state):
          num_estado = next[0]
          num_direc = next[1]
          if num_estado not in Visitado:
              if problem.isGoalState(num_estado):
                  # print 'Find Goal'
                  return actions + [num_direc]
              Fronteira.push((num_estado, actions + [num_direc]))
              Visitado.append(num_estado)

  util.raiseNotDefined()

      
def uniformCostSearch(problem):
  "Search the node of least total custo first. "
  "*** YOUR CODE HERE ***"

  Visitado = {}
  solucao = []
  Fila = util.PriorityQueue()
  parents = {}
  custo = {}


  iniciar = problem.getStartState()
  Fila.push((iniciar, 'Undefined', 0), 0)
  Visitado[iniciar] = 'Undefined'
  custo[iniciar] = 0


  if problem.isGoalState(iniciar):
      return solucao
  objetivo = False;
  while (Fila.isEmpty() != True and objetivo != True):

      no = Fila.pop()

      Visitado[no[0]] = no[1]
      if problem.isGoalState(no[0]):
          noSoluc = no[0]
          objetivo = True
          break

      for elem in problem.getSuccessors(no[0]):

          if elem[0] not in Visitado.keys():
              prioridade = no[2] + elem[2]

              if elem[0] in custo.keys():
                  if custo[elem[0]] <= prioridade:
                      continue

              Fila.push((elem[0], elem[1], prioridade), prioridade)
              custo[elem[0]] = prioridade
              parents[elem[0]] = no[0]

  while (noSoluc in parents.keys()):
      noSolucPre = parents[noSoluc]
      solucao.insert(0, Visitado[noSoluc])
      noSoluc = noSolucPre
  return solucao

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the custo from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):




  Visitado = {}
  solucao = []
  Fila = util.PriorityQueue()
  parents = {}
  custo = {}
  iniciar = problem.getStartState()
  Fila.push((iniciar, 'Undefined', 0), 0)
  Visitado[iniciar] = 'Undefined'
  custo[iniciar] = 0

  if problem.isGoalState(iniciar):
      return solucao


  objetivo = False;
  while (Fila.isEmpty() != True and objetivo != True):

      no = Fila.pop()
      Visitado[no[0]] = no[1]

      if problem.isGoalState(no[0]):
          noSoluc = no[0]
          objetivo = True
          break

      for elem in problem.getSuccessors(no[0]):

          if elem[0] not in Visitado.keys():
              prioridade = no[2] + elem[2] + heuristic(elem[0], problem)

              if elem[0] in custo.keys():
                  if custo[elem[0]] <= prioridade:
                      continue

              Fila.push((elem[0], elem[1], no[2] + elem[2]), prioridade)
              custo[elem[0]] = prioridade
              parents[elem[0]] = no[0]


  while (noSoluc in parents.keys()):

      noSolucPre = parents[noSoluc]
      solucao.insert(0, Visitado[noSoluc])
      noSoluc = noSolucPre

  return solucao
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch