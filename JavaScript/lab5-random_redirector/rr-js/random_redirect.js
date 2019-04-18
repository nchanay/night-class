// Querey selector for button
const ranDiv = document.querySelector('#urlbtn')

// Array of URLs
urlArray = [
  "http://www.zoomquilt.org/",
  "http://www.nooooooooooooooo.com/",
  "http://www.cat-bounce.com/",
  "http://www.pointerpointer.com/",
  "http://www.bristlr.com/",
  "http://www.flightradar24.com/",
  "http://www.snapbubbles.com/",
  "http://www.htwins.net/scale2/",
  "http://www.sanger.dk/",
  "http://www.patience-is-a-virtue.org/",
  "http://www.rainymood.com/",
  "http://www.wwwdotcom.com/",
]

// Click event for button
ranDiv.addEventListener('click', () => {
  let randomURL = urlArray[Math.floor(Math.random() * urlArray.length)];
  window.open(randomURL, "ifra")
})
