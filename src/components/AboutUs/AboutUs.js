import React from 'react';
import './AboutUs.css';
import sec1 from '../../img/board.svg'
import sec2 from '../../img/disco.svg'
import sec3 from '../../img/line.svg'
import slide1 from '../../img/images.jpg'
import slide2 from '../../img/images2.jpg'
import slide3 from '../../img/images3jpg.jpg'
import slide4 from '../../img/min_small.jpg'

const AboutUs = () => {
  return (
    <div className="about-us">
      <div className="header">
        <h1>Познайомимося?</h1>
      </div>
      <div className="features">
        <div className="feature">
          <img src={sec1} alt="Icon 1" />
          <h3>Безпека даних</h3>
          <p>Ми забезпечуємо безпеку даних наших клієнтів, використовуючи найсучасніші технології та стандарти.</p>
        </div>
        <div className="feature">
          <img src={sec2} alt="Icon 2" />
          <h3>Аналіз даних</h3>
          <p>Ми допомагаємо вам отримувати максимальну користь від даних, зібраних на вашому веб-сайті, використовуючи різні метрики та засоби аналізу.</p>
        </div>
        <div className="feature">
          <img src={sec3} alt="Icon 3" />
          <h3>Зручні інтеграції</h3>
          <p>Ми працюємо з різними платформами та системами, щоб ви могли без перешкод інтегрувати наші рішення з вашим сайтом.</p>
        </div>
        <div className="feature">
          <img src={sec2} alt="Icon 4" />
          <h3>Технічна підтримка</h3>
          <p>Наша команда технічної підтримки завжди готова допомогти вам вирішувати будь-які технічні питання, що виникають.</p>
        </div>
      </div>
      <div className="slogan">
      <h2>Робимо веб-аналітику простішою</h2>
      <p>Ми допомагаємо підприємцям, маркетологам та аналітикам розуміти їх аудиторію, збільшувати продажі та збільшувати прибуток від веб-сайту.</p>
      </div>
      <div className="company-info">
        <h2>Про компанію</h2>
        <p>Інформаційна система нашої аудиторської компанії є цифровим інструментом, що дозволяє нам забезпечувати нашим клієнтам найвищий рівень обслуговування та ефективності.</p>
        <p>Наша інформаційна система розроблена для того, щоб забезпечити точність та достовірність важливої інформації, яка використовується під час проведення аудиту та інших послуг, що ми надаємо. Завдяки цьому ми можемо забезпечити нашим клієнтам надійну інформацію, що дозволить їм приймати обґрунтовані рішення та вести бізнес у відповідності з правовими та регуляторними вимогами.</p>
      </div>
      <div className="slideshow">
        <img className="slide" src={slide1} alt="Slide 1" />
        <img className="slide" src={slide2} alt="Slide 2" />
        <img className="slide" src={slide3} alt="Slide 3" />
        <img className="slide" src={slide4} alt="Slide 4" />
      </div>
    </div>
  );
}

export default AboutUs;