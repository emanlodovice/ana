import React, {useEffect, useRef, useState} from 'react';
import lineFactory from './lineFactory';
import style from './LineChart.scss';

export default function LineChart({data}) {
    const ref = useRef();
    const [line, setLine] = useState(() => lineFactory({data}));

    const updateLine = rect => setLine(
        () => lineFactory({data, ...rect})
    );

    useEffect(() => {
        const element = ref.current;

        // Sets line generator based on initial component dimensions
        updateLine(element.getBoundingClientRect().toJSON());

        // Update line generator as the component is resized
        const observer = new ResizeObserver(
            ([entry]) => updateLine(entry.contentRect.toJSON())
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
                        d={line(d.data)}
                    />
                ))}
            </svg>
        </div>
    );
}
