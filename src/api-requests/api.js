import axios from 'axios';

async function getReviews() {
    return await axios.get('http://localhost:5000/feedback');
};

async function getTariffs() {
    return await axios.get('http://localhost:5000/tariff');
};

async function getServices() {
    console.log( axios)
    return await axios.get('http://localhost:5000/service');
};

async function getArticles() {
    console.log( axios)
    return await axios.get('http://localhost:5000/post');
};

export { getReviews, getServices, getTariffs, getArticles };