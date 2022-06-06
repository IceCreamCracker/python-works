
//functions

//canvas management
drawRect = (x1,y1,x2,y2) => {
    canvas = document.getElementById("canvas")
    ctx = canvas.getContext("2d")
    ctx.beginPath()
    //ctx.strokeRect(0,0,20,20)

    ctx.lineWidth = 1
    ctx.fillStyle = "green"
    ctx.fillRect(x1,y2,Math.abs(x1-x2),Math.abs(y1-y2))
}

clearAll = () => {
    canvas = document.getElementById("canvas")
    ctx = canvas.getContext("2d")
    ctx.clearRect(0,0,canvas.width,canvas.height)
}    

updateCanvas = (rects => {
    clearAll()
    rects.map(a => {
        drawRect(
            a["start"]["x"],
            a["start"]["y"],
            a["end"]["x"],
            a["end"]["y"]
        )
    })
})


//coords management
updateCoordList = (rects =>{
    $(".coordList").html("")
    rects.map(r => {
        $(".coordList").append(`
            (${r["start"]["x"]},${r["start"]["y"]}) (${r["end"]["x"]},${r["end"]["y"]})</br>
        `)
    })
})
updateNumOfCoords = (rects) => {
    $("#qtd").html(`${rects.length}`)
}


//API REQUESTS
reqRect = (x1,y1,x2,y2) => {
    $.ajax({
        url:"http://127.0.0.1:5000/api",
        method:"get",
        data: {
            x1:x1,
            y1:y1,
            x2:x2,
            y2:y2
        },

        success: (res)=>{
            updateCoordList(res)
            updateCanvas(res)
            updateNumOfCoords(res)
        }
    })
}
delRects = () => {
    $.ajax({
        url:"http://127.0.0.1:5000/delete",
        type:"get",
        success:document.location.reload()
    })
}
