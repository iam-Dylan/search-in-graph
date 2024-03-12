from maze import *
from const import *
import math

def DFS(g:SearchSpace, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.id]
    closed_set = []
    father = [-1]*g.get_length()
    
    father[g.start.id] = g.start.id

    while(len(open_set) != 0):
        node = g.grid_cells[open_set[-1]]
        open_set.remove(node.id)
        closed_set.append(node.id)
        node.set_color(YELLOW, sc)
        node.draw(sc)
        pygame.time.delay(100)
        pygame.display.flip()

        if(g.is_goal(node)):
            cur_node = g.goal
            g.start.set_color(ORANGE, sc)
            g.goal.set_color(PURPLE, sc)
            g.draw(sc)
            pygame.display.flip()
            while True:
                line_color = WHITE
                father_node = g.grid_cells[father[cur_node.id]]
                pygame.draw.line(sc, line_color, cur_node.rect.center, father_node.rect.center, 3)
                pygame.display.flip()
                cur_node = father_node
                if(cur_node == g.start):
                    break
                pygame.time.delay(100)
                pygame.display.flip()
            return

        node_neighbors = g.get_neighbors(node)
        for i in node_neighbors:
            if(father[i.id] == -1):
                father[i.id] = node.id
                open_set.append(i.id)
                i.set_color(RED, sc)
                i.draw(sc)
                pygame.time.delay(50)
                pygame.display.flip()
            if(g.is_goal(i)):
                    break
        
        node.set_color(BLUE, sc)
        node.draw(sc)
        pygame.display.flip()
    return

def BFS(g:SearchSpace, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.id]
    closed_set = []
    father = [-1]*g.get_length()
    
    father[g.start.id] = g.start.id

    while(len(open_set) != 0):
        node = g.grid_cells[open_set[0]]
        open_set.remove(node.id)
        closed_set.append(node.id)
        node.set_color(YELLOW, sc)
        node.draw(sc)
        pygame.time.delay(50)
        pygame.display.flip()

        if(g.is_goal(node)):
            cur_node = g.goal
            g.start.set_color(ORANGE, sc)
            g.goal.set_color(PURPLE, sc)
            g.draw(sc)
            pygame.display.flip()
            while True:
                line_color = WHITE
                father_node = g.grid_cells[father[cur_node.id]]
                pygame.draw.line(sc, line_color, cur_node.rect.center, father_node.rect.center, 3)
                pygame.display.flip()
                cur_node = father_node
                if(cur_node == g.start):
                    break
                pygame.time.delay(100)
                pygame.display.flip()
            return

        node_neighbors = g.get_neighbors(node)
        for i in node_neighbors:
            if(father[i.id] == -1):
                father[i.id] = node.id
                open_set.append(i.id)
                i.set_color(RED, sc)
                i.draw(sc)
                pygame.time.delay(50)
                pygame.display.flip()
            if(g.is_goal(i)):
                    open_set[0] = i.id
        node.set_color(BLUE, sc)
        node.draw(sc)
        pygame.display.flip()
    return


def Dijkstra(g:SearchSpace, sc:pygame.Surface):
    print('Implement Dijkstra algorithm')

    closed_set = []
    father = [-1]*g.get_length()
    cost = [100000]*g.get_length()
    cost[g.start.id] = 0
    open_set = []
    open_set.append(g.start.id)

    for i in g.grid_cells:
        min_cost = 100000
        best_node = -1
        for j in g.grid_cells:
            if(j.id not in closed_set and cost[j.id] < min_cost):
                min_cost = cost[j.id]
                best_node = j
                
        if(g.is_goal(best_node)):
            is_continue = False
            break
               
        closed_set.append(best_node.id)
        best_node.set_color(YELLOW, sc)
        best_node.draw(sc)
        pygame.time.delay(50)
        pygame.display.flip()
        node_neighbors = g.get_neighbors(best_node)
        for j in node_neighbors:
            w = math.sqrt(abs(best_node.x-j.x)**2+abs(best_node.y-j.y)**2) 
            if(cost[j.id] > cost[best_node.id] + w): 
                cost[j.id] = cost[best_node.id] + w
                father[j.id] = best_node.id
                j.set_color(RED, sc)
                j.draw(sc)
                pygame.time.delay(50)
                pygame.display.flip()
        best_node.set_color(BLUE, sc)
        best_node.draw(sc)
        pygame.display.flip()

    g.start.set_color(ORANGE, sc)
    g.goal.set_color(PURPLE, sc)
    g.start.draw(sc)
    g.goal.draw(sc)
    pygame.display.flip()
    cur_node = g.goal
    while True:
        line_color = WHITE
        father_node = g.grid_cells[father[cur_node.id]]
        pygame.draw.line(sc, line_color, cur_node.rect.center, father_node.rect.center, 3)
        pygame.display.flip()
        cur_node = father_node
        if(cur_node == g.start):
            break
        pygame.time.delay(100)
        pygame.display.flip()
    return      

