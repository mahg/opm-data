
class ComparisonData():
    def __init__(self, compared_keyword):
        self.__compared_keyword = compared_keyword
        self.__avg_absolute_set = False
        self.__avg_relative_set = False
        self.__average_absolute_deviation = 0
        self.__average_relative_deviation = 0
        self.__median_absolute_set = False
        self.__median_relative_set = False
        self.__median_absolute_deviation = 0
        self.__median_relative_deviation = 0

    def getKeywordName(self):
        return self.__compared_keyword

    def numberOfTimesteps(self):
        return 0

    def getAverageAbsoluteDeviation(self):
        if (not self.__avg_absolute_set):
            raise RuntimeError("Cannot get average absolute deviation, comparison has not been performed")
        else:
            return self.__average_absolute_deviation

    def setAverageAbsoluteDeviation(self, absolution_deviation):
        self.__average_absolute_deviation = absolution_deviation
        self.__avg_absolute_set = True

    def getAverageRelativeDeviation(self):
        if (not self.__average_relative_deviation):
            raise RuntimeError("Cannot get average relative deviation, comparison has not been performed")
        else:
            return self.__average_relative_deviation

    def setAverageRelativeDeviation(self, relative_deviation):
        self.__average_relative_deviation = relative_deviation
        self.__avg_relative_set = True

    def getMedianRelativeDeviation(self):
        if (not self.__median_relative_deviation):
            raise RuntimeError("Cannot get median relative deviation, comparison has not been performed")
        else:
            return self.__median_relative_deviation

    def setMedianRelativeDeviation(self, relative_deviation):
        self.__median_relative_deviation = relative_deviation
        self.__median_relative_set = True

    def getMedianAbsoluteDeviation(self):
        if (not self.__median_absolute_deviation):
            raise RuntimeError("Cannot get median absolute deviation, comparison has not been performed")
        else:
            return self.__median_absolute_deviation

    def setMedianAbsoluteDeviation(self, absolute_deviation):
        self.__median_absolute_deviation = absolute_deviation
        self.__median_absolute_set = True