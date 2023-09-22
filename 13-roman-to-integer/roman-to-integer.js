/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(romanStr) {
    valuesOfRoman = {"I":1,"V":5,"X":10,"L":50,"C":100, "D":500, "M": 1000};
        sum = 0;
        romanStr.split('').forEach((ele,index)=>{
                sum += valuesOfRoman[ele] < valuesOfRoman[romanStr[index+1]] ? 
                    -valuesOfRoman[ele]: valuesOfRoman[ele];
        })
        return sum;
};