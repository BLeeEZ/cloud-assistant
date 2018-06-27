import logging
from settings import Settings, CONF_DIR
from nextcloud import Nextcloud

class CloudAssistant:
    def __init__(self, settings):
        self.__nextcloud = Nextcloud(settings)
        self.__nextcloud.connect_and_get_calendars_methainfo()

    def get_events_for_today(self):
        return self.__nextcloud.get_all_events_as_text_for_today()

def main():
    """Main script function."""
    logging.basicConfig(level=logging.INFO)
    
    userSettings = Settings()
    userSettings.load_from_file(CONF_DIR)
    cloud_assistant = CloudAssistant(userSettings)
    
    logging.info( cloud_assistant.get_events_for_today() )

if __name__ == "__main__":
    main()