# -*- coding: utf-8 -*-
import caldav
from caldav.elements import dav, cdav
from datetime import datetime, date, timedelta

class VCalendarWrapper(object):
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

    def to_text(self):
        return 'Der Termin {} beginnt am {} um {} Uhr und endet um {} Uhr.'.format(
        self.__summary, 
        self.__start_datetime.strftime("%d.%m.%Y"), 
        self.__start_datetime.strftime("%H:%M"),
        self.__end_datetime.strftime("%H:%M")
        )

class Nextcloud(object):
    def __init__(self, credentials):
        self.__url = credentials.server_url_dav
        self.__user_name = credentials.user_name
        self.__user_pw = credentials.user_password
        self.__proxy = credentials.proxy
        self.__client = caldav.DAVClient(self.__url, username=self.__user_name, password=self.__user_pw, ssl_verify_cert=False, proxy=self.__proxy)
        self.__principal = None
        self.__calendars = None
        self.__disable_insecure_request_warnings()

    def __disable_insecure_request_warnings(self):
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    def connect_and_get_calendars_methainfo(self):
        self.__principal = self.__client.principal()
        self.__calendars = self.__principal.calendars()

    def get_all_events_between(self, startdate, enddate):
        events_found = []
        return_text = ''
        if len(self.__calendars) > 0:
            for calendar in self.__calendars:
                results = calendar.date_search(startdate, enddate)

                for event in results:
                    calendarEntry = VCalendarWrapper(event.data)
                    events_found.append(calendarEntry.to_text())
        return events_found

    def convert_events_to_text(self, events_list):
        if len(events_list) > 0:
            return_text = 'Es stehen {} Termin an.\n'.format(len(events_list))
            for found_event in events_list:
                return_text = return_text + found_event + '\n'
        else:
            return_text = 'Heute stehen keine Termin an.'
        return return_text

    def get_all_events_as_text_for_today(self):
        startdate = date.today()
        enddate = date.today() + timedelta(days=1)
        events_list = self.get_all_events_between(startdate, enddate)
        return self.convert_events_to_text(events_list)
