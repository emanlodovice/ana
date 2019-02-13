import React from 'react';
import style from './Card.scss';

export default function Card(props) {
    return (
        <div className={style.card}>
            {props.children}
        </div>
    );
}
