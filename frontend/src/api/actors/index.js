import axios from 'axios';
import config from '../../auth_config.json';

const endpoint = config.baseApiUrl;
const token = localStorage.getItem('JWT_TOKEN');

export const getActors = async () => {
    let url = endpoint + '/actors?limit=10';
    let headers = {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    return await axios.get(url, {'headers': headers})
        .then(response => {
            return response.data;
        })
        .catch(error => {
            throw error;
        })
}
