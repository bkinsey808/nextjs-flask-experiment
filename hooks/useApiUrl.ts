import { headers } from "next/headers";

export const useApiUrl = () => {
  const apiUrl = (url: string) => {
    const headersData = headers();
    const protocol = headersData.get("x-forwarded-proto");
    const host = headersData.get("host");
    return `${protocol}://${host}/api/${url}`;
  };
  return { apiUrl };
};
