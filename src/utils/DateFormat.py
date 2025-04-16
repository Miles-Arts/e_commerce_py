import datetime

class DateFormar():
    
    def convert_date(self,date):
        return datetime.datetime.strftime(date,'%d/%m/%Y')
        