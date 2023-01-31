import React from 'react'

export default function Table(props) {
    
        if (props.name === 'songs') {
            return (
                <>
                    <h3>Songs</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Seconds</th>
                                <th>Album</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr key={song.id}>
                                <td>{song.id}</td>
                                <td>{user.name}</td>
                                <td>{user.seconds}</td>
                                <td>{user.album}</td>
                            </tr>
                        </tbody>
                    </table>
                </>
            )
        } else {
            return (
                null
            )
        }

}
