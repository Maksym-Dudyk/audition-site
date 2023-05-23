import React from 'react';
import { Link } from 'react-router-dom';
import '../Navigation/Navigation.css'

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Головна</Link>
        </li>
        <li>
          <Link to="/about">Про нас</Link>
        </li>
        <li>
          <Link to="/services">Послуги</Link>
        </li>
        <li>
          <Link to="/blog">Блог</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;