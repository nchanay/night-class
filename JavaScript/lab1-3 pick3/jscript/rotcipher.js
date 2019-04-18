// ROT cipher lab done in JavaScrit

const displayRotcipherDiv = document.querySelector('#display-rotcipher')
const rotcipherDiv = document.querySelector('#encryptbtn')
const phraseDiv = document.getElementById("phrase")
const shiftDiv = document.getElementById("shift")

const updateDisplayRotcipher = (value) => {
  displayRotcipherDiv.innerText = value
}

let characters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

function encrypt(string, shift){
  let arry1 = []
  let shiftn = (shift % 26)
  const translate = characters.slice(shiftn*2, characters.length) + characters.slice(0 ,shiftn*2)
  for (let char of string) {
    if (characters.indexOf(char) > -1) {
      arry1.push(translate[characters.indexOf(char)])
    }
    else {
      arry1.push(char)
    }
  }
  return arry1.join('')
}

rotcipherDiv.addEventListener('click', () => {
  updateDisplayRotcipher(encrypt(phraseDiv.value, shiftDiv.value))
})

document.addEventListener('keyup', (evt) => {
  if (evt.key === 'Enter') {
    if (evt.target === rotcipherDiv || evt.target === shiftDiv || evt.target === phraseDiv) {
      updateDisplayRotcipher(encrypt(phraseDiv.value, shiftDiv.value))
    }
  }
})
