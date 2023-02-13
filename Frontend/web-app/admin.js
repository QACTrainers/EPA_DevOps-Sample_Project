const selectForm = document.querySelector("#select_form")
const deleletAlbum = document.querySelector("#del_alb_btn")

url = "http://a1409f5223925440e9a55fbeea470060-1962762701.eu-west-1.elb.amazonaws.com/api"

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

const deleteAlbum = async () => {
    const response = await fetch(`${url}/record`, {
        method: "DELETE",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },

    });

    await console.log(response);
}

deleteAlbum.addEventListener("click", deleletAlbum)