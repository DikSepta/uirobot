let counter = 0;

//set timer to update robot position every 500 ms
setInterval(function(){
    let xhr = new XMLHttpRequest();
    
    xhr.onreadystatechange = function(){
        if(this.readyState == 4 && this.status==200) {
            var position = JSON.parse(this.responseText); 

            var canvas = document.getElementById("map_canvas");
            var ctx = canvas.getContext("2d");
            //load image
            var map_img = document.getElementById("id_map_image");

            //clear canvas drawing
            ctx.clearRect(0,0,canvas.width,canvas.height);

            //draw map
            ctx.drawImage(map_img, 0, 0);

            //draw position
            ctx.arc(position.position_x, position.position_y, 10, 0, 2 * Math.PI);
            ctx.stroke();
            ctx.fillStyle = 'red';
            ctx.fill();
        } 
    }

    xhr.open('GET','http://127.0.0.1:8000/get-position/', true);
    xhr.send();
},500);

