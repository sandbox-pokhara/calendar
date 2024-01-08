from bs4 import BeautifulSoup as bs
from template import month_template

file_name = "README.md"


def get_file():
    with open(file_name, 'r') as file:
        content = file.read()
    return content


def get_existing_y_m(file=None):
    if file is None:
        file = get_file()
    soup = bs(file, 'html.parser')
    cal_els = soup.find_all('div', class_='item')
    years = [int(item['id'].split('-')[0]) for item in cal_els]
    months = [int(item['id'].split('-')[1]) for item in cal_els]
    y_m = list(zip(years, months))
    return y_m


def get_red_days(month_el):
    red_els = month_el.select('td[class*=box] span[style*="color:red"]')
    red_days = [int(item.text) for item in red_els]
    return red_days


def get_holidays_str(month_el):
    holiday_el = month_el.find('div', class_='holidays')
    holiday_str = holiday_el.p.text
    return holiday_str


def get_sorted(html):
    soup = bs(html, 'html.parser')
    cal_els = soup.find_all('div', class_='item')
    months_dict = {int(item['id'].split(
        '-')[0]+item['id'].split('-')[1].zfill(2)): item for item in cal_els}
    sorted_items = sorted(months_dict.items())
    return "".join([str(item[1]) for item in sorted_items])


def create_month(
    year,
    month,
    monthName,
    start_weekday,
    end_day,
    days,
    days_int,
    file=None,
    template=month_template
):
    if file is None:
        file = get_file()
    y_m = get_existing_y_m()
    if (year, month) in y_m:
        print(f"{year}-{month} already exists. Use replace.")
        return False
    month_html = template.format(year=year, month=month, mName=monthName, start_weekday=start_weekday,
                                 end_day=end_day, days=days, days_int=days_int, holidays_str="")
    added_html = file + "\n" + month_html
    s_month_html = get_sorted(added_html)
    with open(file_name, 'w') as f:
        f.write(s_month_html)
    return True


def create_red_day(
    year,
    month,
    day,
    reason,
    file=None
):
    if file is None:
        file = get_file()
    soup = bs(file, 'html.parser')
    cal_el = soup.find('div', class_='item', id=f"{year}-{month}")
    existing_hdays = get_red_days(cal_el)
    if day in existing_hdays:
        print(f"Holiday on {year}-{month}-{day} already exists.")
        return False
    red_day_box = soup.new_tag('span', style='color:red')
    red_day_box.append(str(day))
    box_td = soup.find('td', id=f"box-{year}-{month}-{day}")
    box_td.clear()
    box_td.append(red_day_box)
    h_str = get_holidays_str(cal_el)
    if h_str == "":
        h_str = f"{day} - {reason}"
    else:
        h_str += f", {day} - {reason}"
    soup.find('div', class_='item', id=f"{year}-{month}").find(
        'div', class_='holidays').p.string = h_str
    with open(file_name, 'w') as f:
        f.write(str(soup))
    return True
