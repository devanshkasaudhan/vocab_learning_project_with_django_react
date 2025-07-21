import React, { useEffect, useState } from 'react';
import axios from 'axios';

function WordOfTheDay() {
  const [word, setWord] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWord = async () => {
      try {
        setLoading(true);
        setError(null);
        
        // Check if we're in development or production
        const isDevelopment = process.env.NODE_ENV === 'development';
        const apiUrl = isDevelopment 
          ? 'http://localhost:8000/api/word-of-the-day/'
          : `${process.env.PUBLIC_URL || ''}/api/word-of-the-day.json`;
        
        const response = await axios.get(apiUrl);
        setWord(response.data);
      } catch (err) {
        console.error('Error fetching word:', err);
        setError('Failed to load word of the day');
        
        // Fallback word for demo purposes
        setWord({
          word: "Serendipity",
          definition: "The occurrence and development of events by chance in a happy or beneficial way",
          example: "A fortunate stroke of serendipity led her to discover the hidden talent.",
          level: "Advanced"
        });
      } finally {
        setLoading(false);
      }
    };

    fetchWord();
  }, []);

  if (loading) return (
    <div style={{ padding: '1rem', border: '1px solid #ccc', margin: '1rem', textAlign: 'center' }}>
      <p>Loading word of the day...</p>
    </div>
  );

  if (error) return (
    <div style={{ padding: '1rem', border: '1px solid #ff6b6b', margin: '1rem', backgroundColor: '#ffe6e6' }}>
      <p style={{ color: '#d63031' }}>{error}</p>
    </div>
  );

  if (!word) return (
    <div style={{ padding: '1rem', border: '1px solid #ccc', margin: '1rem' }}>
      <p>No word available</p>
    </div>
  );

  return (
    <div style={{ 
      padding: '2rem', 
      border: '2px solid #74b9ff', 
      margin: '1rem', 
      borderRadius: '12px',
      backgroundColor: '#f8f9fa',
      boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
    }}>
      <h2 style={{ 
        color: '#2d3436', 
        marginBottom: '1rem',
        fontSize: '2rem',
        textAlign: 'center'
      }}>
        📚 {word.word}
      </h2>
      
      <div style={{ marginBottom: '1rem' }}>
        <span style={{
          backgroundColor: word.level === 'Beginner' ? '#00b894' : 
                         word.level === 'Intermediate' ? '#fdcb6e' : '#e17055',
          color: 'white',
          padding: '0.3rem 0.8rem',
          borderRadius: '20px',
          fontSize: '0.8rem',
          fontWeight: 'bold'
        }}>
          {word.level}
        </span>
      </div>
      
      <p style={{ 
        fontSize: '1.1rem', 
        lineHeight: '1.6',
        marginBottom: '1rem'
      }}>
        <strong>Definition:</strong> {word.definition}
      </p>
      
      {word.example && (
        <p style={{ 
          fontSize: '1rem', 
          fontStyle: 'italic',
          color: '#636e72',
          lineHeight: '1.5',
          backgroundColor: '#e8f4f8',
          padding: '1rem',
          borderRadius: '8px',
          borderLeft: '4px solid #74b9ff'
        }}>
          <strong>Example:</strong> {word.example}
        </p>
      )}
      
      <div style={{ textAlign: 'center', marginTop: '1.5rem' }}>
        <button 
          onClick={() => window.location.reload()}
          style={{
            backgroundColor: '#74b9ff',
            color: 'white',
            border: 'none',
            padding: '0.8rem 1.5rem',
            borderRadius: '25px',
            cursor: 'pointer',
            fontSize: '1rem',
            fontWeight: 'bold',
            transition: 'all 0.3s ease'
          }}
          onMouseOver={(e) => e.target.style.backgroundColor = '#0984e3'}
          onMouseOut={(e) => e.target.style.backgroundColor = '#74b9ff'}
        >
          🔄 Get New Word
        </button>
      </div>
    </div>
  );
}

export default WordOfTheDay;
