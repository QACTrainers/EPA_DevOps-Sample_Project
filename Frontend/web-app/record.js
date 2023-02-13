const recordDiv = document.querySelector("#record_list")
const searchBtn = document.querySelector("#search_btn")
const showAllBtn = document.querySelector("#show_all")
const searchBar = document.querySelector("#search_text")

url = "a1409f5223925440e9a55fbeea470060-1962762701.eu-west-1.elb.amazonaws.com/api"

const getData = async () => {
    let response = await fetch(`${url}/record`);
    let data = await response.json()
    clearRecords()
    populateData(data.response)
};

const searchData = async () => {

    search = searchBar.value
    searchBar.value = ""

    let response = await fetch(`${url}/record/query?search=${search}`);
    let data = await response.json()
    clearRecords()
    populateData(data.response)

}

const clearRecords = () => {
    recordDiv.textContent = ""
}

const populateData = (data) => {

    data.forEach((record, index) => {

        card_body = document.createElement("div")
        card_img = document.createElement("img")
        card_sub_body = document.createElement("div")
        card_title = document.createElement("h3")
        card_subtitle = document.createElement("h5")
        card_text = document.createElement("p")
        card_add_basket = document.createElement("a")
        card_more_info = document.createElement("a")

        card_body.classList.add("card", "m-3")
        card_img.classList.add("card-img-top")
        card_sub_body.classList.add("card-body")
        card_title.classList.add("card-title")
        card_subtitle.classList.add("card-subtitle")
        card_text.classList.add("card-text")

        card_body.style = "width: 18rem"
    
        card_img.src = `https://picsum.photos/300/?random=${index + 1}`
        card_title.innerText = record.title
        card_subtitle.innerText = record.artist
        card_text.innerText = record.cost

        card_more_info.href = ``

        recordDiv.appendChild(card_body)
        card_body.appendChild(card_img)
        card_body.appendChild(card_sub_body)
        card_sub_body.appendChild(card_title)
        card_sub_body.appendChild(card_subtitle)
        card_sub_body.appendChild(card_text)

    })
}

searchBtn.addEventListener("click", searchData)
showAllBtn.addEventListener("click", getData)

// getData().then((data) => {

//     record_data = data.response
//     console.log(record_data);

//     populateData(record_data)

// });

getData()