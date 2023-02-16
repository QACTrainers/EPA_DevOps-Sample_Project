const orderDiv = document.querySelector("#order_list")
const selectForm = document.querySelector("#select_form")
const orderBtn = document.querySelector("#add_order_btn")
const quantityInput = document.querySelector("#album_quantity")

url = "http://a9e614bff6d4f4f2684a31bd44f1c683-600235163.eu-west-1.elb.amazonaws.com/api"

const getData = async () => {
    let response = await fetch(`${url}/order`);
    let data = await response.json()
    clearRecords()
    populateData(data.response)
};

const clearRecords = () => {
    orderDiv.textContent = ""
}

const populateData = (data) => { 
    data.forEach(async (order, index) => {

        let album_data = await fetch(`${url}/record/${order.item_id}`)
        let data = await album_data.json()

        card = document.createElement("div")
        card_body = document.createElement("div")
        card_title = document.createElement("h5")
        card_subtitle = document.createElement("h6")
        card_text = document.createElement("p")

        card.classList.add("card")
        card_body.classList.add("card-body")
        card_title.classList.add("card-title")
        card_subtitle.classList.add("card-subtitle", "mb-2", "text-muted")
        card_text.classList.add("card-text")

        card_title.innerText = `Order ID:  ${order.order_id}`
        card_subtitle.innerText = await `Album: ${data.title}  Artist: ${data.artist}`
        card_text.innerText = `Quantity: ${order.quantity}    Total Cost:  ${order.total_cost}    Order Placed:  ${order.date_time}`

        orderDiv.appendChild(card)
        card.appendChild(card_body)
        card_body.appendChild(card_title)
        card_body.appendChild(card_subtitle)
        card_body.appendChild(card_text)

    })
}

const populateSelect = async () => {

    let album_data = await fetch(`${url}/record`)
    let data = await album_data.json()

    data.response.forEach((data, index) => {
        new_option = document.createElement("option")
        new_option.value = data.item_id
        new_option.innerText = data.title

        selectForm.appendChild(new_option)
    })

}

const submitOrder = async () => {

    // console.log("Hello!");

    let album_data = await fetch(`${url}/record/${selectForm.value}`)
    let data = await album_data.json()

    total_cost = await data.cost * quantityInput.value

    orderObj = {
        item_id: selectForm.value,
        quantity: quantityInput.value,
        total_cost: total_cost
    }

    const response = await fetch(`${url}/order`, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
        body: JSON.stringify(orderObj)
    });

    await console.log(response);

}

getData()
populateSelect()

orderBtn.addEventListener("click", submitOrder)