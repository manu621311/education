var url='/home/request_live_list';
var count_dict;
var xhttp=new XMLHttpRequest();
var count=0,count1=0,count2=0;
var flag1=0,flag2=0;
var x;
var month = new Array();
month[0] = "January";
month[1] = "February";
month[2] = "March";
month[3] = "April";
month[4] = "May";
month[5] = "June";
month[6] = "July";
month[7] = "August";
month[8] = "September";
month[9] = "October";
month[10] = "November";
month[11] = "December";
xhttp.open('GET',url,true);
xhttp.send();
xhttp.onreadystatechange=function(){
    if(this.readyState==4 && this.status==200){
        count_dict=JSON.parse(this.responseText);
        check(count_dict);
    }
}

function check(count_dict){
    var i,value,left,top,type,mon,day,hr,temp;
    for(i=0;i<count_dict.subject_name.length;i++){
        mon=month[new Date(count_dict.deadline[i]).getMonth()]
        day=(new Date(count_dict.deadline[i]).getDate()).toString();
        temp=new Date(count_dict.deadline[i]).getHours()
        if(temp>12){
            hr=(temp-12).toString()+'pm'
        }else{
            hr=temp.toString()+'am'
        }
        scheduled='Scheduled on '+day+"th "+mon+" "+hr;
        create_div(type="subject",count_dict.subject_name[i],count_dict.deadline[i],identifier='live_subject',left='20px',top='30px'); 
        create_div(type="topic",count_dict.topic_name[i],count_dict.deadline[i],identifier='live_heading',left='20px',top='30px'); 
        create_div(type="schedule",scheduled,count_dict.deadline[i],identifier='live_time',left='20px',top='70px'); 
    }
}


function create_div(type,value,deadline,identifier,left,top){
    var node,parent,value;
    node=document.createElement('div')
    value=document.createTextNode(value)    
    node.appendChild(value)
    node.setAttribute('id',identifier)
    node.style.cssText='left:'+left+';top:'+top;
    if(Date.parse(deadline)-Date.parse(new Date())>300000){
        if(flag1==1){
            parent=document.getElementsByClassName('live_1')
        }else{
            parent=document.getElementsByClassName('live_2')
        }
        count1+=1;
        if(count1==3){
            flag1=1;
        }
    }else{
        if(flag2==1){
            parent=document.getElementsByClassName('live_3')
        }else{
            parent=document.getElementsByClassName('live_4')
        }
        count2+=1;
        if(count2==3){
            flag2=1;
        }
    }
    
    parent[0].appendChild(node);  
}