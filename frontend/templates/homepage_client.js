document.addEventListener("DOMContentLoaded", function () {
    
    document.querySelector('form').onsubmit = function () {
        
        // Checking for blank submission.
        let blank_submit = document.querySelector('#input-text-box').value

        if (blank_submit == "" || blank_submit == null) {  //Blank submit check.
            alert("Blank Submission was made")
        }
        else if(/^\s*$/.test(blank_submit)) {   // Blank Lines Check.
            alert("Blank Submission was made")
        }
        
        else {
            // Capute user input.
            let user_input = document.querySelector("#input-text-box").value;
            console.log(user_input)

            // POST to server.
            const data = { "user_input": user_input };

            fetch('/report' , {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                    // Server Response.
                    scores = data["scores"]
                    stats = data["stats"]

                    // Readability.
                    document.querySelector('#remark').innerHTML = scores["remark"]

                    //FRES.
                    document.querySelector('#fres').innerHTML = scores["fres"]

                    // Grade Score.
                    document.querySelector("#grade").innerHTML = scores["grade_score"]

                    // Statistics.
                    document.querySelector("#word_count").innerHTML = stats["total_words"]
                    document.querySelector("#sentence_count").innerHTML = stats["total_sentences"]
                    document.querySelector("#syllable_count").innerHTML = stats["total_syllables"]
                })
                .catch((error) => {
                    console.error('Error:', error);
                });

            // Report Animation.
            document.querySelector('.report').style.display = "block";
            gsap.to('.text', 
                    {duration: 1, 
                    stagger: 0.25, 
                    ease: "power2.out", 
                    y: '0%'} )

            return false;
        }
    }
      
    // Report Window Close Button.
    document.querySelector('#close-button').onclick = function () {
        document.querySelector('.report').style.display = "none";
        document.querySelector('#input-text-box').value = "";

        // Setting the syle back.
        gsap.to('.text', {'y':'100%'})
        return false;
    }
})