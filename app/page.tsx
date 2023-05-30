import { useApiUrl } from "@/hooks/useApiUrl";

export default async function Home() {
  const { apiUrl } = useApiUrl();
  const res = await fetch(apiUrl("python2"));
  const data = await res.json();

  return (
    <main>
      this is main
      {JSON.stringify(data)}
    </main>
  );
}
