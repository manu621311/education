var block=['block_1','block_2','block_3','block_4'];
var url='/home/request_assign_count';
var count_dict;
var xhttp=new XMLHttpRequest();
var count=0;
var flag=0;
xhttp.open('GET',url,true);
xhttp.send();
xhttp.onreadystatechange=function(){
    if(this.readyState==4 && this.status==200){
        count_dict=JSON.parse(this.responseText);
        check(count_dict);
    }
}
function check_deadline(type,value,deadline,status,id,left,top){
    var x,node,parent;
    node=document.createElement('div')
    if(type!="bar"&&type!='progress_bar'&&type!='comment'&&type!='timer'){
        value=document.createTextNode(value)    
        node.appendChild(value)
    }
    node.setAttribute('id',id)
    node.style.cssText='left:'+left+';top:'+top;
    if(type=="progress_bar"){
        node.style.width=(value*230/100).toString()+"px";
    }
    if(status==2){
        if(Date.parse(deadline)-Date.parse(new Date())>864000000){
            parent=document.getElementsByClassName(block[3]);
            if(type=="bar"){
                node.style.background='#56A2F9  0% 0% no-repeat padding-box';
            }else if(type=="comment"){
                value=document.createTextNode('Looks Good!')
                node.appendChild(value)
            }    
        }else{
            parent=document.getElementsByClassName(block[0]);
            if(type=="bar"){
                node.style.background="#F84F4C 0% 0% no-repeat padding-box"
            }else if(type=="comment"){
                value=document.createTextNode('TIME TO WORK!')
                node.appendChild(value)
            }
        }
    }else{
        if(flag==0){
            parent=document.getElementsByClassName(block[1]);
            if(type=="bar"){
                node.style.background="#80C97E 0% 0% no-repeat padding-box"
            }else if(type=="comment"){
                value=document.createTextNode('Great Job!')
                node.appendChild(value)
            }
        }else{
            parent=document.getElementsByClassName(block[2]);
            if(type=="bar"){
                node.style.background="#80C97E 0% 0% no-repeat padding-box"
            }else if(type=="comment"){
                value=document.createTextNode('Great Job!')
                node.appendChild(value)
            }
        }
        count=count+1;
        if(count==6){
            flag=1;
        }
    }
    parent[0].appendChild(node);  
}
function fortimer(type,deadline,id,left,top){
    var value,node,parent;
    node=document.createElement('div')
    node.setAttribute('id',id)
    if(type=="format"){
        var value=document.createTextNode("Days"+Array(6).fill('\xa0').join('')+'Hours'+Array(7).fill('\xa0').join('')+
        'Min'+Array(7).fill('\xa0').join('')+'Sec'); 
        node.appendChild(value)
    }
    node.style.cssText='left:'+left+';top:'+top;
    if(Date.parse(deadline)-Date.parse(new Date())>864000000){
        parent=document.getElementsByClassName(block[3]);
    }else{
        parent=document.getElementsByClassName(block[0]);
    }
    parent[0].appendChild(node);  
}

function check(count_dict){
    var i,value,left,top,type;
    for(i=0;i<4;i++){
        check_deadline(type="heading",count_dict.subject_name[i],count_dict.deadline[i],count_dict.status[i],id='heading',left='20px',top='20px'); 
        value=count_dict.video_count[i]+' Videos + '+count_dict.reading_count[i]+' Reading';
        check_deadline(type="detail",value,count_dict.deadline[i],count_dict.status[i],id='detail',left='20px',top='30px');
        check_deadline(type="bar",value="",count_dict.deadline[i],count_dict.status[i],id='bar',left='20px',top='50px');
        check_deadline(type="progress_bar",value=count_dict.progress[i],count_dict.deadline[i],count_dict.status[i],id='progress_bar',left='20px',top='37px');
        value=(count_dict.progress[i]).toString()+'%';
        check_deadline(type="progress",value,count_dict.deadline[i],count_dict.status[i],id='progress',left='310px',top='16px');
        check_deadline(type="comment",value="",count_dict.deadline[i],count_dict.status[i],id='comment',left='20px',top='46px');
        /*if(i==0){
            fortimer(type="clock",count_dict.deadline[i],id='timer1',left='100px',top='70px');
            var myVar1=setInterval(myTimer,1000,count_dict.deadline[i],id='timer1')
            fortimer(type="format",count_dict.deadline[i],id='format1',left='100px',top='70px');
        }else if(i==3){
            fortimer(type="clock",count_dict.deadline[i],id='timer4',left='100px',top='70px');
            var myVar2=setInterval(myTimer,1000,count_dict.deadline[i],id='timer4')
            fortimer(type="format",count_dict.deadline[i],id='format4',left='100px',top='70px');
        }*/
    }
}
function myTimer(deadline,id){
    var d=Date.parse(new Date());
    var rem=Date.parse(deadline)-d;
    days=Math.floor(rem/(1000*60*60*24));
    var hours = Math.floor((rem%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
    var minutes = Math.floor((rem % (1000 * 60 * 60)) / (1000 * 60)); 
    var seconds = Math.floor((rem % (1000 * 60)) / 1000); 
    document.getElementById(id).innerText=days+" "+hours+" "+minutes+" "+seconds;
}




