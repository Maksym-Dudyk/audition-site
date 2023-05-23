import React from 'react';
import '../Footer/Footer.css';

function Footer() {
  return (
    <footer>
      <div className="footer-container">
        <div className="footer-content">
          <div className="footer-section contact">
            <h3>Контакти</h3>
            <ul>
              <li><i className="fa fa-map-marker"></i>Адреса: м. Київ, вул. Хрещатик, 10</li>
              <li><i className="fa fa-phone"></i>Телефон: +380123456789</li>
              <li><i className="fa fa-envelope"></i>Email: info@auditorsys.com</li>
            </ul>
          </div>
          <div className="footer-section social">
            <h3>Ми в соціальних мережах</h3>
            <ul>
              <li><a href="#"><i className="fa fa-facebook"></i></a></li>
              <li><a href="#"><i className="fa fa-twitter"></i></a></li>
              <li><a href="#"><i className="fa fa-instagram"></i></a></li>
            </ul>
          </div>
        </div>
      </div>
      <div className="footer-bottom">
        <p>© 2023 Аудиторська компанія "AuditorSys". Усі права захищені.</p>
      </div>
    </footer>
  );
}

export default Footer;