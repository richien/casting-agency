import React from 'react'
import { Pie } from 'react-chartjs-2';


const labels = ['Assigned', 'Un-assigned'];
const datasets = [{
    data: [30, 20],
    backgroundColor: ['#52de97', '#ff5151']
}];

function ActorPieChart() {
    return (
        <div>
            <header><h6>Actors</h6></header>
            <div className='chart-wrapper'>
                <Pie
                    data={{
                        labels,
                        datasets
                    }}
                    height={200}
                />
            </div>
        </div>
    )
}

export default ActorPieChart
