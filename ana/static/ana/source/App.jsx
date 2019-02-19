import React, {useState} from 'react';
import Card from './components/Card/Card.jsx';
import LineChart from './charts/LineChart/LineChart.jsx';
import './stylesheets/global.scss';

function generateArrayWithSize(n) {
    return new Array(n).fill(null);
}

function generateDummyData() {
    return generateArrayWithSize(3).map(
        () => generateArrayWithSize(5).map(
            () => Math.round((Math.random() * 200) - 100)
        )
    );
}

export default function App() {
    const [data] = useState(generateDummyData());

    return (
        <Card>
            <LineChart data={data} />
        </Card>
    );
}
