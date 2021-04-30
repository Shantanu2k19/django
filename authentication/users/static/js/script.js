document.addEventListener('DOMContentLoaded', () => 
            {
                document.querySelector('#submit').disabled = true;

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

});
