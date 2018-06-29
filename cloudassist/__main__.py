from cloudassist.settings import Settings
from cloudassist.nextcloud import Nextcloud, OutputStyler, DecoratedOutputStyler

class CloudAssistant:
    def __init__(self, settings):
        self.__nextcloud = Nextcloud(settings)
        self.__nextcloud.connect_and_get_calendars_methainfo()

    def print_all_appointments_for_today(self, styler):
        print( styler.formatAppointments(self.__nextcloud.get_all_appointments_for_today()) )

    def print_all_appointments_till_one_week(self, styler):
        print( styler.formatAppointments(self.__nextcloud.get_all_appointments_for_this_week()) )

def main():
    """Main script function."""
    userSettings = Settings()
    userSettings.load_from_file(Settings.CONF_DIR)
    cloud_assistant = CloudAssistant(userSettings)

    styler = DecoratedOutputStyler()
    cloud_assistant.print_all_appointments_till_one_week(styler)

if __name__ == "__main__":
    main()
