//functions
fodase = () => {
    alert("Hello World diferenciado")
}
drawRect = (x1,y1,x2,y2) => {
    canvas = document.getElementById("canvas")
    ctx = canvas.getContext("2d")
    ctx.lineWidth = 1
    ctx.beginPath()
    ctx.strokeRect(x1,y1,Math.abs(x1-x2),Math.abs(y1-y2))
    ctx.stroke()
}
clearAll = () => {
    canvas = document.getElementById("canvas")
    ctx = canvas.getContext("2d")
    ctx.clearRect(0,0,canvas.width,canvas.height)
}    
updateCanvas(rects => {
    clearAll()
    rects.map(a => {
        drawRect(a[0],a[1],a[2],a[3])
    })
})

