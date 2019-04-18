// Make Change in JavaScript

const displayChangeDiv = document.querySelector('#display-change')
const changeDiv = document.querySelector('#changebtn')
const moneyDiv = document.getElementById("money")

const updateDisplayChange = (value) => {
  displayChangeDiv.innerText = value
}

function makeChange(money) {
  let userMoney = Math.round(parseFloat(money) * 100);

  let quarters = Math.floor(userMoney / 25)
  userMoney %= 25

  let dimes = Math.floor(userMoney / 10)
  userMoney %= 10

  let nickles = Math.floor(userMoney / 5)
  userMoney %= 5

  return (`Your change is:\n${quarters} quarter(s)\n${dimes} dime(s)\n${nickles} nickle(s)\n${userMoney} pennie(s)`)
}

changeDiv.addEventListener('click', () => {
  updateDisplayChange(makeChange(moneyDiv.value))
})

document.addEventListener('keyup', (evt) => {
  if (evt.key === 'Enter') {
    updateDisplayChange(makeChange(moneyDiv.value))
  }
})
