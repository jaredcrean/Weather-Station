import time
import threading
import Adafruit_BMP.BMP085 as BMP085
import csv


class Weather():
    def __init__(self):
        self.sensor = BMP085.BMP085()
        p = self.sensor
        self.pressure = '{0:0.2f}'.format(p.read_pressure())


    def messure_pressure(self, pressure):
        """
        Take the pressure messurement
        """
        #return self.pressure
        print(self.pressure)


    def write_csv(self, fileName, data):
        """
        Write a time stamp and data to CSV file
        """
            
        with open(fileName, 'a') as dataFile:
            t = time.ctime()
            writer = csv.writer(dataFile, delimiter= ' ')
            writer.writerow([t, data])
            dataFile.close()
            print(data)
            t = threading.Timer(30.0, lambda: write_csv(fileName, data))
            t.start()
