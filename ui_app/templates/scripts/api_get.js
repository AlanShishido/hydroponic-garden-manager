async function getContent(){
    try {
        const response = await fetch('http://localhost:8000/lettucenutrients/')
        // const response = await fetch('http://localhost:8021/')
        // console.log(response)
        const datas = await response.json()

        addCardsData(datas)
        addDatas(datas)


    } catch (error) {
        console.error(error)
    }
}

function show (datas){
    let output = ``
    for (let data of datas){
        output += `<div class="data-object">`
        output += `<li>${data.id}</li>`
        output += `<li>${data.created_at}</li>`
        output += `<li>${data.ph_value}</li>`
        output += `<li>${data.tds_value}</li>`
        output += `</div>`
    }
    document.querySelector('div.datas-objects').innerHTML = output
}

function addCardsData(datas){
    let phav = 0
    let tdsav = 0
    let count = Object.keys(datas).length
    
    for (let data of datas){
        phav += data.ph_value
        tdsav += data.tds_value
    }
    phav /= count
    tdsav /= count
    let cards = '' 
    const card_init = '<div class="card-data">', card_end = '</div>'
    cards += card_init + '<h3>Acidez</h3>' + `<p>${phav}</p>` + card_end
    cards += card_init + '<h3>Condutividade</h3>' +`<p>${tdsav}</p>` + card_end

    document.querySelector('div#cards-data').innerHTML = cards
}

function addDatas(datas){
    let infos = ``
    let init = '<div class="data-object">'
    let end = '</div>'
    let info1 = `<p>data.id</p>`
    let info2 = `<p>data.ph_value</p>`
    let info3 = `<p>data.tds_value</p>`
    for (let data of datas){
        info1 +=`<p>${data.id}</p>`
        info2 +=`<p>${data.ph_value}</p>`
        info3 +=`<p>${data.tds_value}</p>`
    }
    info1 = init + info1 + end
    info2 = init + info2 + end
    info3 = init + info3 + end
    infos += info1 + info2 + info3
    document.querySelector('div#datas-objects').innerHTML = infos
}

getContent()