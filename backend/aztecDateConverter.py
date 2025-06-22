from datetime import datetime
from calendar_data import nahuatl_numbers, xiuhpohualli_months


def convert_to_aztec(date_str):
    """
    Convert a Gregorian date (YYYY-MM-DD) into basic Aztec calendar data.

    Inputs:
        date_str (str): A date string in format 'YYYY-MM-DD'
    
    Outputs:
        dict: Aztec calendar data including the year number and year symbol
    """
    date = datetime.strptime(date_str, "%Y-%m-%d")
    year_number, year_symbol = get_aztec_year_sign(date.year)
    month = get_xiuhpohualli_month(date_str)
    
    return {
        "gregorian": date_str,
        "aztec_year_number": year_number,
        "aztec_year_symbol": year_symbol,
        "aztec_month": month["month_name"],
        "aztec_month_spanish": month["spanish_translation"],
        "aztec_month_english": month["english_translation"]
    }


def get_aztec_year_sign(year):
    """
    Get the Aztec year number (1–13) and year symbol (Tochtli, Acatl, Tecpatl, Calli)
    based on the 52-year cycle starting from the year 2000.

    Inputs:
        year (int): Gregorian year
    
    Outputs:
        tuple: (aztec_number (int), aztec_symbol (str))
    """
    year_symbols = ["Tecpatl", "Calli", "Tochtli", "Acatl"]
    offset = year - 2000

    number = (offset % 13) + 1
    symbol = year_symbols[offset % 4]

    return number, symbol

def get_nahuatl_number_name(number):
    """
    Get the Nahuatl word for a sacred number from 1 to 13 
    used in the Tonalpohualli calendar.

    Inputs:
        number (int): A number from 1 to 13

    Outputs:
        str: The corresponding Nahuatl name (e.g., 'Ce', 'Ome', etc.)
    """

    return nahuatl_numbers.get(number, "Unknown")

def get_xiuhpohualli_month(date_obj):
    """
    Get the Xiuhpohualli (solar calendar) month name for a given Gregorian date.

    Inputs:
        date_obj (datetime.date): A Gregorian date
    
    Outputs:
        dict: {
            'month_name': str,
            'spanish_translation': str,
            'english_translation': str
        }
    """

    date_obj = datetime.strptime(date_obj, "%Y-%m-%d").date()

    for (start_month, start_day), (end_month, end_day), name, es, en in xiuhpohualli_months:
        # Handle the one month (Dec 17 – Jan 5) that wraps over year-end
        if start_month > end_month:
            if (date_obj.month == start_month and date_obj.day >= start_day) or \
               (date_obj.month == end_month and date_obj.day <= end_day):
                return {"month_name": name, "spanish_translation": es, "english_translation": en}
        elif (start_month, start_day) <= (date_obj.month, date_obj.day) <= (end_month, end_day):
            return {"month_name": name, "spanish_translation": es, "english_translation": en}
    
    return {"month_name": "Unknown", "spanish_translation": "", "english_translation": ""}


# Quick test for development
if __name__ == "__main__":
    test_dates = [
        "2000-06-01",
        "2012-06-20",
        "2025-11-01",
        "1986-04-14",
        "1985-09-03"
    ]

    for date_str in test_dates:
        result = get_xiuhpohualli_month(date_str)
        print(f"{date_str} → {result['month_name']} ({result['english_translation']})")
