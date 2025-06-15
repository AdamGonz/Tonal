from datetime import datetime

def convert_to_aztec(date_str):
    # Placeholder logic
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return {
        "gregorian": date_str,
        "tonalpohualli": "8 Tochtli",
        "xiuhpohualli": "Huey Tecuilhuitl",
        "deity": "Xochipilli",
        "info": "Festival of flowers and music"
    }
