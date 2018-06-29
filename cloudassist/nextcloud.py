# -*- coding: utf-8 -*-
import caldav
from caldav.elements import dav, cdav
from datetime import datetime, date, timedelta
from cloudassist.vcalendarwrapper import VCalendarWrapper

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

    def get_all_appointments_between(self, startdate, enddate):
        appointments_found = []
        if len(self.__calendars) > 0:
            for calendar in self.__calendars:
                results = calendar.date_search(startdate, enddate)

                for appointment in results:
                    calendarEntry = VCalendarWrapper(appointment.data)
                    appointments_found.append(calendarEntry)
        appointments_found.sort(key= lambda x: x.startDateTime)
        return appointments_found

    def get_all_appointments_for_today(self):
        startdate = date.today()
        enddate = date.today() + timedelta(days=1)
        return self.get_all_appointments_between(startdate, enddate)

    def get_all_appointments_for_this_week(self):
        startdate = date.today()
        enddate = date.today() + timedelta(days=7)
        return self.get_all_appointments_between(startdate, enddate)
