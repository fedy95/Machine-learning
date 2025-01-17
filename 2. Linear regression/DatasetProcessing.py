import math
import random
import numpy as np
"""
"""


class DatasetProcessing(object):
    """Initialization variables"""
    def __init__(self, area, rooms, price):
        self.area = area
        self.rooms = rooms
        self.price = price

    @staticmethod
    def getDataset(filename):
        """Метод обработки входного датасета.

        file 'dataset.txt': входной датасет, содержащий информацию о точках в виде (area,rooms,price).

        Args:
            filename: имя входного датасета.

        Returns:
            data: лист, содержащий входной датасет в виде (area,rooms,price).
        """
        data = []
        file = open(filename)
        for line in file:
            area, rooms, price = line.split(',')
            data.append([float(area), float(rooms), float(price)])
        file.close()
        random.shuffle(data)
        return data

    @staticmethod
    def getSeparetedData(data):
        """Метод разделения листа вида (area,rooms,price) на составляющие.

        Args:
            data: лист, содержащий входной датасет в виде (area,rooms,price).

        Returns:
            area: лист, содержащий area составляющую датасета.
            rooms: лист, содержащий rooms составляющую датасета.
            price: лист, содержащий price составляющую датасета.
        """
        area = []
        rooms = []
        price = []
        for i in range(len(data)):
            area.append(data[i][0])
            rooms.append(data[i][1])
            price.append(data[i][2])
        return area, rooms, price

    @staticmethod
    def getAvgData(data):
        """Метод получения средних значений составляющих листа вида (area,rooms,price).

        Args:
            data: лист, содержащий входной датасет в виде (area,rooms,price).

        Returns:
            avgArea: переменная, содержащая среднюю area составляющую датасета.
            avgRooms: переменная, содержащая среднюю rooms составляющую датасета.
            avgPrice: переменная, содержащая среднюю price составляющую датасета.
        """
        area, rooms, price = DatasetProcessing.getSeparetedData(data)
        sumArea = 0
        sumRooms = 0
        sumPrice = 0

        for i in range(len(area)):
            sumArea = sumArea + area[i]
            sumRooms = sumRooms + rooms[i]
            sumPrice = sumPrice + price[i]

        avgArea = sumArea / len(area)
        avgRooms = sumRooms / len(rooms)
        avgPrice = sumPrice / len(price)
        return avgArea, avgRooms, avgPrice

    @staticmethod
    def getStandardDeviationData(data):
        """Метод получения стандарного отклонения составляющих листа вида (area,rooms,price).

        Args:
            data: лист, содержащий входной датасет в виде (area,rooms,price).

        Returns:
            standardDeviationArea: переменная, содержащая стандартное отклонение состоявляющей area.
            standardDeviationRooms: переменная, содержащая стандартное отклонение состоявляющей rooms.
            standardDeviationPrice: переменная, содержащая стандартное отклонение состоявляющей price.
        """
        avgArea, avgRooms, avgPrice = DatasetProcessing.getAvgData(data)
        area, rooms, price = DatasetProcessing.getSeparetedData(data)

        differenceWithAvgArea = []
        differenceWithAvgRooms = []
        differenceWithAvgPrice = []
        squareDifferenceWithAvgArea = []
        squareDifferenceWithAvgRooms = []
        squareDifferenceWithAvgPrice = []
        sumSquaresDifferenceWithAvgArea = 0
        sumSquaresDifferenceWithAvgRooms = 0
        sumSquaresDifferenceWithAvgPrice = 0
        dispersionArea = 0
        dispersionRooms = 0
        dispersionPrice = 0
        for i in range(len(area)):
            differenceWithAvgArea.append(area[i] - avgArea)
            differenceWithAvgRooms.append(rooms[i] - avgRooms)
            differenceWithAvgPrice.append(price[i] - avgPrice)

            squareDifferenceWithAvgArea.append((area[i] - avgArea) ** 2)
            squareDifferenceWithAvgRooms.append((rooms[i] - avgRooms) ** 2)
            squareDifferenceWithAvgPrice.append((price[i] - avgPrice) ** 2)

            sumSquaresDifferenceWithAvgArea = sumSquaresDifferenceWithAvgArea + squareDifferenceWithAvgArea[i]
            sumSquaresDifferenceWithAvgRooms = sumSquaresDifferenceWithAvgRooms + squareDifferenceWithAvgRooms[i]
            sumSquaresDifferenceWithAvgPrice = sumSquaresDifferenceWithAvgPrice + squareDifferenceWithAvgPrice[i]

        dispersionArea = sumSquaresDifferenceWithAvgArea / (len(area) - 1)  # len(area) > 30 => n-1
        dispersionRooms = sumSquaresDifferenceWithAvgRooms / (len(rooms) - 1)
        dispersionPrice = sumSquaresDifferenceWithAvgPrice / (len(price) - 1)

        standardDeviationArea = round(math.sqrt(dispersionArea))
        standardDeviationRooms = round(math.sqrt(dispersionRooms))
        standardDeviationPrice = round(math.sqrt(dispersionPrice))
        return standardDeviationArea, standardDeviationRooms, standardDeviationPrice

    @staticmethod
    def getNormalizeDataset(inputData):
        """Метод нормализации входного датасета.

        Сдвиг (-) каждой составляющей на среднее значение + деление на стандарное отклонение
        Args:
            inputData: лист, содержащий входной датасет в виде (area,rooms,price).

        Returns:
            normalizeData: лист, содержащий нормализованный датасет в виде (area,rooms,price).
        """
        area, rooms, price = DatasetProcessing.getSeparetedData(inputData)
        avgArea, avgRooms, avgPrice = DatasetProcessing.getAvgData(inputData)
        standardDeviationArea, standardDeviationRooms, standardDeviationPrice = DatasetProcessing.getStandardDeviationData(inputData)

        normalizeData = []
        for i in range(len(inputData)):
            normalizeData.append([(area[i] - avgArea) / standardDeviationArea,
                               (rooms[i] - avgRooms) / standardDeviationRooms,
                               (price[i] - avgPrice) / standardDeviationPrice])
        return normalizeData

    @staticmethod
    def getNormalizeInputDataset(areaInputList, roomsInputList):
        """Метод нормализации введенного датасета areaInput, roomsInput.

        Сдвиг (-) каждой составляющей на среднее значение + деление на стандарное отклонение
        Args:
            areaInputList: лист, содержащий area составляющую.
            roomsInputList: лист, содержащий rooms составляющую.

        Returns:
            normalizeAreaInput: лист, содержащий нормализованные значения areaInput.
            normalizeRoomsInput: лист, содержащий нормализованные значения roomsInput.
        """
        sumArea = 0
        sumRooms = 0

        for i in range(len(areaInputList)):
            sumArea = sumArea + areaInputList[i]
            sumRooms = sumRooms + roomsInputList[i]

        avgAreaInput = sumArea / len(areaInputList)
        avgRoomsInput = sumRooms / len(roomsInputList)

        differenceWithAvgArea = []
        differenceWithAvgRooms = []
        squareDifferenceWithAvgArea = []
        squareDifferenceWithAvgRooms = []
        sumSquaresDifferenceWithAvgArea = 0
        sumSquaresDifferenceWithAvgRooms = 0
        dispersionArea = 0
        dispersionRooms = 0
        for i in range(len(areaInputList)):
            differenceWithAvgArea.append(areaInputList[i] - avgAreaInput)
            differenceWithAvgRooms.append(roomsInputList[i] - avgRoomsInput)

            squareDifferenceWithAvgArea.append((areaInputList[i] - avgAreaInput) ** 2)
            squareDifferenceWithAvgRooms.append((roomsInputList[i] - avgRoomsInput) ** 2)

            sumSquaresDifferenceWithAvgArea = sumSquaresDifferenceWithAvgArea + squareDifferenceWithAvgArea[i]
            sumSquaresDifferenceWithAvgRooms = sumSquaresDifferenceWithAvgRooms + squareDifferenceWithAvgRooms[i]

        dispersionArea = sumSquaresDifferenceWithAvgArea / (len(areaInputList) - 1)  # len(area) > 30 => n-1
        dispersionRooms = sumSquaresDifferenceWithAvgRooms / (len(roomsInputList) - 1)

        standardDeviationAreaInput = round(math.sqrt(dispersionArea))
        standardDeviationRoomsInput = round(math.sqrt(dispersionRooms))
        normalizeAreaInput = []
        normalizeRoomsInput = []
        for i in range(len(areaInputList)):
            normalizeAreaInput.append([(areaInputList[i] - avgAreaInput) / standardDeviationAreaInput])
            normalizeRoomsInput.append([(roomsInputList[i] - avgRoomsInput) / standardDeviationRoomsInput])
        return normalizeAreaInput, normalizeRoomsInput

    @staticmethod
    def getCombinedInputData(areaInputList, roomsInputList, priceNormalizeInputList):
        """Метод обработки введенных и рассчитанных датасетов.

        Args:
            areaInputList: лист, содержащий area составляющую.
            roomsInputList: лист, содержащий rooms составляющую.
            priceNormalizeInputList: лист, содержащий нормализованную price составляющую.

        Returns:
            normalizeDataInput: лист, содержащий введенные объединненные нормализованне датасеты
             в виде (areaNormalizeInputList,roomsNormalizeInputList,priceNormalizeInputList).
        """
        areaNormalizeInputList, roomsNormalizeInputList = \
            DatasetProcessing.getNormalizeInputDataset(areaInputList, roomsInputList)
        normalizeDataInput = []
        for i in range(len(areaNormalizeInputList)):
            normalizeDataInput.append([areaNormalizeInputList[i][0],
                                       roomsNormalizeInputList[i][0], priceNormalizeInputList[i]])
        return normalizeDataInput
