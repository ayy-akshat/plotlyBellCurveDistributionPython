import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")

graph = ff.create_distplot([df["Avg Rating"].tolist()], ["Company Rating Distribution"])
graph.show()
