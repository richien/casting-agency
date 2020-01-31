import axios from 'axios';
import config from '../../auth_config.json';

const baseApiUrl = config.baseApiUrl;
const token = localStorage.getItem('JWT_TOKEN');
const headers = {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
}

export const getRecentMovies = async () => (
    await axios.get(
        baseApiUrl + '/movies?limit=10',
        {'headers': headers}
    ).then(response => response.data)
    .catch(error => error)
);