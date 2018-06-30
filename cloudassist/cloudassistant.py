from cloudassist.nextcloud import Nextcloud

class CloudAssistant:
    def __init__(self, settings):
        self.__nextcloud = Nextcloud(settings)
        self.__nextcloud.connect_and_get_calendars_methainfo()

    def print_all_appointments_for_today(self, styler):
        print( styler.format_appointments(self.__nextcloud.get_all_appointments_for_today()) )

    def print_all_appointments_till_one_week(self, styler):
        print( styler.format_appointments(self.__nextcloud.get_all_appointments_for_this_week()) )
