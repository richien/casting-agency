const formatDate = (isoDate) => {
    const date = new Date(isoDate)
    return date.toDateString()
}

export default formatDate