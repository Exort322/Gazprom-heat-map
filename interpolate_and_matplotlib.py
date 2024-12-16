import numpy as np
from scipy.interpolate import griddata
import pandas as pd


class InterpolateData:
    def __init__(self, depth, csv_file):
        self.depth = depth
        self.csv_file = csv_file

    def interpolate(self):
        """
        Интерполирует температуры между скважинами и строит тепловую карту на заданной глубине.

        :param well_positions: Список координат скважин в формате [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        :param temperatures: Список температур в скважинах на разных глубинах в формате [[t1_0, t1_5, ..., t1_50], [t2_0, t2_5, ..., t2_50], ...]
        :param depth: Глубина для построения тепловой карты (в метрах)
        """

        df = pd.read_csv(self.csv_file)
        tc1 = df['TC-1'].tolist()
        tc2 = df['TC-2'].tolist()
        tc3 = df['TC-3'].tolist()
        tc4 = df['TC-4'].tolist()

        well_positions = np.array([[0, 0], [100, 0], [100, 100], [0, 100]])  # Координаты скважин

        temperatures = [
            tc2,  # Температуры в скважине 1
            tc4,  # Температуры в скважине 2
            tc3,  # Температуры в скважине 3
            tc1  # Температуры в скважине 4
        ]

        # Определяем глубины, на которых измерялись температуры
        depths = np.array(df['Глубина'].tolist())

        # Находим индекс глубины, ближайшей к заданной
        depth_index = np.argmin(np.abs(depths - self.depth))

        # Создаем сетку для интерполяции
        grid_x, grid_y = np.mgrid[min(well_positions[:, 0]):max(well_positions[:, 0]):100j,
                         min(well_positions[:, 1]):max(well_positions[:, 1]):100j]

        # Выбираем температуры на заданной глубине
        well_temperatures = [temp[depth_index] for temp in temperatures]

        # Интерполируем температуры на сетку
        grid_z = griddata(well_positions, well_temperatures, (grid_x, grid_y), method='cubic')

        # размер графика
        xmin = min(well_positions[:, 0])
        xmax = max(well_positions[:, 0])
        ymin = min(well_positions[:, 1])
        ymax = max(well_positions[:, 1])

        return grid_x, grid_y, grid_z, xmin, xmax, ymin, ymax, self.depth
