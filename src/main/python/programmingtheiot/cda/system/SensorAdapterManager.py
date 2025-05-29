#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#



import logging

from importlib import import_module

from apscheduler.schedulers.background import BackgroundScheduler

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
from programmingtheiot.cda.sim.HumiditySensorSimTask import HumiditySensorSimTask
from programmingtheiot.cda.sim.TemperatureSensorSimTask import TemperatureSensorSimTask
from programmingtheiot.cda.sim.PressureSensorSimTask import PressureSensorSimTask

from programmingtheiot.cda.sim.SmokeSensorSimTask import SmokeSensorSimTask


class SensorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""

	def _initEnvironmentalSensorTasks(self):
		humidityFloor   = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.HUMIDITY_SIM_FLOOR_KEY, defaultVal = SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY)
		humidityCeiling = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.HUMIDITY_SIM_CEILING_KEY, defaultVal = SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)

		pressureFloor   = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.PRESSURE_SIM_FLOOR_KEY, defaultVal = SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE)
		pressureCeiling = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.PRESSURE_SIM_CEILING_KEY, defaultVal = SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE)

		tempFloor       = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.TEMP_SIM_FLOOR_KEY, defaultVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP)
		tempCeiling     = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.TEMP_SIM_CEILING_KEY, defaultVal = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)


		if not self.useEmulator:
			self.dataGenerator = SensorDataGenerator()

			humidityData = \
				self.dataGenerator.generateDailyEnvironmentHumidityDataSet( \
					minValue = humidityFloor, maxValue = humidityCeiling, useSeconds = False)
			pressureData = \
				self.dataGenerator.generateDailyEnvironmentPressureDataSet( \
					minValue = pressureFloor, maxValue = pressureCeiling, useSeconds = False)
			tempData     = \
				self.dataGenerator.generateDailyIndoorTemperatureDataSet( \
					minValue = tempFloor, maxValue = tempCeiling, useSeconds = False)
			
			smokeData    =  \
				self.dataGenerator.generateDailySmokeLevelDataSet(
					minValue = 0.0, maxValue = 100.0, useSeconds = False)
			
			

			self.humidityAdapter = HumiditySensorSimTask(dataSet = humidityData)
			self.pressureAdapter = PressureSensorSimTask(dataSet = pressureData)
			self.tempAdapter     = TemperatureSensorSimTask(dataSet = tempData)
			self.smokeAdapter = SmokeSensorSimTask(dataSet = smokeData)

		else:
			heModule = import_module('programmingtheiot.cda.emulated.HumiditySensorEmulatorTask', 'HumiditySensorEmulatorTask')
			heClazz = getattr(heModule, 'HumiditySensorEmulatorTask')
			self.humidityAdapter = heClazz()

			peModule = import_module('programmingtheiot.cda.emulated.PressureSensorEmulatorTask', 'PressureSensorEmulatorTask')
			peClazz = getattr(peModule, 'PressureSensorEmulatorTask')
			self.pressureAdapter = peClazz()

			teModule = import_module('programmingtheiot.cda.emulated.TemperatureSensorEmulatorTask', 'TemperatureSensorEmulatorTask')
			teClazz = getattr(teModule, 'TemperatureSensorEmulatorTask')
			self.tempAdapter = teClazz()

			seModule = import_module('programmingtheiot.cda.emulated.SmokeSensorEmulatorTask', 'SmokeSensorEmulatorTask')
			seClazz = getattr(seModule, 'SmokeSensorEmulatorTask')
			self.smokeAdapter = seClazz()

	def _initEnvironmentalSensorTasks(self):
		humidityFloor   = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.HUMIDITY_SIM_FLOOR_KEY, defaultVal = SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY)
		humidityCeiling = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.HUMIDITY_SIM_CEILING_KEY, defaultVal = SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)

		pressureFloor   = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.PRESSURE_SIM_FLOOR_KEY, defaultVal = SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE)
		pressureCeiling = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.PRESSURE_SIM_CEILING_KEY, defaultVal = SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE)

		tempFloor       = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.TEMP_SIM_FLOOR_KEY, defaultVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP)
		tempCeiling     = \
			self.configUtil.getFloat( \
				section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.TEMP_SIM_CEILING_KEY, defaultVal = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)

		if not self.useEmulator:
			self.dataGenerator = SensorDataGenerator()

			humidityData = \
				self.dataGenerator.generateDailyEnvironmentHumidityDataSet( \
					minValue = humidityFloor, maxValue = humidityCeiling, useSeconds = False)
			pressureData = \
				self.dataGenerator.generateDailyEnvironmentPressureDataSet( \
					minValue = pressureFloor, maxValue = pressureCeiling, useSeconds = False)
			tempData     = \
				self.dataGenerator.generateDailyIndoorTemperatureDataSet( \
					minValue = tempFloor, maxValue = tempCeiling, useSeconds = False)

			self.humidityAdapter = HumiditySensorSimTask(dataSet = humidityData)
			self.pressureAdapter = PressureSensorSimTask(dataSet = pressureData)
			self.tempAdapter     = TemperatureSensorSimTask(dataSet = tempData)

		else:
			heModule = import_module('programmingtheiot.cda.emulated.HumiditySensorEmulatorTask', 'HumiditySensorEmulatorTask')
			heClazz = getattr(heModule, 'HumiditySensorEmulatorTask')
			self.humidityAdapter = heClazz()

			peModule = import_module('programmingtheiot.cda.emulated.PressureSensorEmulatorTask', 'PressureSensorEmulatorTask')
			peClazz = getattr(peModule, 'PressureSensorEmulatorTask')
			self.pressureAdapter = peClazz()

			teModule = import_module('programmingtheiot.cda.emulated.TemperatureSensorEmulatorTask', 'TemperatureSensorEmulatorTask')
			teClazz = getattr(teModule, 'TemperatureSensorEmulatorTask')
			self.tempAdapter = teClazz()	

	def handleTelemetry(self):
		humidityData = self.humidityAdapter.generateTelemetry()
		pressureData = self.pressureAdapter.generateTelemetry()
		tempData     = self.tempAdapter.generateTelemetry()
		smokeData = self.smokeAdapter.generateTelemetry()

		humidityData.setLocationID(self.locationID)
		pressureData.setLocationID(self.locationID)
		tempData.setLocationID(self.locationID)
		smokeData.setLocationID(self.locationID)

		logging.debug('Generated humidity data: ' + str(humidityData))
		logging.debug('Generated pressure data: ' + str(pressureData))
		logging.debug('Generated temp data: ' + str(tempData))
		logging.debug('Generated smoke data: ' + str(smokeData))

		if self.dataMsgListener:
			self.dataMsgListener.handleSensorMessage(humidityData)
			self.dataMsgListener.handleSensorMessage(pressureData)
			self.dataMsgListener.handleSensorMessage(tempData)
			self.dataMsgListener.handleSensorMessage(smokeData)
		
	def setDataMessageListener(self, listener: IDataMessageListener):
		if listener:
			self.dataMsgListener = listener
			

	def startManager(self) -> bool:
		logging.info("Started SensorAdapterManager.")

		if not self.scheduler.running:
			self.scheduler.start()
			return True
		else:
			logging.info("SensorAdapterManager scheduler already started. Ignoring.")
			return False

	def stopManager(self) -> bool:
		logging.info("Stopped SensorAdapterManager.")

		try:
			self.scheduler.shutdown()
			return True
		except:
			logging.info("SensorAdapterManager scheduler already stopped. Ignoring.")
		return False

def __init__(self, useEmulator: bool = False):
	self.useEmulator = useEmulator
	self.scheduler = BackgroundScheduler()
	self.configUtil = ConfigUtil()
	self.locationID = 1
	self.dataMsgListener = None

	self.humidityAdapter = None
	self.pressureAdapter = None
	self.tempAdapter = None
	self.smokeAdapter = None  

	self._initEnvironmentalSensorTasks()