import { useEffect, useState } from 'react';

const useGetHookExample = ({ id }) => {
  const [isLoading, setIsLoading] = useState(null);
  const [error, setError] = useState(null);
  const [data, setData] = useState(null);

  useEffect(() => {
    const controller = new AbortController();
    const { signal } = controller;

    setIsLoading(true);
    const fetchData = async () => {
      try {
        const response = await fetch(`https://example.com/api/data/${id}`, { signal });

        if (!response.ok) {
          setError(response.status);
        }
        const responseBody = await response.json();
        setData(responseBody);
      }
      catch (e) {
        if (e.name === 'AbortError') {
          console.error('Request aborted');
        }
        else {
          setError(e);
          console.error('Error', e);
        }
      }
      finally {
        setIsLoading(false);
      }
    };
    fetchData();
    return () => {
      controller.abort('unmounted component');
    };
  }, [id]);

  return { data, error, isLoading };
};

export default useGetHookExample;
