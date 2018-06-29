from datetime import datetime

class VCalendarWrapper(object):
    @property
    def summary(self):
        return self.__summary
    @property
    def startDateTime(self):
        return self.__start_datetime
    @property
    def startDate(self):
        return self.__start_datetime.strftime("%d.%m.%Y")
    @property
    def startTime(self):
        return self.__start_datetime.strftime("%H:%M")
    @property
    def endDateTime(self):
        return self.__end_datetime
    @property
    def endDate(self):
        return self.__end_datetime.strftime("%d.%m.%Y")
    @property
    def endTime(self):
        return self.__end_datetime.strftime("%H:%M")

    def __init__(self, calendar_data):
        self.__calendar_data = calendar_data
        self.__start_datetime = None
        self.__end_datetime = None
        self.__summary = None
        self.__analyze()

    def __datetime_string_to_datetime(self, text):
        return datetime.strptime(text, '%Y%m%dT%H%M%SZ')
    def __date_string_to_datetime(self, text):
        return datetime.strptime(text, '%Y%m%d')

    def __analyze(self):
        for line in self.__calendar_data.split('\r\n'):
            if 'DTSTART:' in line:
                self.__start_datetime = self.__datetime_string_to_datetime( line.replace('DTSTART:', '') )
            if 'DTSTART;VALUE=DATE:' in line:
                self.__start_datetime = self.__date_string_to_datetime( line.replace('DTSTART;VALUE=DATE:', '') )

            if 'DTEND:' in line:
                self.__end_datetime = self.__datetime_string_to_datetime( line.replace('DTEND:', '') )
            if 'DTEND;VALUE=DATE:' in line:
                self.__end_datetime = self.__date_string_to_datetime( line.replace('DTEND;VALUE=DATE:', '') )

            if 'SUMMARY:' in line:
                self.__summary = line.replace('SUMMARY:', '')