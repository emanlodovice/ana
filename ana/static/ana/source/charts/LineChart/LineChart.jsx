import React, {useEffect} from 'react';
import * as d3 from 'd3';
import style from './LineChart.scss';

export default function LineChart({data}) {
    const ref = React.createRef();

    useEffect(() => {
        const values = data[0].data;
        const x = d3.scaleLinear()
            .domain([0, values.length - 1])
            .range([0, 700]);
        const y = d3.scaleLinear()
            .domain([0, d3.max(values)])
            .range([0, 200]);
        const lineGenerator = d3.line()
            .x((d, i) => x(i))
            .y(d => y(d));

        d3.select('path')
            .attr('d', lineGenerator(values));
    }, []);

    return (
        <svg
            ref={ref}
            className={style.lineChart}
            viewBox="0 0 700 200"
        >
            <path fill="none" stroke="red" />
        </svg>
    );
}
