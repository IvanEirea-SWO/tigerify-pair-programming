import React from 'react'

/** 
 * This component is used to produce different types of buttons when needed,
 * just by passing it the adequate props
 * 
 * @param {*} props 
 * @returns 
 */
export default function Button(props) {

    if (props.name === 'submit') {
        return (
            <>
                <button type='submit' className='btn btn-primary'>Submit</button>
            </>
            )
    } else if (props.name === 'button') {
        return (
            <>
                <button type='button' className='btn btn-secondary'>Button</button>
            </>
        )
    } else {
        return (
            null
        )
    }

}
