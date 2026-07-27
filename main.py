import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fungsi perhitungan sederhana (contoh)
def compute_gravity():
    density = float(entry_density.get())
    depth = float(entry_depth.get())

    x = np.linspace(0, 1000, 200)

    # Anomali sintetik sederhana
    gravity = density * np.exp(-((x - 500)**2)/(2*(depth/2)**2))

    ax1.clear()
    ax1.plot(x, gravity, 'b', linewidth=2)
    ax1.set_xlabel("Distance (m)")
    ax1.set_ylabel("Gravity Anomaly (mGal)")
    ax1.set_title("Gravity Response")

    # Model bawah permukaan
    ax2.clear()
    polygon_x = [300, 700, 700, 300]
    polygon_z = [depth, depth, depth+200, depth+200]

    ax2.fill(polygon_x, polygon_z, color='gray')
    ax2.set_xlim(0, 1000)
    ax2.set_ylim(depth+300, 0)
    ax2.set_xlabel("Distance (m)")
    ax2.set_ylabel("Depth (m)")
    ax2.set_title("2D Model")

    canvas.draw()

# GUI utama
root = tk.Tk()
root.title("FORGRAV (Forward Modelling Gravity)")
root.geometry("1000x700")

frame_input = ttk.Frame(root)
frame_input.pack(side=tk.LEFT, padx=10, pady=10)

ttk.Label(frame_input, text="Density Contrast (g/cm³)").pack()
entry_density = ttk.Entry(frame_input)
entry_density.insert(0, "0.5")
entry_density.pack()

ttk.Label(frame_input, text="Depth (m)").pack()
entry_depth = ttk.Entry(frame_input)
entry_depth.insert(0, "200")
entry_depth.pack()

ttk.Button(frame_input, text="Compute", command=compute_gravity).pack(pady=20)

# Figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 7))

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()