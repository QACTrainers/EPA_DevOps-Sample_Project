const getData = async () => {
    let response = await fetch(`http://localhost:5000/record`);
    let data = await response.json()
    return data;
};

getData().then((data) => {
    console.log(data)
    console.log(data.response[1]);
});