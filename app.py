pip install -r requirements.txt ## Installing dependencies

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a function for the animation
def animate_graph():
    fig, ax = plt.subplots()
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    line, = ax.plot(x, y, color='b')

    ax.set_xlim(0, 2 * np.pi)  # x-axis limits
    ax.set_ylim(-1.1, 1.1)  # y-axis limits

    # Animation function
    def update(frame):
        line.set_ydata(np.sin(x + frame / 10))  # Update y data
        return line,

    # Create animation
    ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    return ani

# Streamlit toggle for activation
on = st.toggle("Activate feature")

# Placeholder for the plot
placeholder = st.empty()

if on:
    st.write("Feature activated! Starting the animation...")
    
    # Start the animation
    ani = animate_graph()
    
    # Use Streamlit's placeholder to update the plot
    for _ in range(100):
        placeholder.pyplot(ani._fig)
    
    # Display the plot
else:
    st.write("Feature deactivated. Animation stopped.")
