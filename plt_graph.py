import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class HeatMap:
    def __init__(self, grid_x, grid_y, grid_z, xmin, xmax, ymin, ymax, depth):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.grid_z = grid_z
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.depth = depth

    def chart(self):
        # Строим тепловую карту
        self.figure = plt.figure(figsize=(10, 8))
        self.canvas = FigureCanvas(self.figure)
        # колорбар
        self.im = plt.imshow(self.grid_z.T, extent=(self.xmin, self.xmax, self.ymin, self.ymax),
                             origin='lower', cmap='YlGnBu_r', aspect='auto')
        cbar = plt.colorbar(self.im, ax=plt.gca(), orientation='vertical', fraction=0.046, pad=0.15)
        # Получаем текущие границы цветовой шкалы
        cbar_ax = cbar.ax

        # Добавляем текст слева от цветовой шкалы
        cbar_ax.text(-1, 0.5, 'Температура (°C)', rotation=90,
                     va='center', ha='center', transform=cbar_ax.transAxes, fontsize=12)

        plt.title(f'Тепловая карта на глубине {self.depth} м')
        contours = plt.contour(self.grid_x, self.grid_y, self.grid_z, levels=10, colors='black',
                               linewidths=0.4)  # levels=10 для 10 уровней контуров
        plt.clabel(contours, inline=True, fontsize=6, fmt='%.2f')  # Добавление меток на контуры
        plt.axis("off")  # убираю разметку координат
        # добавляю подписи ТС
        plt.text(self.xmin - 10, self.ymax, 'ТС-1', ha='left', va='top', fontsize=16)
        plt.text(self.xmax + 10, self.ymax, 'ТС-3', ha='right', va='top', fontsize=16)
        plt.text(self.xmin - 10, self.ymin, 'ТС-2', ha='left', va='bottom', fontsize=16)
        plt.text(self.xmax + 10, self.ymin, 'ТС-4', ha='right', va='bottom', fontsize=16)

