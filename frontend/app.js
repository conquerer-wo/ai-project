const input = document.getElementById('input');
const input1 = document.getElementById('input1');
const input2 = document.getElementById('input2');
const input3 = document.getElementById('input3');
const butt = document.getElementById('butt');
const resu = document.getElementById('resu')
async function api(i, i1, i2, i3, type) {
  const url = `http://127.0.0.1:5000/${type}`;
  const res = await fetch(url, {
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
  });

  const data = await res.json();
  resu.textContent = `the area is approximatly ${data.approx} units`
}

function handleSubmit() {
  const inpu = input.value.trim();
  const inpu1 = input1.value.trim();
  const inpu2 = input2.value.trim();
  const inpu3 = input3.value.trim();
  const button = document.querySelector('input[type="radio"]:checked');

  if (!button) {
    alert("Please select a method (radio button).");
    return;
  }

  api(inpu, inpu1, inpu2, inpu3, button.value);
}

butt.addEventListener('click', handleSubmit);
