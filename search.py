"""
In search.py, you will implement generic search algorithms
"""

import CPF.util as util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def lookup(s, problem):
    """
    for Dfs and Bfs
    :param s: the queue/stack
    :param problem: the problem
    :return: the solution
    """
    d = {}  # the father of each node
    visited = set()  # a set of the visited nodes
    start = problem.get_start_state()
    s.push(start)
    visited.add(start)
    d[start] = None

    while not s.isEmpty():
        u = s.pop()

        # creating the moves solution
        if problem.is_goal_state(u):
            curr_state = u
            moves_list = []
            while d[curr_state] is not None:
                moves_list.append(d[curr_state][1])
                curr_state = d[curr_state][0]
            return moves_list[::-1]

        # adding each child to the queue/stack
        for tup in problem.get_successors(u):
            if tup[0] in visited:
                continue
            a = tup[0]
            d[a] = (u, tup[1])
            s.push(a)
            visited.add(a)


def depth_first_search(problem):
    """
    DFS for the problem
    :param problem: the problem
    :return: the solution
    """
    s = util.Stack()  # in DFS we use stack
    return lookup(s, problem)


def breadth_first_search(problem):
    """
    BFS for the problem
    :param problem: the problem
    :return: the solution
    """
    s = util.Queue()  # in BFS we use queue
    return lookup(s, problem)


def uniform_f_cost_search(problem, f):
    """
    a general function for ucs and astar
    :param problem: the problem
    :param f: the cost function. returns the cost to the point,
    and the heuristic to the point (in ucs the heuristic is 0)
    :return: the solution
    """
    count = 0
    count_expanded = 0
    queue = util.PriorityQueue()
    nodes = {}  # a dict that connects between state number and the state. num: state, move, father_num
    queue.push((count, None, 0), 0)  # node_num, father_num, cost
    nodes[0] = (problem.get_start_state(), None, None)

    while not queue.isEmpty():
        count_expanded += 1
        node = queue.pop()\

        # checking if we reached a goal state:
        if problem.is_goal_state(nodes[node[0]][0]):
            last = node[0]
            moves_list = []

            # creating the steps for the solution:
            while nodes[last][2] is not None:
                state, move, new_last = nodes[last]
                last = new_last
                if move is None:
                    break
                moves_list.append(move)
            return moves_list[::-1]

        cost = node[2]
        father_count = node[0]

        # adding all the successors of the curr node:
        for successor in problem.get_successors(nodes[node[0]][0]):
            count += 1
            state = successor[0]
            move = successor[1]
            nodes[count] = (state, move, father_count)
            new_cost, h = f(move, state)
            new_cost = cost + new_cost
            # saving the father of the curr node and the cost to get to it
            queue.push((count, father_count, new_cost),
                       new_cost + h)
        # print(cost, count_expanded)


def uniform_cost_search(problem):
    """
    UCS algorithm for finding shortest path
    :param problem: the problem
    :return: the solution
    """
    def cost(move, state):
        """
        a cost function for ucs
        :param move: the move we have done which determines the price
        :param state: the state, we don't need it in ucs because we don;t use heuristics
        :return: the cost of the curr move
        """

        # we return ,0 because the heuristic is 0
        return problem.get_cost_of_actions([move]), 0

    return uniform_f_cost_search(problem, cost)


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    A star algorithm for finding shortest path
    :param problem: the problem
    :param heuristic: the heuristic
    :return: the solution
    """

    def astar_cost(move, state):
        """
        a cost function for a star
        :param move: the move we have done which determines the price
        :param state: the state, for the heuristic function
        :return: the cost and the heuristic
        """
        return problem.get_cost_of_actions([move]), heuristic(state, problem)

    return uniform_f_cost_search(problem, astar_cost)


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
