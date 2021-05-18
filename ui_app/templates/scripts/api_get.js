async function getContent(){
    try {
        const response = await fetch('http://localhost:8000/lettucenutrients/')
        // const response = await fetch('http://localhost:8021/')
        // console.log(response)
        const datas = await response.json()

        console.log(datas)
        show(datas)


    } catch (error) {
        console.error(error)
    }
}

getContent()

function show (datas){
    let output = ``
    for (let data of datas){
        output += `<li>${data.id} - ${data.created_at}</li>`
    }
    console.log(output)
    document.querySelector('main').innerHTML = output
}