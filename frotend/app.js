const input = document.getElementById('input');
const input1 = document.getElementById('input1');
const input2 = document.getElementById('input2');
const input3 = document.getElementById('input3');
const form = document.getElementById('form')
const left = document.getElementById('left');
const right = document.getElementById('right');
const center = document.getElementById('center');
const trapezoid = document.getElementById('trapezoid');
const butt = document.getElementById('butt')
async function api(i,i1,i2,i3,type) { url = `http://127.0.0.1:5000/${type}`
    res = await fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    expr: i,
    a: i1,
    b: i2,
    n: i3
  })
})
data = await res.json()
console.log(data.approx)

  

    
}
function res() {inpu = input.value.trim()
inpu1 = input1.value.trim()
inpu2 = input2.value.trim()
inpu3 = input3.value.trim()

}