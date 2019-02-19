import {useEffect, useRef, useState} from 'react';
import lineFactory from './lineFactory';

export function useLine(data) {
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

    return [ref, line];
}
