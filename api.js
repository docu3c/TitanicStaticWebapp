import axios from 'axios';

function MyComponent() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('https://titanicsurvived.azurewebsites.net/api/HttpExample?code=y2vKOEKLvgkoWFSUWapIiCLf6ToNPZkXni6n-4lZ7iGhAzFuodtSag==')
      .then(response => setData(response.data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      {data && <div>{JSON.stringify(data)}</div>}
    </div>
  );
}