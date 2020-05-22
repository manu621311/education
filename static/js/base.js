var heading_row_1=['telugu_text','hindi_text','science_text','biology_text'];
var heading_row_2=['english_text','mathematics_text','social_text','general_text'];
var heading_row=heading_row_1.concat(heading_row_2);
var subject_tiles=['TELUGU','HINDI','SCIENCE','BIOLOGY','ENGLISH','SOCIAL','MATHEMATICS','GENERAL'];
var left=['275','637','1013','1375'];
var exam="{{exam_count}}"

create_node();

function create_node(){
    var i;
    for(i=0;i<8;i++){
        var node=document.createElement('p');
        var value=document.createTextNode(subject_tiles[i]);
        node.appendChild(value);
        node.setAttribute('id',heading_row[i]);
        document.body.append(node);
        
    }
    add_css_1();   
}

function add_css_1(){
    var i,x,y=0;
    for(i of heading_row_1){
        x=document.getElementById([i]);
        console.log(x);
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