def UCS(g:SearchSpace, sc:pygame.Surface):
    print('Implement UCS algorithm')

    closed_set = []
    father = [-1]*g.get_length()
    cost = [100000]*g.get_length()
    cost[g.start.id] = 0
    open_set = []
    open_set.append(g.start.id)

    is_continue = True

    for i in g.grid_cells:
        
        if(is_continue == False):
            break

        min_cost = 100000
        best_node = -1
        for j in g.grid_cells:
            if(j.id not in closed_set and cost[j.id] < min_cost):
                min_cost = cost[j.id]
                best_node = j
               
        closed_set.append(best_node.id)
        best_node.set_color(YELLOW, sc)
        best_node.draw(sc)
        pygame.time.delay(50)
        pygame.display.flip()

        if(g.is_goal(best_node)):
            is_continue = False
            break

        node_neighbors = g.get_neighbors(best_node)
        for j in node_neighbors:
            #w = math.sqrt(abs(best_node.x-j.x)**2+abs(best_node.y-j.y)**2)
            if(cost[j.id] > cost[best_node.id]):
                cost[j.id] = cost[best_node.id]
                father[j.id] = best_node.id
                j.set_color(RED, sc)
                j.draw(sc)
                pygame.time.delay(50)
                pygame.display.flip()
            if(g.is_goal(j)):
                is_continue = False
                break
        
        best_node.set_color(BLUE, sc)
        best_node.draw(sc)
        pygame.display.flip()

    g.start.set_color(ORANGE, sc)
    g.goal.set_color(PURPLE, sc)
    g.start.draw(sc)
    g.goal.draw(sc)
    pygame.display.flip()
    cur_node = g.goal
    while True:
        line_color = WHITE
        father_node = g.grid_cells[father[cur_node.id]]
        pygame.draw.line(sc, line_color, cur_node.rect.center, father_node.rect.center, 3)
        pygame.display.flip()
        cur_node = father_node
        if(cur_node == g.start):
            break
        pygame.time.delay(100)
        pygame.display.flip()
    return        


def AStar(g:SearchSpace, sc:pygame.Surface):
    print('Implement A* algorithm')

    closed_set = []
    father = [-1]*g.get_length()
    cost = [100000]*g.get_length()
    cost[g.start.id] = 0
    open_set = []
    open_set.append(g.start.id)

    g_score = [100000]*g.get_length()
    g_score[g.start.id] = 0
    f_score = [100000]*g.get_length()
    f_score[g.start.id] = g_score[g.start.id] + math.sqrt(abs(g.start.x-g.goal.x)**2+abs(g.start.y-g.goal.y)**2)
    
    while len(open_set) != 0:
        min_f_score = 100000
        best_node = -1
        for i in open_set:
            if(f_score[i] < min_f_score):
                min_f_score = f_score[i]
                best_node = i
        cur_node = g.grid_cells[best_node]
        open_set.remove(cur_node.id)
        closed_set.append(cur_node.id)
        cur_node.set_color(YELLOW, sc)
        cur_node.draw(sc)
        pygame.time.delay(50)
        pygame.display.flip()
        
        if(g.is_goal(cur_node)):
            cur_node = g.goal
            g.start.set_color(ORANGE, sc)
            g.goal.set_color(PURPLE, sc)
            g.draw(sc)
            pygame.display.flip()
            while True:
                line_color = WHITE
                father_node = g.grid_cells[father[cur_node.id]]
                pygame.draw.line(sc, line_color, cur_node.rect.center, father_node.rect.center, 3)
                pygame.display.flip()
                cur_node = father_node
                if(cur_node == g.start):
                    break
                pygame.time.delay(100)
                pygame.display.flip()
            return
        
        node_neighbors = g.get_neighbors(cur_node)
        for i in node_neighbors:
            if(i.id in closed_set):
                continue
            w = math.sqrt(abs(cur_node.x-i.x)**2+abs(cur_node.y-i.y)**2)
            tentative_g_score = g_score[cur_node.id] + w
            if(i.id not in open_set or tentative_g_score < g_score[i.id]):
                father[i.id] = cur_node.id
                g_score[i.id] = tentative_g_score
                f_score[i.id] = g_score[i.id] + math.sqrt(abs(i.x-g.goal.x)**2+abs(i.y-g.goal.y)**2)
                if(i.id not in open_set):
                    open_set.append(i.id)
                    i.set_color(RED, sc)
                    i.draw(sc)
                    pygame.time.delay(50)
                    pygame.display.flip()
            if(g.is_goal(i)):
                open_set[0] = i.id
                break
        cur_node.set_color(BLUE, sc)
        cur_node.draw(sc)
        pygame.display.flip()
    return

