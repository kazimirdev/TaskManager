import datetime, pytz


def convert_to_server_time(dt, tz, stz):
    tz = pytz.timezone(tz) 
    stz = pytz.timezone(stz)

    dt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M")
    dt = tz.localize(dt).astimezone(stz).strftime("%Y-%m-%d %H:%M")
    dt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M")
    return dt



