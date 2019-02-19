import React, {useEffect, useRef} from 'react';
import * as d3 from 'd3';
import style from './LineChart.scss';

function drawLineChart(svg, data, rect) {
    // Create a line generator whose max and min values are scaled within the
    // size of the component.
    const xMax = Math.max(...data.map(d => d.length)) - 1;
    const yMax = Math.max(...data.map(d => Math.max(...d)));
    const yMin = Math.min(...data.map(d => Math.min(...d)));
    const xScale = d3.scaleLinear().domain([0, xMax]).range([0, rect.width]);
    const yScale = d3.scaleLinear().domain([yMin, yMax]).range([0, rect.height]);
    const line = d3.line().x((d, i) => xScale(i)).y(d => yScale(d));

    // Remove previously added lines. This seems to be necessary in order to
    // handle changing data props.
    d3.select(svg).selectAll('path').remove();

    // Draw lines for each data item.
    d3.select(svg)
        .selectAll('path')
        .data(data)
        .enter()
        .append('path')
        .attr('stroke', 'red')
        .attr('stroke-width', 1)
        .attr('d', line);
}

export default function LineChart({data}) {
    const ref = useRef();

    useEffect(() => {
        const element = ref.current;
        const svg = element.querySelector('svg');
        const updateLineChart = rect => drawLineChart(svg, data, rect);

        updateLineChart(element.getBoundingClientRect());

        const observer = new ResizeObserver(
            ([entry]) => updateLineChart(entry.contentRect)
        );
        observer.observe(element);

        return () => observer.unobserve(element);
    }, data);

    return (
        <div ref={ref} className={style.lineChart}>
            <svg></svg>
        </div>
    );
}
