import React, {useEffect, useRef, useState} from 'react';
import * as d3 from 'd3';
import style from './LineChart.scss';

function lineGeneratorFactory({data, width=0, height=0}) {
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

export default function LineChart({data}) {
    const ref = useRef();

    const [lineGenerator, setLineGenerator] = useState(
        () => lineGeneratorFactory({data})
    );

    const updateLineGenerator = rect => setLineGenerator(
        () => lineGeneratorFactory({data, ...rect})
    );

    useEffect(() => {
        const element = ref.current;

        // Sets line generator based on initial component dimensions
        updateLineGenerator(element.getBoundingClientRect().toJSON());

        // Update line generator as the component is resized
        const observer = new ResizeObserver(
            ([entry]) => updateLineGenerator(entry.contentRect.toJSON())
        );
        observer.observe(ref.current);

        return () => observer.unobserve(ref.current);
    }, data);

    return (
        <div ref={ref} className={style.lineChart}>
            <svg>
                {data.map(d => (
                    <path
                        key={d.label}
                        stroke="red"
                        strokeWidth="1"
                        d={lineGenerator(d.data)}
                    />
                ))}
            </svg>
        </div>
    );
}
