//Sock Sorter in JavaScript
const sockTypes = ['ankle', 'crew', 'calf', 'thigh'];
const sockColors = ['black', 'white', 'blue'];
const sockList = [];
const sockCounter = {};

for (let i=0; i<100; i++) {
    let sock = sockTypes[Math.floor(Match.random() * sockTypes.length)];
    let color = sockColors[Math.floor(Match.random() * sockColors.length)];
    let sock = [type, color];
    sockList.push(sock);

    sockCounter[sock] = (sockCounter[sock] || 0) + 1;

    // if (sockCounter.hasOwnProperty(sock)) {
    //     sockCounter[sock] += 1;
    // } else {
    //     sockCounter[sock] = 1;
    // }
}

for (let sock in sockCounter) {
    console.log(`${sock} has ${sockCounter[sock % 2]} loner(s).`);
}
