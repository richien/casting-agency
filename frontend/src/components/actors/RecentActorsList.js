import React, {useState, useEffect} from 'react'
import Actor from './Actor'
import { connect } from 'react-redux'
import {fetchActors} from '../../redux/actor'
import Spinner from '../commons/Spinner'
import formatDate from '../../utils/formatDate'
import PropTypes from 'prop-types';

function RecentActorsList({fetchActors, actors, loading}) {
    let [redirect, setRedirect] = useState(false)
    const handleSetRedirect = () => {
        setRedirect(true)
    }
    useEffect(() => {
            fetchActors()
        }, [])
    
    return (
        <div>
            <header><h6>Recently Added Actors</h6></header>
            {
                loading ? 
                <div data-test='spinner' className='spinner'><Spinner /></div> : 
            actors.map((actor, index, actors) => (
            <div data-test='list-wrapper' className='list-wrapper' key={actor.id} onClick={() => handleSetRedirect()}>
                <p>{index + 1}</p>
                <span>
                    <Actor actor={actor} key={actor.id} redirect={redirect}/>
                    <div className='joined-date-wrapper'><i>Joined {formatDate(actors[index]['created-at'])}</i></div>
                </span>
            </div>))
            }
        </div>
    )
}

const mapStateToProps = (state) => ({
    actors: state.actors.data,
    loading: state.actors.loading   
})

const mapDispatchToProps = (dispatch) => {
    return {
        fetchActors: () => dispatch(fetchActors())
    }
}

RecentActorsList.propTypes = {
    fetchActors: PropTypes.func,
    actors: PropTypes.array,
    loading: PropTypes.bool
}

export default connect(
        mapStateToProps,
        mapDispatchToProps
    )(RecentActorsList)
