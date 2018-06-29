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

import argparse
def main():
    parser = argparse.ArgumentParser(description="Cloud assistant for command line")
    parser.add_argument('-d', dest='decoraterStyle', action='store_true',
                       help='Specify the style of the output')
    parser.add_argument('-t', dest='isToday', action='store_true',
                       help='Print appointments for today')
    parser.add_argument('-w', dest='isWeek', action='store_true',
                       help='Print appointments for today to on week in the future')

    args = parser.parse_args()
    
    if args.decoraterStyle:
        styler = DecoratedOutputStyler()
    else:
        styler = OutputStyler()

    userSettings = Settings()
    userSettings.load_from_file(Settings.CONF_DIR)
    cloud_assistant = CloudAssistant(userSettings)

    if args.isToday:
        cloud_assistant.print_all_appointments_for_today(styler)
    elif args.isWeek:
        cloud_assistant.print_all_appointments_till_one_week(styler)
    else:
        cloud_assistant.print_all_appointments_for_today(styler)

if __name__ == "__main__":
    main()
