import os, os.path

class BaseJobRunner( object ):
    def build_command_line( self, job ):
        """
        Compose the sequence of commands necessary to execute a job.
        """
        commands = job.get_command_line()
        # All job runners currently handle this case which should never
        # occur
        if not commands:
            return None
        return commands
