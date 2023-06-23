//13. Roman to Integer


// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000

// For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

// I can be placed before V (5) and X (10) to make 4 and 9. 
// X can be placed before L (50) and C (100) to make 40 and 90. 
// C can be placed before D (500) and M (1000) to make 400 and 900.
// Given a roman numeral, convert it to an integer.



//create anobject that contain symbols and values 


console.log('Question 13. Roman to Integer')


const romanToNum = (s) => {

    //object containing the roman numerals and its values
    const romanNum = {
       "I": 1, 
        "V": 5, 
        "X": 10,
        "L": 50,
        "C": 100, 
        "D": 500, 
        "M": 1000
    }

 let answer = 0;

 //iterate over string 's' and retrieves its value from the 'romanNum' object
 for (let i=0; i<s.length; i++) {

    const currentSymbol = romanNum[s[i]];
    //retrieve the next value in the string 
    const nextSymbol = romanNum[s[i+1]];
  
    //check if the current roman symbol is less than the next symbol's value. If true it represents a subtractive notation
    if (currentSymbol < nextSymbol ){
        //adds the difference between the next symbol and current symbol and increments the variable by 1 
        answer += nextSymbol - currentSymbol;
        i++;
    }
    //if the current symbol is not less than the next symbol's value, there's no subtractive notation so the symbol is just added to the answer
    else{
        answer += currentSymbol;
    }
 }
 console.log(answer)
 return answer
}


console.log(romanToNum("XI"))