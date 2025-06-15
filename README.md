# Aztec Date Converter

A cultural computing tool for converting Gregorian dates into Aztec calendar dates using both the **Tonalpohualli** (260-day ritual calendar) and **Xiuhpohualli** (365-day solar calendar) systems.

This tool is developed with respect for Indigenous knowledge systems and with the intention to educate, preserve, and share cultural memory through modern tools.

## Description

This project explores the logic behind the Aztec calendrical systems by developing a Python-based backend that can transform standard Gregorian dates into traditional Aztec date representations. The system includes:

- **Tonalpohualli**: a sacred 260-day cycle made of 20 day signs combined with 13 sacred numbers
- **Xiuhpohualli**: a 365-day solar calendar composed of 18 20-day "veintenas" + 5 nemontemi (rest/reflection) days
- **Aztec Year Bearers**: based on a repeating 52-year cycle using 4 year symbols and numbers 1–13
- **Nahuatl Naming**: traditional number names from 1–13 in Nahuatl are included to support authentic date rendering

The project currently runs locally using Flask and will eventually be connected to a React frontend. It is designed for personal use, cultural education, and future integration into Aztec-focused digital experiences.

## Getting Started

### Dependencies

- **Operating System**: Windows 10, macOS, or Linux (Python 3.8+ recommended)
- **Python Libraries**:
  - `Flask` – lightweight web framework for serving API endpoints
  - `datetime` – for parsing and handling Gregorian dates

### Setup

1. Clone the repo:
   ```sh
   git clone https://github.com/<your-username>/aztec-date-converter.git
   ```

2. Navigate into the backend directory:

   ```sh
   cd aztec-date-converter/backend
   ```

3. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # OR
   source venv/bin/activate  # macOS/Linux
   ```

4. Install required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

5. Run the Flask app locally:

   ```sh
   python app.py
   ```

6. Test the API:
   Open your browser or use Postman to test:

   ```
   http://localhost:5000/aztec-date?date=2025-06-14
   ```


## Authors

Adam Axtopani Gonzales – [adamurlnum2@gmail.com](mailto:adamurlnum2@gmail.com)

## Version History

* 0.0 – Building

## Acknowledgments

### Cultural & Academic Sources

* [tlahuilcalli.com](https://tlahuilcalli.com/que-es-el-tonalamatl/)

