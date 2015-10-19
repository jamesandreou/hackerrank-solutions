// hackerrank - Algorithms: Pangrams
// Written by James Andreou, University of Waterloo
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        int [] alphabet = new int[128];
        for(int i = 0; i < word.length(); i++){
            alphabet[word.charAt(i)] = 1;
        }
        int asciDif = 'a' - 'A';
        boolean isPangram = true;
        for(int i = 'A'; i <= 'Z'; i++){
            if(alphabet[i] != 1 && alphabet[i+asciDif] != 1){
                isPangram = false;
                break;
            }
        }
        if(isPangram){
            System.out.println("pangram");
        }else{
            System.out.println("not pangram");
        }
    }

}