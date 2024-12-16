from interpolate_and_matplotlib import *
from plt_graph import *


if __name__ == "__main__":
    depth = 45  # Глубина для построения тепловой карты
    data = InterpolateData(depth, "thermometric_measurements.csv")
    interp_data = InterpolateData.interpolate(data)
    graph = HeatMap(*interp_data)
    HeatMap.chart(graph)