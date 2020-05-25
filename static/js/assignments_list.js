var block=['block_1','block_2','block_3','block_4'];
var url='/home/request_assign_count';
var count_dict;
var xhttp=new XMLHttpRequest();
var count=0;
xhttp.open('GET',url,true);
xhttp.send();
xhttp.onreadystatechange=function(){
    if(this.readyState==4 && this.status==200){
        count_dict=JSON.parse(this.responseText);
        check(count_dict);
        console.log(count_dict)
    }
}

function check(count_dict){
    var i;
    for(i=0;i<4;i++){
        check_deadline(count_dict.subject_name[i],count_dict.deadline[i],count_dict.status[i],count_dict.video_count[i],count_dict.reading_count[i]); 
    }
}

function check_deadline(subject,deadline,status,video_count,reading_count){
    var x,node1,value1,node2,value2;
    node1=document.createElement('p');
    node2=document.createElement('p');
    node1.setAttribute('id','heading');  
    node2.setAttribute('id','detail');  
    value1=document.createTextNode(subject);
    value2=document.createTextNode(video_count+' Videos '+reading_count+' Reading');
    if(status==2){
        if(Date.parse(deadline)-Date.parse(new Date())>864000000){
            x=document.getElementsByClassName('block_4')
            x[0].style.background='transparent linear-gradient(132deg, #2375D3 0%, #3BA9FE 100%) 0% 0% no-repeat padding-box';
            node1.style.cssText='top: 584px;left: 968px;';
            node2.style.cssText='top: 627px;left: 968px;'
        }else{
            x=document.getElementsByClassName('block_1');
            x[0].style.background='transparent linear-gradient(131deg, #CB2D3E 0%, #EF473A 100%) 0% 0% no-repeat padding-box';
            node1.style.cssText='top: 358px;left: 531px';
            node2.style.cssText='top: 401px;left: 531px;'
        }
    }else{
        if(count==0){
            x=document.getElementsByClassName('block_2');
            x[0].style.background='transparent linear-gradient(122deg, #1D976C 0%, #9DD138 100%) 0% 0% no-repeat padding-box';
            node1.style.cssText='top: 358px;left: 968px;';
            node2.style.cssText='top: 401px;left: 968px;'
        }else{
            x=document.getElementsByClassName('block_3');
            x[0].style.background='transparent linear-gradient(122deg, #1D976C 0%, #9DD138 100%) 0% 0% no-repeat padding-box';
            node1.style.cssText='top: 676px;left: 531px;';
            node2.style.cssText='top: 719px;left: 531px;'
        }
        count=count+1;
    }
    node1.appendChild(value1);
    document.body.append(node1);
    node2.appendChild(value2)
    document.body.append(node2)
}
