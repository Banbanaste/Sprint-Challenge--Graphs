class Graph:
    def __init__(self, v):
        self.verticies = {i for i in v}

    def add_edges(self, v, **kwargs):
        print("in add_edge: ", v, kwargs)
