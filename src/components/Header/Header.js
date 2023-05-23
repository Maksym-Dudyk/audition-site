import React from 'react';
import logo1 from '../../img/logo.jpg';
import '../Header/Header.css'

function Header() {
  return (
    <header>
      <div className="header-container">
        <nav>
          <ul>
            <li><a href="/">Головна</a></li>
            <li><a href="/about">Про нас</a></li>
            <li><a href="/services">Послуги</a></li>
            <li><a href="/blog">Блог</a></li>
          </ul>
        </nav>
        <div className="logo">
          <a href="/">
            <img src={logo1} alt="Логотип компанії" />
            <h1>Аудиторська компанія</h1>
          </a>
        </div>
      </div>
    </header>
  );
}

export default Header;