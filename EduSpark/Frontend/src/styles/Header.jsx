import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/components/Header.css'; // Correct path to your CSS file

function Header() {
  return (
    <header className="header">
      <div className="container">
        <nav className="header-nav">
          <Link to="/" className="header-logo">
            EduSpark
          </Link>
          <div className="header-links">
            <Link to="/dashboard">Dashboard</Link>
            <Link to="/courses">Courses</Link>
            <Link to="/profile">Profile</Link>
            <Link to="/contact">Contact</Link>
          </div>
        </nav>
      </div>
    </header>
  );
}

export default Header;