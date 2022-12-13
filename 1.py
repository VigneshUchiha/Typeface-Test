class Graph:

    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
        self.isolated = set()
        self.start = 0
        self.curr = [0, 0, 0, 0]
        self.lap = [0, 0, 0, 0]
        self.mg = [0, 0, 0, 0]

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])

    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices

    def dfs(self, i, j, visited):

        # These arrays are used to get row and col
        # of a given cell
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        # Mark this cell as visited
        visited[i][j] = True

        # Recur for all connected neighbours
        for xi, yi in directions:
            if self.isSafe(i + xi, j + yi, visited):
                self.dfs(i + xi, j + yi, visited)

    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix

    def iso(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]

        # Initialize count as 0 and traverse
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    if not self.start:
                        self.curr = [i, j, 0, 0]
                        self.mg = [i, j, 0, 0]
                        self.start = 1
                    else:

                        self.curr = [(self.curr[0] + i) // 2,
                                     (self.curr[1] + j) // 2, abs(self.curr[0] - i), abs(self.curr[1] - j)]
                        self.lap = [i, j, 0, 0]

                    self.dfs(i, j, visited)
                    count += 1
                else:
                    self.isolated.add((self.curr[0], self.curr[1], abs(
                        self.mg[0] - self.lap[0]), abs(self.mg[1] - self.lap[1])))
                    self.curr = [0, 0, 0, 0]
                    self.lap = [0, 0, 0, 0]
                    self.mg = [0, 0, 0, 0]
                    self.start = 0

        return self.isolated


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1]]


row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)


print(g.iso())
