from visualizer import Visualizer

v = Visualizer("cos(x)", "sin(y)")
plt = v.plot_color(skip=1)
plt.savefig("./img/vector_field.png")