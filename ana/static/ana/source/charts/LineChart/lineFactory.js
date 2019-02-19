import * as d3 from 'd3';

export default function lineFactory({data, width=0, height=0}) {
    const x = d3.scaleLinear()
        .domain([0, Math.max(...data.map(d => d.data.length)) - 1])
        .range([0, width]);
    const y = d3.scaleLinear()
        .domain([
            Math.min(...data.map(d => Math.min(...d.data))),
            Math.max(...data.map(d => Math.max(...d.data)))
        ])
        .range([0, height]);

    return d3.line().x((d, i) => x(i)).y(d => y(d));
}
