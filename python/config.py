"""
config
File holds the configuration class and corresponding functionalities
"""


class Config:
    """
    Configuration class
    """

    def __init__(self):
        """
        Constructor of the configuration class
        """
        self.max_concurrent_parsers = 50

        self.db_host = "127.0.0.1"
        self.db_name = "INB"
        self.db_port = 5432
        self.db_username = "postgres"
        self.db_password = "postgres"


config = Config()
