from mltrain.log import logger
from mltrain.configurations.configuration_set import ConfigurationSet


class Trajectory(ConfigurationSet):
    """Trajectory"""

    @property
    def t0(self) -> float:
        """Initial time of this trajectory

        Returns:
            (float): t_0 in fs
        """
        return 0. if len(self) == 0 else self[0].time

    @t0.setter
    def t0(self, value: float):
        """Set the initial time for a trajectory"""

        for frame in self:
            if frame.time is None:
                logger.warning('Attempted to set the initial time but a '
                               f'time was note defined. Setting to {value}')
                frame.time = value

            else:
                frame.time += value

        return

    @property
    def final_frame(self) -> 'mltrain.Configuration':
        """
        Return the final frame from this trajectory

        Returns:
            (mltrain.Configuration): Frame
        """

        if len(self) == 0:
            raise ValueError('Had no final frame - no configurations present')

        return self[-1]
