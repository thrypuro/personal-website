random_djinn()
              function random_djinn(){
               var djinni = ["Djinn.gif","Mars.gif","Mercury.gif","Jupiter.gif"];
               var num = Math.floor(Math.random()*4);
               document.getElementById("djini").src ="oldsite/"+ djinni[num];
            
            }
            function hi(text1){
                document.getElementById("desc").innerHTML = text1;
            }
            function fun(a){var b = "";for (let i=0; i<a.length;i++){if(a[i]%2!=0){b+=(String.fromCharCode(a[i]^42));}else{b+=(String.fromCharCode(a[i]^68));}}  return b;}
            function flee(){
                var num = Math.floor(Math.random()*100);
                /* I see you're curious ;)*/
                if(num==69){
                  var ch = [44, 48, 48, 52, 89, 126, 5, 5, 83, 69, 95, 48, 95, 106, 38, 79, 5, 32, 123, 93, 112, 93, 19, 125, 77, 28, 73, 123];
                  var ct = [32, 75, 71, 81, 32, 75, 48, 117, 93, 75, 89, 117, 79, 62, 87];
                  var t = fun(ch);
                  document.getElementById("Flee").href = t; }
                else{
                    alert("You ran away!");
                }
                
            }
            var ina = document.getElementById("insap");
            
            
            function inspa(){
               document.getElementById("insap").style.display = "block";
            }
            window.onclick = function(event) {
                if (event.target == ina) {
                    ina.style.display = "none";
                    }
                 }
                 function hide(){
                    document.getElementById("hia").style.display = "block";
                    document.getElementById("hnav").style.display = "none";   
               }
               function unhide(){
                   document.getElementById("hia").style.display = "none";
                    document.getElementById("hnav").style.display = "block";   
       
               }