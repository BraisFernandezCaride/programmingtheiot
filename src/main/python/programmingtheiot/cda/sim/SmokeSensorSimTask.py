#
# This class is part of the Programming the Internet of Things project.
#
# Simulates a smoke sensor using SensorDataGenerator.
#

import logging
import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator

from programmingtheiot.data.SensorData import SensorData

class SmokeSensorSimTask(BaseSensorSimTask):
	"""
	Simulated smoke sensor task. Generates data using SensorDataGenerator.
	"""

	def __init__(self, dataSet = None):
		super(SmokeSensorSimTask, self).__init__(
			name = ConfigConst.SMOKE_SENSOR_NAME,
			typeID = ConfigConst.SMOKE_SENSOR_TYPE,
			dataSet = dataSet,
			minVal = 0.0,               # Rango típico para niveles de humo (0-100)
			maxVal = 100.0
		)