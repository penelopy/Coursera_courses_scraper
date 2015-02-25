import re
from datetime import datetime, date

def parse_date_fields(input_string):

    # Create regex strings for individual text
    strip_junk_1 = '(?:<p>)'
    month_regex = '(?P<three_char_month>\w{3})'
    strip_junk_2 = '(?:\s)'
    day_regex = '(?P<day_num>\d+)'
    strip_junk_3 = '(?:\w{2},\s)'
    year_regex = '(?P<four_dig_year>\d{4})'
    strip_junk_4 = '(?:<br>)'
    alt_text_regex = '(?P<alt_text>.+)'
    strip_junk_5 = '(?:</br>)'

    # Build master regex string
    all_regex = strip_junk_1 + \
                month_regex + \
                strip_junk_2 + \
                day_regex + \
                strip_junk_3 + \
                year_regex + \
                strip_junk_4 + \
                alt_text_regex + \
                strip_junk_5
    # Perform regex search
    matches = re.search(all_regex, input_string)
    return matches

# input_string = '<p>Jan 23rd, 2015<br>6 weeks long</br></p>'
# matches = parse_date_fields(input_string)


def clean_date_data(matches):    
    try: 
        month_num_text = matches.group('three_char_month')
        date_dic = {"Jan":1, "Feb": 2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        month_num = date_dic.get(month_num_text)
        day_num = matches.group('day_num')
        year= matches.group('four_dig_year')
        duration= matches.group('alt_text')
        course_begins = date(int(year),int(month_num),int(day_num))
    except: 
        course_begins = None
        duration = None
    # try:
    #     day_num = matches.group('day_num')
    # except:
    #     course_begins = None
    #     year= matches.group('four_dig_year')
    #     course_begins = None
    #     duration= matches.group('alt_text')
    #     course_begins = None
    #     course_begins = date(int(year),int(month_num),int(day_num))
    
    return course_begins, duration





