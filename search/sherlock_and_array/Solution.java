// hackerrank - Algorithms: Sherlock and Array
// Written by James Andreou, University of Waterloo

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t > 0){
            int n = sc.nextInt();
            int[] a = new int[n];
            for(int i = 0; i < n; i++){
                a[i] = sc.nextInt();
            }
            System.out.println(isSherlock(a, n));
            t--;
        }
    }
    
    static String isSherlock(int[] a, int n){
        int[] leftSums = new int[n];
        int[] rightSums = new int[n];
        // find left and right sums O(n)
        leftSums[0] = 0;
        for(int i = 1; i < n; i++){
            leftSums[i] = leftSums[i-1] + a[i-1];
        }
        rightSums[n-1] = 0;
        for(int i = n-2; i >= 0; i--){
            rightSums[i] = rightSums[i+1] + a[i+1];
        }
        // check each i O(n)
        for(int i = 0; i < n; i++){
            if(leftSums[i] == rightSums[i]){
                return "YES";
            }
        }
        return "NO";
    }
}
