// hackerrank - Algorithms: The Maximum Subarray
// Written by James Andreou, University of Waterloo
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int nTests = sc.nextInt();
        for (int t = 0; t < nTests; t++){
            int n = sc.nextInt();
            int []arr = new int[n];
            for (int i = 0; i < n; i++){
                arr[i] = sc.nextInt();
            }
            System.out.println(contMax(arr) + " " + nonContMax(arr));
        }
    }

    static int contMax(int [] arr){
        int curMax = 0;
        int lastMax = 0;
        int maxNeg = Integer.MIN_VALUE;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] <= 0 && arr[i] > maxNeg) maxNeg = arr[i];
            lastMax = lastMax + arr[i];
            if(lastMax < 0) lastMax = 0;
            if(curMax < lastMax) curMax = lastMax;
        }
        return (curMax > 0) ? curMax : maxNeg;
    }

    static int nonContMax(int [] arr){
        int max = 0;
        int maxNeg = Integer.MIN_VALUE;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] > 0){
                max += arr[i];
            }else if(arr[i] > maxNeg){
                maxNeg = arr[i];
            }
        }
        return (max > 0) ? max : maxNeg;
    }
}