import formatDate from '../formatDate';

test('should return human readable date from an iso date string', () => {
    const expectedDate = 'Mon Jan 20 2020';
    const isoDate = '2020-01-20T18:42:00';

    const formatedDate = formatDate(isoDate);

    expect(formatedDate).toEqual(expectedDate)
})