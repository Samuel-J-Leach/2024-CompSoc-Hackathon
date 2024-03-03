import React from 'react';
import Head from 'next/head';

function Layout({ children }) {
  return (
    <div>
      <header className="header">
          <nav className="navbar">
            <a className="navbar-box" href="/">
              <h2 className="navbar-link">Home</h2>
            </a>
            <a className="navbar-box" href="/aboutPage">
              <h2 className="navbar-link">About</h2>
            </a>
          </nav>
        </header>
      <main>
        {children}
      </main>

      <footer className="footer">
        <h2 className="footer-text">2024 Team HLS | Surrey CompSoc Hackathon</h2>
      </footer>
    </div>
  );
}

export default Layout;