from datetime import datetime

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
    nahuatl_numbers = {
        1: "Ce",
        2: "Ome",
        3: "Yei",
        4: "Nahui",
        5: "Macuili",
        6: "Chicoaze",
        7: "Chicome",
        8: "Chicyei",
        9: "Chicnahui",
        10: "Matlactli",
        11: "Matlactli ihuan Ce",
        12: "Matlactli ihuan Ome",
        13: "Matlactli ihuan Yei"
    }
    
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
    xiuhpohualli_months = [
        ((3, 12), (3, 31), "Atlacahualo", "Lo Dejado por las aguas", "What is left by the water"),
        ((4, 1), (4, 20), "Tlacaxipehualiztli", "El cambio en la Persona", "The Change in the Person"),
        ((4, 21), (5, 10), "Tozoztontli", "La Pequeña velacion", "The Small Vigil"),
        ((5, 11), (5, 30), "Hueytozoztli", "La gran velacion", "The Big Vigil"),
        ((5, 31), (6, 19), "Toxcatl", "Las cosas Secas", "The Dry things"),
        ((6, 20), (7, 9), "Etzacualiztli", "Comer frijol y maiz", "The feast of beans & corn"),
        ((7, 10), (7, 29), "Tecuilhuitontli", "Fiesta de los Señores", "Fiesta of the Great people"),
        ((7, 30), (8, 18), "Huey Tecuilhuitl", "La Gran Fiesta de los Señores", "The Big fiesta of the great people"),
        ((8, 19), (9, 7), "Tlaxochimaco", "Ofrenda de Flores", "Offering of the Flowers"),
        ((9, 8), (9, 27), "Xocotl Huetzi", "La Caída de los Frutos", "The Falling of the Fruit"),
        ((9, 28), (10, 17), "Ochpaniztli", "Barrimiento de los Caminos", "The Sweeping of the Roads"),
        ((10, 18), (11, 6), "Teotleco", "La Llegada de los principios generadores de la Naturaleza", "The Arriving of the principle generators of Nature"),
        ((11, 7), (11, 26), "Tepeilhuitl", "La Fiesta de los Cerros", "The Fiesta of the Mountains"),
        ((11, 27), (12, 16), "Quicholli", "La Veintena del Flamingo", "The 20 day count of the Flamingo"),
        ((12, 17), (1, 5), "Panquetzaliztli", "El Levantamiento de los Estandartes", "The Raising of the Standards"),
        ((1, 6), (1, 25), "Atemoztli", "El Descenso de la Aguas", "The descent of the water"),
        ((1, 26), (2, 14), "Tititl", "Veintena del Recogimiento", "The 20 day count of Absorption"),
        ((2, 15), (3, 6), "Izcalli", "Veintena del Resurgimiento", "The 20 day count of Resurgence"),
        ((3, 7), (3, 11), "Nemontemi", "Tiempo de Reflexión", "5.25 days for Reflection")
    ]

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
