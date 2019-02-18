import React, {useEffect, useRef} from 'react';
import * as d3 from 'd3';
import style from './LineChart.scss';

export default function LineChart({data}) {
    const ref = useRef();

    const draw = ({width, height}) => {
        const x = d3.scaleLinear()
            .domain([0, Math.max(...data.map(d => d.data.length)) - 1])
            .range([0, width]);
        const y = d3.scaleLinear()
            .domain([
                Math.min(...data.map(d => Math.min(...d.data))),
                Math.max(...data.map(d => Math.max(...d.data)))
            ])
            .range([0, height]);

        const lineGenerator = d3.line()
            .x((d, i) => x(i))
            .y(d => y(d));

        d3.select(ref.current)
            .selectAll('path')
            .remove();

        d3.select(ref.current)
            .select('svg')
            .selectAll('path')
            .data(data)
            .enter()
            .append('path')
            .attr('stroke', 'red')
            .attr('stroke-width', 1)
            .attr('d', d => lineGenerator(d.data));
    };

    useEffect(() => {
        draw(ref.current.getBoundingClientRect());

        const observer = new ResizeObserver(([entry]) => draw(entry.contentRect));
        observer.observe(ref.current);

        return () => observer.unobserve(ref.current);
    }, data);

    return (
        <div ref={ref} className={style.lineChart}>
            <svg></svg>
        </div>
    );
}
