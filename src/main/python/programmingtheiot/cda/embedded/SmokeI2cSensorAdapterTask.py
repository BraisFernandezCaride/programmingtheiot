#
# This class is part of the Programming the Internet of Things project.
#
# Shell implementation of an I2C smoke sensor adapter.
#

import logging
from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst

class SmokeI2cSensorAdapterTask():
	"""
	Adapter for a smoke sensor communicating over I2C (simulated or real).
	"""

	def __init__(self):
		self.latestVal = 0.0
		self.sensorName = ConfigConst.SMOKE_SENSOR_NAME
		self.sensorType = ConfigConst.SMOKE_SENSOR_TYPE
		logging.info("SmokeI2cSensorAdapterTask initialized.")

	def generateTelemetry(self) -> SensorData:
		# Aquí simulas lectura I2C. En un sensor real usarías librería de hardware, como smbus.
		import random
		self.latestVal = round(random.uniform(0.0, 100.0), 2)  # Valor simulado de 0 a 100

		sensorData = SensorData(name=self.sensorName, typeID=self.sensorType)
		sensorData.setValue(self.latestVal)

		logging.debug(f"Generated smoke sensor data: {self.latestVal}")
		return sensorData

	def getTelemetryValue(self) -> float:
		return self.latestVal
