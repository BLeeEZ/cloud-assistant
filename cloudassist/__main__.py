from cloudassist.settings import Settings
from cloudassist.cloudassistant import CloudAssistant
from cloudassist.styler.listingstyler import ListingStyler
from cloudassist.styler.reportstyler import ReportStyler
import argparse

def main():
    parser = argparse.ArgumentParser(description="Cloud assistant for command line")
    parser.add_argument('-s', dest='decoraterStyle', action='store',
                       help='Specify the style of the output')
    parser.add_argument('-d', dest='isToday', action='store_true',
                       help='Print appointments for today')
    parser.add_argument('-w', dest='isWeek', action='store_true',
                       help='Print appointments for today to on week in the future')

    args = parser.parse_args()

    if args.decoraterStyle == 'report':
        styler = ReportStyler()
    else:
        styler = ListingStyler()

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
