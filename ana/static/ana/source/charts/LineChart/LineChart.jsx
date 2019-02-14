import React, {useEffect} from 'react';
import * as d3 from 'd3';
import style from './LineChart.scss';

export default function LineChart({data}) {
    const ref = React.createRef();

    useEffect(() => {
        const x = d3.scaleLinear()
            .domain([0, Math.max(...data.map(d => d.data.length)) - 1])
            .range([0, 700]);
        const y = d3.scaleLinear()
            .domain([0, Math.max(...data.map(d => Math.max(...d.data)))])
            .range([0, 200]);

        const lineGenerator = d3.line()
            .x((d, i) => x(i))
            .y(d => y(d));

        d3.select(ref.current)
            .selectAll('path')
            .data(data)
            .enter()
            .append('path')
            .attr('stroke', 'red')
            .attr('stroke-width', 3)
            .attr('d', d => lineGenerator(d.data));
    }, []);

    return (
        <svg
            ref={ref}
            className={style.lineChart}
            viewBox="0 0 700 200"
        >
        </svg>
    );
}
