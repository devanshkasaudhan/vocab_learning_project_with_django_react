import React from 'react';
import WordOfTheDay from './components/WordOfTheDay';

function App() {
  return (
    <div style={{ 
      fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif", 
      maxWidth: '800px', 
      margin: 'auto',
      padding: '2rem',
      backgroundColor: '#f5f6fa',
      minHeight: '100vh'
    }}>
      <header style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1 style={{ 
          color: '#2c3e50',
          fontSize: '3rem',
          marginBottom: '0.5rem',
          textShadow: '2px 2px 4px rgba(0,0,0,0.1)'
        }}>
          📚 Vocabulary Improver
        </h1>
        <p style={{ 
          color: '#7f8c8d',
          fontSize: '1.2rem',
          margin: '0'
        }}>
          Expand your vocabulary one word at a time
        </p>
      </header>
      
      <main>
        <WordOfTheDay />
      </main>
      
      <footer style={{ 
        textAlign: 'center', 
        marginTop: '3rem',
        padding: '2rem',
        borderTop: '2px solid #ddd',
        color: '#7f8c8d'
      }}>
        <p>
          Built with ❤️ using Django & React | 
          <a 
            href="https://github.com/devanshkasaudhan/vocab_learning_project_with_django_react" 
            target="_blank" 
            rel="noopener noreferrer"
            style={{ 
              color: '#74b9ff', 
              textDecoration: 'none',
              marginLeft: '0.5rem'
            }}
          >
            View on GitHub
          </a>
        </p>
      </footer>
    </div>
  );
}

export default App;
