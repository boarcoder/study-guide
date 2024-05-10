import { useQuery } from '@tanstack/react-query';

/*
React query will automatically cache based on queryKey!

*/
function useGetItem({ id }) {
  const { data, isLoading } = useQuery({
    queryKey: [id],
    queryFn: async () => {
      const response = await fetch(
        `https://example.com/api/data/${id}`,
      );
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const responseBody = response.json();
      return responseBody;
    },
    staleTime: 1000 * 60 * 10, // re-fetch after 10 minutes
  });
}
