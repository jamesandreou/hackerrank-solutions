// hackerrank - Algorithms: Palindrome Index
// Written by James Andreou, University of Waterloo
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int nTests = sc.nextInt();
        String word = sc.nextLine();
        for(int t = 0; t < nTests; t++){
            word = sc.nextLine();
            Map <Character, Integer> alphabet = new HashMap <Character, Integer>();
            for(int i = 0; i < word.length(); i++){
                if(alphabet.containsKey(word.charAt(i))){
                    alphabet.put(word.charAt(i), 
                        alphabet.get(word.charAt(i)) + 1);
                }else{
                    alphabet.put(word.charAt(i), 1);
                }
            }
            Iterator it = alphabet.keySet().iterator();
            int indexToRem = -1;
            while (it.hasNext() && indexToRem == -1) {
                char key = (char) it.next();
                if(alphabet.get(key) % 2 != 0){
                    int l = 0;
                    int r = word.length() -1;
                    while (l<= r){
                        if(word.charAt(l) == key &&
                          word.charAt(l) != word.charAt(word.length() - l - 1)){
                            indexToRem = l;
                            break;
                        }else if(word.charAt(r) == key &&
                          word.charAt(r) != word.charAt(word.length() - r - 1)){
                            indexToRem = r;
                            break;
                        }
                        l++;
                        r--;
                    }
                }
                it.remove();
            }
            System.out.println(indexToRem);
        }
    }

}