
function getSnapshotsTime(array){
    let labels = []
    for (let item of array){
        labels.push(item.time)
    }
    return labels
}

function getSnapshotsExp(array){
    let data = []
    for (let item of array){
        data.push(item.character_info.experience)
    }
    return data
}

function getTimeAndExp(array){
    let time = []
    let exp = []
    for (let item of array){
        let d = new Date(item.time)
        time.push(d.toLocaleString('en-GB', {day: 'numeric', month: 'short'}))
        exp.push(item.character_info.experience)
    }
    let data = [time, exp]
    return data
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

export {getTimeAndExp}
export {numberWithCommas}