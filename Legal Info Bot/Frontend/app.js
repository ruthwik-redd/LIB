import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [faqs, setFaqs] = useState([]);
  const [legalRights, setLegalRights] = useState([]);
  const [glossary, setGlossary] = useState([]);
  const [income, setIncome] = useState('');
  const [incomeTax, setIncomeTax] = useState(null);
  const [service, setService] = useState('faqs');
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    axios.get('/api/faqs')
      .then(response => setFaqs(response.data))
      .catch(error => console.error('Error fetching FAQs:', error));

    axios.get('/api/legal_rights')
      .then(response => setLegalRights(response.data))
      .catch(error => console.error('Error fetching legal rights:', error));

    axios.get('/api/legal_glossary')
      .then(response => setGlossary(response.data))
      .catch(error => console.error('Error fetching glossary:', error));
  }, []);

  const handleIncomeTaxCalculation = () => {
    axios.post('/api/income_tax', { income: parseFloat(income) })
      .then(response => setIncomeTax(response.data.tax))
      .catch(error => console.error('Error calculating income tax:', error));
  };

  const handleServiceChange = (service) => {
    setService(service);
  };

  const handleDarkModeToggle = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className={`container mx-auto p-4 ${darkMode ? 'bg-gray-900 text-white' : 'bg-white text-gray-900'}`}>
      <div className="flex justify-center mb-4">
        <button
          className={`bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ${service === 'faqs' ? 'bg-blue-700' : ''}`}
          onClick={() => handleServiceChange('faqs')}
        >
          FAQs
        </button>
        <button
          className={`bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ${service === 'legal-rights' ? 'bg-blue-700' : ''}`}
          onClick={() => handleServiceChange('legal-rights')}
        >
          Legal Rights
        </button>
        <button
          className={`bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ${service === 'glossary' ? 'bg-blue-700' : ''}`}
          onClick={() => handleServiceChange('glossary')}
        >
          Glossary
        </button>
        <button
          className={`bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ${service === 'income-tax' ? 'bg-blue-700' : ''}`}
          onClick={() => handleServiceChange('income-tax')}
        >
          Income Tax Calculator
        </button>
        <button
          className={`bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded ${darkMode ? 'bg-gray-700' : ''}`}
          onClick={handleDarkModeToggle}
        >
          Toggle Dark Mode
        </button>
      </div>

      {service === 'faqs' && (
        <div>
          <h2 className="text-lg font-bold mb-2">Frequently Asked Questions</h2>
          <ul>
            {faqs.map((faq, index) => (
              <li key={index} className="mb-4">
                <h3 className="text-lg font-bold">{faq.Question}</h3>
                <p>{faq.Answer}</p>
              </li>
            ))}
          </ul>
        </div>
      )}

      {service === 'legal-rights' && (
        <div>
          <h2 className="text-lg font-bold mb-2">Legal Rights</h2>
          <ul>
            {legalRights.map((right, index) => (
              <li key={index} className="mb-4">
                <h3 className="text-lg font-bold">{right.Right}</h3>
                <p>{right.Description}</p>
              </li>
            ))}
          </ul>
        </div>
      )}

      {service === 'glossary' && (
        <div>
          <h2 className="text-lg font-bold mb-2">Glossary</h2>
          <ul>
            {glossary.map((term, index) => (
              <li key={index} className="mb-4">
                <h3 className="text-lg font-bold">{term.Term}</h3>
                <p>{term.Definition}</p>
              </li>
            ))}
          </ul>
        </div>
      )}

      {service === 'income-tax' && (
        <div>
          <h2 className="text-lg font-bold mb-2">Income Tax Calculator</h2>
          <input
            type="number"
            placeholder="Enter your income"
            value={income}
            onChange={(e) => setIncome(e.target.value)}
            className="mb-2 p-2 border border-gray-300 rounded"
          />
          <button
            onClick={handleIncomeTaxCalculation}
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Calculate Tax
          </button>
          {incomeTax !== null && (
            <p className="mt-2">Your income tax is: {incomeTax}</p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
