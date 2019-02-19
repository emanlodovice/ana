import React from 'react';
import {useLine} from './reactHooks';
import style from './LineChart.scss';

export default function LineChart({data}) {
    const [ref, line] = useLine(data);

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
