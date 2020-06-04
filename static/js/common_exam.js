var url='/home/apiviews/queans';
var xhttp=new XMLHttpRequest();
var option=['A','B','C','D']
xhttp.open('GET',url,true);
xhttp.send();
xhttp.onreadystatechange=function(){
    if(this.readyState==4 && this.status==200){
        var dict=JSON.parse(this.responseText);
    }
}
/*function qnum(parent,num,question){
    var qnum=document.createElement('div')
    qnum.setAttribute('class','questnum')
    var textnode=document.createTextNode('Question'+' '+num.toString())
    qnum.appendChild(textnode)
    parent.appendChild(qnum)
    var quest=document.createElement('div')
    quest.setAttribute('class','question')
    var textnode=document.createTextNode(question)
    quest.appendChild(textnode)
    parent.appendChild(quest)
}
function create_div(queobj,parent,num){
    var i;
    var qcont=document.createElement('div')
    parent.appendChild(qcont)
    qnum(qcont,num,queobj['question'])//for 5 questions
    for(i=0;i<4;i++){//for 4 options
        var anscont=document.createElement('div')//container for answer options
        anscont.setAttribute('class','opt_container')
        parent.appendChild(anscont)
        answer_option(anscont,queobj['answer'],i)
    }
}
function place_questions(arr){
    var i,parent;
    parent=document.getElementById('parent');
    for(i=0;i<5;i++){//For 5 question objects
        var queobj=arr[i];
        var contanier=document.createElement('div')//container for a complete question
        contanier.setAttribute('class','col-q-7')
        contanier.classList.add('q_container')
        parent.appendChild(contanier)
        create_div(queobj,contanier,i+1);
    }
}


function pick_questions(dict){
    var arr=[];
    for(var i=0;i<5;i++){
        var index=Math.floor(Math.random()*10)
        arr.push(dict[index])
    }
    console.log(arr[0])
    place_questions(arr)
}


function answer_option(parent,answer_array,index){
    var alphabet=document.createElement('div')
    alphabet.setAttribute('class','alphabet')
    var textnode=document.createTextNode(option[index])
    alphabet.appendChild(textnode)
    parent.appendChild(alphabet)
}*/