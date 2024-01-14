// 문자열 자르기는 substr 혹은 slice 사용하기
function solution(my_string, overwrite_string, s) {
    // substr: (시작위치, 길이)
    let overwrite_len = overwrite_string.length;
    let answer = my_string.substr(0,s) + overwrite_string + my_string.substr(s+overwrite_len);
    
    // slice: (시작위치, 종료위치)
    let end = s + overwrite_string.length;
    let answer = my_string.slice(0, s) + overwrite_string + my_string.slice(end)
    
    return answer;
}