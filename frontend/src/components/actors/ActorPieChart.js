import React, { useEffect, useState } from 'react'
import { Pie } from 'react-chartjs-2';
import { getActorTotals } from '../../api/actors';
import Spinner from '../commons/Spinner';
import { doLogout } from '../../utils';

function ActorPieChart() {
    let [assigned, setAssigned] = useState(0);
    let [unassigned, setUnassigned] = useState(0);
    let [loading, setLoading] = useState(false);

    useEffect(() => {
        getData()
    }, [assigned, unassigned]);
    
    const getData = async () => {
        setLoading(true)
        await getActorTotals()
        .then(result => {
            setAssigned(result.data.assigned)
            setUnassigned(result.data.unassigned)
            setLoading(false)
        })
        .catch(error => {
            setLoading(false)
            if (error.response.status === 401){
                doLogout()
            }
            console.log(error.response)
        })
    }
    const labels = ['Assigned', 'Unassigned'];
    const datasets = [{
        data: [assigned, unassigned],
        backgroundColor: ['#52de97', '#ff5151']
    }];
    return (
        <div>
            <header><h6>Actors</h6></header>
            {
                loading ? 
                <div data-test='spinner' className='spinner'><Spinner /></div>
                : <div className='chart-wrapper'>
                        <Pie
                            data={{
                                labels,
                                datasets
                            }}
                            height={200}
                        />
                    </div>
            }
        </div>
    )
}

export default ActorPieChart
