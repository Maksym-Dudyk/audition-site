import React, { useEffect, useState } from 'react';
import '../Blog/Blog.css'
import { getArticles } from '../../api-requests/api';


const Blog = () => {
  const [articles, changeArticles] = useState([]);

  useEffect(() => {
    const updateArticles = async () => {
      const articlesFromAPI = await getArticles();
      changeArticles(articlesFromAPI.data);
    }
    updateArticles();
  }, [])
  return (
    <div className='box-padding'>
      <h1>Блог</h1>

      <section className="articles">
        {articles.map(({ text, img_link }, index) => (
          <a href="/" key={index}>
            <img src={img_link} alt={text} />
            <h2>{text}</h2>
          </a>
        ))}
      </section>

      <div className="sidebar">
        <h2>Популярні статті</h2>
        <ul>
          <li><a href="#">Lorem ipsum dolor sit amet</a></li>
          <li><a href="#">Consectetur adipiscing elit</a></li>
          <li><a href="#">Sed do eiusmod tempor incididunt</a></li>
        </ul>

        <h2>Популярні теги</h2>
        <ul>
          <li><a href="#">Audit</a></li>
          <li><a href="#">Tax</a></li>
          <li><a href="#">Consulting</a></li>
        </ul>

        <h2>Останні коментарі</h2>
        <ul>
          <li>John Doe on Lorem ipsum dolor sit amet</li>
          <li>Jane Smith on Consectetur adipiscing elit</li>
          <li>Bob Johnson on Sed do eiusmod tempor incididunt</li>
        </ul>
      </div>
    </div>
  )
};

export default Blog;