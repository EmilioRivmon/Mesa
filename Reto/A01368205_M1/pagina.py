from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from A01570748_M1.money_model import MoneyModel
from mesa.visualization.modules import CanvasGrid

def agent_portrayal(agent):
  portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5}

  if agent.tipo == "carroH":
    portrayal["Color"] = "blue"
    portrayal["Layer"] = 1
    portrayal["r"] = 0.3
  elif agent.tipo == "carrroV":
    portrayal["Color"] = "green"
    portrayal["Layer"] = 1
    portrayal["r"] = 0.3
  return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(MoneyModel, 
                      [grid], 
                      "Modelo de Limpieza", 
                      {"N":6, "width":10, "height": 10, "percent": 1})
server.port = 8521
server.launch()