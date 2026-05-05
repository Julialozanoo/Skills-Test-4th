from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
absences = np.array([0, 0, 0, 0, 0])

def add_attendance(event):
    day = document.getElementById("day").value
    value = document.getElementById("absences").value

    if value == "":
        return

    value = int(value)

    if day in days:
        index = list(days).index(day)
        absences[index] = value

    display(f"{day}: {value} absences", target="output")


def show_graph(event):
    plt.clf()

    plt.plot(days, absences, marker='o')

    plt.title("Weekly Absences")
    plt.xlabel("Days")
    plt.ylabel("Absences")
    plt.grid(True)

    display(plt.gcf(), target="output")
