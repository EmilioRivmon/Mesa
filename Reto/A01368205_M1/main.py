from A01570748_M1.money_model import MoneyModel
import matplotlib.pyplot as plt
import time


def basic_example_space():

    start_time = time.time()
    model = MoneyModel(6, 10, 10, 1)
    count = 0
    while count <= 100:
        time.sleep(0.25)
        model.step()
        model.printarray()
        count = count+1
        

    print("--- %s segundos ---" % (time.time() - start_time))
    
    
