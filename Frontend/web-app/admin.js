const selectForm = document.querySelector("#select_form")
const selectFormOrders = document.querySelector("#select_form_orders")

const deleteAlbumBtn = document.querySelector("#del_alb_btn")
const deleteOrderBtn = document.querySelector("#del_ord_btn")
const createAlbumBtn = document.querySelector("#create_alb_btn")

const title_input = document.querySelector("#title_input")
const artist_input = document.querySelector("#artist_input")
const genre_input = document.querySelector("#genre_input")
const runtime_input = document.querySelector("#runtime_input")
const stock_input = document.querySelector("#stock_input")
const cost_input = document.querySelector("#cost_input")

url = "http://a1409f5223925440e9a55fbeea470060-1962762701.eu-west-1.elb.amazonaws.com/api"

const populateSelect = async () => {

    let album_data = await fetch(`${url}/record`)
    let data = await album_data.json()

    let order_data = await fetch(`${url}/order`)
    let data_2 = await order_data.json()

    console.log(data);
    console.log(data_2);

    data.response.forEach((data, index) => {
        new_option = document.createElement("option")
        new_option.value = data.item_id
        new_option.innerText = data.title

        selectForm.appendChild(new_option)
    })

    data_2.response.forEach((data, index) => {
        new_option = document.createElement("option")
        new_option.value = data.order_id
        new_option.innerText = data.order_id

        selectFormOrders.appendChild(new_option)
    })

}

const deleteAlbum = async () => {
    const response = await fetch(`${url}/record/${selectForm.value}`, {
        method: "DELETE",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },

    });

    await console.log(response);
}

const deleteOrder = async () => {
    const response = await fetch(`${url}/order/${selectFormOrders.value}`, {
        method: "DELETE",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },

    });

    await console.log(response);
}

const createAlbum = async () => {

    albumObj = {
        artist: artist_input.value,
        cost: cost_input.value,
        genre: genre_input.value,
        runtime: runtime_input.value,
        title: title_input.value,
        total_stock: stock_input.value
    }

    artist_input.value = ""
    cost_input.value = ""
    genre_input.value = ""
    runtime_input.value = ""
    title_input.value = ""
    stock_input.value = ""

    console.log(albumObj);

    const response = await fetch(`${url}/record`, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(albumObj)
    })

    await console.log(response);
    
}

deleteAlbumBtn.addEventListener("click", deleteAlbum)
deleteOrderBtn.addEventListener("click", deleteOrder)
createAlbumBtn.addEventListener("click", createAlbum)

populateSelect()