# 
# This class is part of the Programming the Internet of Things project.
# 
# Simulates a smoke sensor using random values.
#

from programmingtheiot.data.SensorData import SensorData

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask

import random

class SmokeSensorEmulatorTask(BaseSensorSimTask):
	"""
	Simulated smoke sensor. Generates values between 0 and 100.
	"""

	def __init__(self):
		super(SmokeSensorEmulatorTask, self).__init__(
			name = ConfigConst.SMOKE_SENSOR_NAME,
			typeID = ConfigConst.SMOKE_SENSOR_TYPE
		)

	def generateTelemetry(self) -> SensorData:
		sensorData = SensorData(name = self.getName(), typeID = self.getTypeID())

		# Emulate smoke level as a random float between 0 and 100
		sensorVal = round(random.uniform(0, 100), 2)

		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData

		return sensorData