import React, { useEffect, useState } from 'react';
import './OurServices.css';
import { getReviews, getServices, getTariffs } from '../../api-requests/api';

// const services = [
//   {
//     id: 1,
//     title: 'Аудиторські послуги',
//     description:
//       'Надаємо повний спектр аудиторських послуг, що допоможуть Вашому бізнесу розвиватися та ефективно працювати.',
//   },
//   {
//     id: 2,
//     title: 'Податкові консультації',
//     description:
//       'Допоможемо Вам з питань оподаткування та податкового планування, a також допоможемо вирішити податкові спори.',
//   },
//   {
//     id: 3,
//     title: 'Консультації з управління',
//     description:
//       'Надаємо консультації з управління бізнесом, зокрема з питань стратегічного планування, бізнес-аналізу та оптимізації бізнес-процесів.',
//   },
// ];

// const tariffs = [
//   {
//     id: 1,
//     name: 'Базовий',
//     description: 'Пакет для початківців',
//     price: 500,
//   },
//   {
//     id: 2,
//     name: 'Стандартний',
//     description: 'Пакет для невеликих компаній',
//     price: 1000,
//   },
//   {
//     id: 3,
//     name: 'Преміум',
//     description: 'Пакет для великих компаній',
//     price: 2000,
//   },
// ];

// const reviews = [
//   {
//     id: 1,
//     image: 'avatar',
//     name: 'Іван Іванов',
//     text: 'Дуже задоволений послугами компанії. Вони надали мені дуже корисні поради та рекомендації, які допомогли моєму бізнесу рости.',
//   },
//   {
//     id: 2,
//     image: 'avatar',
//     name: 'Марія Петренко',
//     text: 'Професіоналізм, який проявляють працівники цієї компанії, дійсно вражає. Вони завжди готові допомогти та відповісти на всі запитання.',
//   },
//   {
//     id: 3,
//     image: 'avatar',
//     name: 'Петро Сидоренко',
//     text: 'Дякую за чудову роботу! Якість послуг на висоті, а співпраця з компанією - це справжнє задоволення.',
//   },
// ];

const OurServices = () => {
  const [reviews, changeReviews] = useState([]);
  const [tariffs, changeTariffs] = useState([]);
  const [services, changeServices] = useState([]);

  useEffect(() => {
    const updateReviews = async () => {
      const reviewsFromAPI = await getReviews();
      changeReviews(reviewsFromAPI.data);
    }
    const updateServices = async () => {
      const servicesFromAPI = await getServices();
      changeServices(servicesFromAPI.data);
    }
    const updateTariffs = async () => {
      const tariffsFromAPI = await getTariffs();
      changeTariffs(tariffsFromAPI.data);
    }
    updateReviews();
    updateServices();
    updateTariffs();
  }, [])
  return (
    <div className="our-services">
      <h2>Наші послуги</h2>
      <ul>
        {services.map((service) => (
          <li key={service.id}>
            <h3>{service.title}</h3>
            <p>{service.description}</p>
          </li>
        ))}
      </ul>
      <h2>Тарифи</h2>
      <div className="tariffs">
        {tariffs.map((tariff) => (
          <div key={tariff.id} className="tariff">
            <h3>{tariff.name}</h3>
            <p>{tariff.description}</p>
            <p>{tariff.price} грн/міс</p>
          </div>
        ))}
      </div>
      <h2>Відгуки</h2>
      <ul>
        {reviews.map((review) => (
          <li key={review.id}>
            <h3>{review.name}</h3>
            <p>{review.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default OurServices;
