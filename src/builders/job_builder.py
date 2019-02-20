from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class JobBuilder(BaseBuilder):
    def __init__(self):
        super(JobBuilder, self).__init__()
        self._required_arguments = [
            JOB_NAME,
            MODEL_NAME,
            RUN_JOB_AUTOMATICALLY,
            CPU_COUNT,
            USER_SUBROUTINE
        ]

    def _build(self, **kwargs):
        model_name = kwargs[MODEL_NAME],
        job_name = kwargs[JOB_NAME],
        auto_run = kwargs[RUN_JOB_AUTOMATICALLY]
        cpu_count = kwargs[CPU_COUNT]
        subroutine_path = kwargs[USER_SUBROUTINE]
        self.__create_job(model_name, job_name, cpu_count, subroutine_path)

        if auto_run:
            self.__run_job(job_name)

    @staticmethod
    def __run_job(job_name):
        mdb.jobs[job_name].submit(consistencyChecking=OFF)

    @staticmethod
    def __create_job(model_name, job_name, cpu_count, subroutine_path):
        job_description = 'Job for model %s' % model_name
        mdb.Job(name=job_name, model=model_name, description=job_description, type=ANALYSIS, atTime=None,
                waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
                userSubroutine=subroutine_path, scratch='',
                resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=cpu_count, numGPUs=0)
