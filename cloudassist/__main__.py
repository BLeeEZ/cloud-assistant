from cloudassist.settings import Settings
from cloudassist.nextcloud import Nextcloud

class CloudAssistant:
    def __init__(self, settings):
        self.__nextcloud = Nextcloud(settings)
        self.__nextcloud.connect_and_get_calendars_methainfo()

    def get_events_for_today(self):
        return self.__nextcloud.get_all_events_as_text_for_today()

def main():
    """Main script function."""
    userSettings = Settings()
    userSettings.load_from_file(Settings.CONF_DIR)
    cloud_assistant = CloudAssistant(userSettings)

    print( cloud_assistant.get_events_for_today() )

if __name__ == "__main__":
    main()
