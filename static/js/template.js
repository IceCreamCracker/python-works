
//functions

//canvas management
drawRect = (x1,y1,x2,y2) => {
    canvas = document.getElementById("canvas")
    ctx = canvas.getContext("2d")
    ctx.beginPath()
    ctx.strokeRect(0,0,20,20)

    ctx.lineWidth = 1
    ctx.strokeRect(x1,y1,Math.abs(x1-x2),Math.abs(y1-y2))
}
clearAll = () => {
    canvas = document.getElementById("canvas")
    ctx = canvas.getContext("2d")
    ctx.clearRect(0,0,canvas.width,canvas.height)
}    
updateCanvas = (rects => {
    clearAll()
    rects.map(a => {
        drawRect(a[0],a[1],a[2],a[3])
    })
})

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
            $("#x1").html(`${res["x1"]}`)
            $("#x2").html(`${res["x2"]}`)
            $("#y1").html(`${res["y1"]}`)
            $("#y2").html(`${res["y2"]}`)
            
        }
    })
        // .done((res)=>{
        // console.log("foi")
        // console.log(res)
    // })
}
