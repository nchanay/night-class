// Grading lab done in JavaScrit

const displayGradeDiv = document.querySelector('#display-grade')
const gradeDiv = document.querySelector('#grade')
const scoreDiv = document.getElementById("score")

const updateDisplayGrading = (value) => {
  displayGradeDiv.innerText = value
}

function grading(score) {
        let letterGrade = ""
        if (score < 60) {
                letterGrade = "F";
        } else if (score < 70) {
                letterGrade = "D";
        } else if (score < 80) {
                letterGrade = "C";
        } else if (score < 90) {
                letterGrade = "B";
        } else if (score >= 90) {
                letterGrade = "A";
        }

        let onesDigit = (score) => (score % 10);
        let sign = "";
        if (letterGrade !== "F") {
            if (onesDigit(score) <= 3) {
                  sign = "-";
            } else if (onesDigit(score) >= 7) {
                  sign = "+";
            }
        }
        if (score >= 100) {
            sign = "+";
        }
    return (`Grade : ${letterGrade}${sign}`);
}

gradeDiv.addEventListener('click', () => {
  updateDisplayGrading(grading(scoreDiv.value))
})

document.addEventListener('keyup', (evt) => {
  if (evt.key === 'Enter') {
    updateDisplayGrading(grading(scoreDiv.value))
  }
})
