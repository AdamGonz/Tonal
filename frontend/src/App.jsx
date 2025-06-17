import { useState } from 'react';

function App() {
  const [date, setDate] = useState('');
  const [aztecInfo, setAztecInfo] = useState(null);

  const fetchAztecDate = async () => {
    try {
      const res = await fetch(`http://localhost:5000/aztec-date?date=${date}`);
      const data = await res.json();
      setAztecInfo(data);
    } catch (err) {
      console.error('Error fetching date:', err);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Aztec Calendar Converter</h1>
      <input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />
      <button onClick={fetchAztecDate}>Convert</button>

      {aztecInfo && (
        <div style={{ marginTop: '1rem' }}>
          <h2>Aztec Date Information</h2>
          <p><strong>Gregorian:</strong> {aztecInfo.gregorian}</p>
          <p><strong>Aztec Year:</strong> {aztecInfo.aztec_year_number} {aztecInfo.aztec_year_symbol}</p>
          <p><strong>Aztec Month:</strong> {aztecInfo.aztec_month}</p>
          <p><strong>Aztec Month English:</strong> {aztecInfo.aztec_month_english}</p>
          <p><strong>Aztec Month Spanish:</strong> {aztecInfo.aztec_month_spanish}</p>
          {/* Add more fields as you implement Tonalpohualli or Xiuhpohualli */}
        </div>
      )}
    </div>
  );
}

export default App;
