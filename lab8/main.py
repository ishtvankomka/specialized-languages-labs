import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

from client_application.client_application import ClientApplication


if __name__ == "__main__":

    """ for x in range(0, 5):
        plt.close()
        df = pd.read_csv('lab8/data.csv')
        print(df.to_string())

        df.plot(kind='bar', x='date', y='income')

        plt.show() """

    """ df = pd.read_csv('lab8/data.csv')
    print(df.to_string())
    df.plot(kind='bar', x='date', y='income')
    plt.show()

    df = pd.read_csv('lab8/data.csv')
    print(df.to_string())
    df.plot(kind='bar', x='date', y='income')
    plt.show() """

    app = ClientApplication()
    app.launch()
