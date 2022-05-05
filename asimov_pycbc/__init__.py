"""
An integration to allow asimov to access PyCBC
"""
import importlib

from asimov.pipeline import Pipeline
from asimov import logger

import os.path

__version__ = "0.0.1"

class PyCBC(Pipeline):
    """
    The PyCBC Pipeline integration for asimov.

    This integration allows asimov to create and monitor PyCBC jobs.
    """

    config_template = importlib.resources.path(__name__, 'pycbc.ini')
    _pipeline_command = "pycbc_inference"

    def __init__(self, analysis):
        super().__init__(analysis)

    def detect_completion(self):
        """
        Check for the production of a final posterior file to
        signal that a job has been completed.
        """
        raise NotImplementedError

    def build_dag(self):
        """
        Construct a DAG file for the analysis to be passed to ``pycbc_inference``.
        """

        command = [self._pipeline_command,
                   ini,
                   "--output-file", self.analysis.rundir,
                   "--nprocesses", self.analysis.sampling['processes'],
                   "--force"
        ]
        self.logger.info(" ".join(command))

        pipe = subprocess.Popen(command, 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        out, err = pipe.communicate()

        self.logger.info(out)
        self.logger.error(err)
        

    def submit_dag(self):
        """
        Submit the DAG file to the cluster.
        """
        pass

    def collect_assets(self):
        """
        Collect all of the output assets for this job.
        """
        pass

    def samples(self):
        """
        Collect the combined samples file for PESummary.
        """
        pass

    def after_completion(self):
        """
        A hook to be run after the pipeline is detected to have completed.
        """
        pass

    def collect_logs(self):
        """
        Collect all of the log files produced by this pipeline and return their contents as a dictionary.
        """
        pass

    def check_progress(self):
        """
        Return the progress of this job.
        """
        pass

    def read_ini(self):
        """
        Read and parse a configuration file for this pipeline.
        """
        pass

    def resurrect(self):
        """
        Attempt to fix and restart a stuck or failed job.
        """
        pass
