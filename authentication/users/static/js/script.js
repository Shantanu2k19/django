document.addEventListener('DOMContentLoaded', () => 
            {
                document.querySelector('#submit').disabled = true;

                //Enable button only when key-up, text is entered
                //also check if the length of entered string is 0, bcs erasing the text will enable submit button
                document.querySelector('#username').onkeyup = () => {
                	if(document.querySelector('#username').value.length > 1){
                        document.getElementById("user_check").style.color = "green";
                    }
                	else{
                        document.getElementById("user_check").style.color = "red";
                    }
                };

                document.querySelector('#pass1').onkeyup = () => {
                	if(document.querySelector('#pass1').value.length > 1){
                        document.getElementById("pass1_check").style.color = "green";
                    }
                	else{
                        document.getElementById("user_check").style.color = "red";
                    }
                };

                document.querySelector('#pass2').onkeyup = () => {
                	if(document.querySelector('#pass2').value.length > 1){
                        if(document.querySelector('#pass1').value == document.querySelector('#pass2').value){
                            document.getElementById("advice").innerHTML = "passwords matched &#10004";
                            document.getElementById("pass2_check").style.color = "green";
                            document.querySelector('#submit').disabled = false;
                        }
                        else{
                            document.getElementById("advice").innerHTML = "passwords should be same";
                            document.getElementById("pass2_check").style.color = "red";
                            document.querySelector('#submit').disabled = true;
                        }
                    }
                	else{
                        document.getElementById("user_check").style.color = "red";
                    }
                };

                /*
                document.querySelector('#new-task').onsubmit = () => 
                {

                    // Create new item for list, take value from #task
                    const li = document.createElement('li');
                    li.innerHTML = document.querySelector('#task').value;

                    // Add new item to task list
                    document.querySelector('#tasks').append(li);

                    // Clear input field
                    document.querySelector('#task').value = '';

                    //after clearing, disable the button again
                    document.querySelector('#submit').disabled = true;

                    // Stop form from submitting(reloading the page), hence the task will not get erased
                    return false;
                };
                */

});
