// Add product to Flask API
async function addProduct(){

    const response = await axios.post(
        "http://localhost:5000/api/products",
        {
            name: "Audi Car",
            price: 8000000
        }
    )

    console.log("Created:", response.data)

}

addProduct()



// Get products from Flask API
async function getProducts(){

    const response = await axios.get(
        "http://localhost:5000/api/products"
    )

    console.log("Products:", response.data)

}

getProducts()



// Get data from external API
async function getExternalData(){

    const response = await axios.get(
        "https://api.sampleapis.com/futurama/info"
    )

    console.log("External API Data:", response.data)

}

getExternalData()



// Send external API data to Flask API
async function sendExternalData(){

    const response = await axios.get(
        "https://api.sampleapis.com/futurama/info"
    )

    await axios.post(
        "http://localhost:5000/api/products",
        response.data
    )

    console.log("External data sent to API")

}

sendExternalData()