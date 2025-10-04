// File: pages/HomePage.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div>
      <section className="hero">
        <h1>Welcome to Our Education System</h1>
        <p>Explore a variety of courses and start your learning journey today.</p>
        <Link to="/courses">Browse Courses</Link>
      </section>

      <section className="features">
        <h2>Why Choose Us?</h2>
        <ul>
          <li>Expert Instructors</li>
          <li>Flexible Learning</li>
          <li>Accredited Courses</li>
        </ul>
      </section>
    </div>
  );
};

export default HomePage;