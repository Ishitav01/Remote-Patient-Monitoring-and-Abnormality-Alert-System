import time

class InactivityTracker:
    def __init__(self, inactivity_threshold=300):
        
        """
        Initializes the inactivity tracker.
        :param inactivity_threshold: Time in seconds after which inactivity is flagged.
        """
        self.inactivity_threshold = inactivity_threshold
        self.last_movement_time = time.time()
        self.inactivity_alerted = False  # To prevent multiple alerts

    def update_activity(self, is_moving):
        """
        Updates the timestamp for the last movement.
        :param is_moving: Boolean indicating if the person is moving.
        """
        if is_moving:
            self.last_movement_time = time.time()
            self.inactivity_alerted = False  # Reset alert flag

    def check_inactivity(self):
        """
        Checks if the inactivity threshold has been crossed.
        :return: Boolean indicating if inactivity alert should be triggered.
        """
        current_time = time.time()
        if (current_time - self.last_movement_time >= self.inactivity_threshold) and not self.inactivity_alerted:
            self.inactivity_alerted = True
            return True  # Inactivity alert
        return False
