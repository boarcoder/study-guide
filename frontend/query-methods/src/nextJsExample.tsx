
async function NextComponent({ id }) {
    /*
        Like tanstack query, next will automatically cache the fetch request.
        Next will also cache certain renders automatically
        Note, there is no `useEffect` here.
    */
    const response = await fetch(
        `https://example.com/api/data/${id}`
    );
    const data = await response.json();

    return (
        <pre className= "details" >
            {JSON.stringify(data)}
        </pre>
    )
}