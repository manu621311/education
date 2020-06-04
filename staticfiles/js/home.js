var heading_row_1=['telugu_text','hindi_text','science_text','biology_text'];
var heading_row_2=['english_text','mathematics_text','social_text','general_text'];
var heading_row=heading_row_1.concat(heading_row_2);
var subject_tiles=['TELUGU','HINDI','SCIENCE','BIOLOGY','ENGLISH','MATHEMATICS','SOCIAL','GENERAL'];
var count_array=['telugu_count','hindi_count','science_count','biology_count','english_count','mathematics_count','social_count','general_count'];
var left=['275','637','1013','1375'];
var more_left=['509','870','1247','1608'];
var bar=['telugu_bar','hindi_bar','science_bar','biology_bar','english_bar','mathematics_bar','social_bar','general'];
var subject_progress=['subject_progress_1','subject_progress_2','subject_progress_3','subject_progress_4','subject_progress_5','subject_\
progress_6','subject_progress_7','subject_progress_8'];
var progress=['progress_1','progress_2','progress_3','progress_4','progress_5','progress_6','progress_7','progress_8'];
var url1='/home/request_count';
var xhttp=new XMLHttpRequest();
xhttp.open('GET',url1,true);
xhttp.send();
xhttp.onreadystatechange=function(){
    if(this.readyState==4 && this.status==200){
        var count_dict=JSON.parse(this.responseText);
        create_node(count_dict);
    }
}

function connect_nodes(flag,id_array,value_array,tag){
    var i;
        for(i=0;i<8;i++){
            var node=document.createElement(tag);
            if(value_array!="" && flag!="subject_progress"){
                if(flag=="detail"){
                    var value=document.createTextNode(value_array.video_count[i]+" \
                    Videos - "+value_array.exam_count[i]+" Exams - "+value_array.subject_count[i]+" Subjects");
                }else if(flag=="progress"){
                    var value=document.createTextNode(value_array.progress[i]+"%");
                    node.setAttribute('class',progress[i]);
                }else{
                    var value=document.createTextNode(value_array[i]);
                }
                node.appendChild(value);
            }
            if(flag=="subject_progress"){
                node.setAttribute('class',id_array[i]);
                node.style.width=(value_array.progress[i]*124/100).toString() +"px";
                node.style.height="15px";
            }if(flag!="progress"){
                node.setAttribute('id',id_array[i]);
            }
            document.body.append(node);
        }
}

function create_node(count_dict){
    var flag="",tag="",position="";
    connect_nodes(flag="heading",heading_row,subject_tiles,tag="p");
    connect_nodes(flag="detail",count_array,count_dict,tag="p");  
    connect_nodes(flag="bar",bar,"",tag="div");
    connect_nodes(flag="subject_progress",subject_progress,count_dict,tag="div");
    connect_nodes(flag="progress",progress,count_dict,tag="p");
    add_css_3(flag="id",position="left",count_array); 
    add_css_3(flag="class",position="left",subject_progress);
    add_css_3(flag="class",position="more_left",progress);
    add_css_1();   
}

function add_css_1(){
    var i,x,y=0;
    for(i of heading_row_1){
        x=document.getElementById([i]);
        x.style.top='415px';
        x.style.left=left[y]+'px';
        y=y+1;
    }
    add_css_2();    
}

function add_css_2(){
    var i,x,y=0;
    for(i of heading_row_2){
        x=document.getElementById(i);
        x.style.top='655px';
        x.style.left=left[y]+'px';
        y=y+1;
    }
}

function add_css_3(flag,position,arr){
    var i,x,y=0;
    for(i=0;i<8;i++){
        if(flag=="id"){
            x=document.getElementById(arr[i]);
            if(i%2==0){
                if(i>=4){
                    x.style.top='711px';
                }else{
                    x.style.top='471px';
                }
                
            }else{
                if(i>=4){
                    x.style.top='711px';
                }else{
                    x.style.top='471px';
                }
            }
        }else{
            x=document.getElementsByClassName(arr[i])[0];
            if(i%2==0){
                if(i>=4){
                    x.style.top='760px';
                }else{
                    x.style.top='518px';
                }
                
            }else{
                if(i>=4){
                    x.style.top='760px';
                }else{
                    x.style.top='518px';
                }
            }
        }
        if(position=="more_left"){
            x.style.left=more_left[y]+'px'
            if(i==3){
                y=0;
            }else{
                y=y+1;
            }
        }else{
            x.style.left=left[y]+'px'
            if(i==3){
                y=0;
            }else{
                y=y+1;
            }
        }
    }
}
