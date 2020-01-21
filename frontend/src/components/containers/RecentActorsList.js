import React, {useState, useEffect} from 'react'
import Actor from '../Actor'
import { connect } from 'react-redux'
import {fetchActors} from '../../redux'
import Spinner from '../commons/Spinner'
import formatDate from '../../utils/formatDate'

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
                <div className='spinner'><Spinner /></div> : 
            actors.map((actor, index, actors) => (
            <div className='list-wrapper' key={actor.id} onClick={() => handleSetRedirect()}>
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
    actors: state.actor.actors,
    loading: state.actor.loading   
})

const mapDispatchToProps = (dispatch) => {
    return {
        fetchActors: () => dispatch(fetchActors())
    }
}

export default connect(
        mapStateToProps,
        mapDispatchToProps
    )(RecentActorsList)
