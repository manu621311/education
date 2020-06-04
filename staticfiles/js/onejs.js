function stringize(c,ll,ul){//function that returns array containing the two strings
    var str1='',str2='',arr=[];
    if(c-2<ll||c+3>ul){//for letters 'a','b','x','y','z'
        if(c+1>ul){
            str1+=String.fromCharCode(c-2);
            str1+=String.fromCharCode(c-1);
            str1+=String.fromCharCode(c);
            str1+=String.fromCharCode(c-25);
            str1+=String.fromCharCode(c-24);
            str2+=String.fromCharCode(c-1);
            str2+=String.fromCharCode(c);
            str2+=String.fromCharCode(c-25);
            str2+=String.fromCharCode(c-24);
            str2+=String.fromCharCode(c-23);            
        }else if(c-1<ll){
            str1+=String.fromCharCode(c+24);
            str1+=String.fromCharCode(c+25);
            str1+=String.fromCharCode(c);
            str1+=String.fromCharCode(c+1);
            str1+=String.fromCharCode(c+2);
            str2+=String.fromCharCode(c+25);
            str2+=String.fromCharCode(c);
            str2+=String.fromCharCode(c+1);
            str2+=String.fromCharCode(c+2);
            str2+=String.fromCharCode(c+3);
        }else if(c+2>ul){
            str1+=String.fromCharCode(c-2);
            str1+=String.fromCharCode(c-1);
            str1+=String.fromCharCode(c);
            str1+=String.fromCharCode(c+1);
            str1+=String.fromCharCode(c-24);
            str2+=String.fromCharCode(c-1);
            str2+=String.fromCharCode(c);
            str2+=String.fromCharCode(c+1);
            str2+=String.fromCharCode(c-24);
            str2+=String.fromCharCode(c-23);
        }else if(c-2<ll){
            str1+=String.fromCharCode(c+24);
            str1+=String.fromCharCode(c-1);
            str1+=String.fromCharCode(c);
            str1+=String.fromCharCode(c+1);
            str1+=String.fromCharCode(c+2);
            str2+=String.fromCharCode(c-1);
            str2+=String.fromCharCode(c);
            str2+=String.fromCharCode(c+1);
            str2+=String.fromCharCode(c+2);
            str2+=String.fromCharCode(c+3);
        }else if(c+3>ul){
            str1+=String.fromCharCode(c-2);
            str1+=String.fromCharCode(c-1);
            str1+=String.fromCharCode(c);
            str1+=String.fromCharCode(c+1);
            str1+=String.fromCharCode(c+2);
            str2+=String.fromCharCode(c-1);
            str2+=String.fromCharCode(c);
            str2+=String.fromCharCode(c+1);
            str2+=String.fromCharCode(c+2);
            str2+=String.fromCharCode(c-23);
        }

    }else{//for cases between c to w
        str1+=String.fromCharCode(c-2);
        str1+=String.fromCharCode(c-1);
        str1+=String.fromCharCode(c);
        str1+=String.fromCharCode(c+1);
        str1+=String.fromCharCode(c+2);
        str2+=String.fromCharCode(c-1);
        str2+=String.fromCharCode(c);
        str2+=String.fromCharCode(c+1);
        str2+=String.fromCharCode(c+2);
        str2+=String.fromCharCode(c+3);
    }
arr.push(str1)
arr.push(str2)
return arr
}
function asdfghjk(str){
    var i,x,json,obj={};
    for(i of str){
        if(i in obj){
            continue;
        }else{
            if(i == i.toUpperCase()){
                x=stringize(i.charCodeAt(0),65,90);//to get array containing the two strings
            }else{
                x=stringize(i.charCodeAt(0),97,122);//to get array containing the two strings
            }
        }
        obj[i]=x;
    }
    json=JSON.stringify(obj);
    console.log(json)
}

asdfghjk('yxb');
