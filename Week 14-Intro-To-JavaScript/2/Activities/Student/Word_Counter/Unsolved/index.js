// function countWords(string){
//     var words{};
// var wordarray=string.split(" ")
//     if("words" in words){
//         words[word]+=1
//     }
// }

function count(str){
    var obj={};
    str.split(" ").forEach(function(element,i,array){
      obj[element]=  obj[element]? ++obj[element]: 1;
    });
    return obj;
   }
   console.log(count("olly olly in come free"));