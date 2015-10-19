// hackerrank - Algorithms: Alternating Characters
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
            if(word.length() == 1){
                System.out.println(0);
            }else{
                int nDeletes = 0;
                for(int i = 1; i < word.length(); i++){
                    if(word.charAt(i) == word.charAt(i-1)){
                        nDeletes ++;
                    }
                }
                System.out.println(nDeletes);
            }
        }
    }

}