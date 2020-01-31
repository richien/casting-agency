import moxios from 'moxios';
import { getRecentMovies } from './../movies';

describe('movies api', () => {
    beforeEach(() => {
        moxios.install();
    });

    afterEach(() => {
        moxios.uninstall();
    });

    test('getRecentMovies with success response', async () => {
        const data = {
            movies: [{title: 'Test movie 1'}],
            'total-movies': 1,
            success: true
        }
        moxios.wait(() => {
            const request = moxios.requests.mostRecent();
            request.respondWith({
                status: 200,
                response: data
            });
        });
        const result = await getRecentMovies();
        expect(result).toEqual(data);
        
    });

    test('getRecentMovies with failure response', async () => {
        const errorResponse = {
            success: false,
            error: 404,
            message: 'resource not found'
        }
        moxios.wait(() => {
            const request = moxios.requests.mostRecent();
            request.respondWith({
                status: 404,
                response: errorResponse
            });
        });
        const result = await getRecentMovies();
        expect(result.response.data).toEqual(errorResponse);
    });
});