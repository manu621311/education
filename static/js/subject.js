var x=document.getElementsByClassName('video');
for(var i of x){
    i.addEventListener('click',function(){        
        var video_link=this.childNodes[1].innerText;
        document.getElementById('video').src=video_link;
    });
}

