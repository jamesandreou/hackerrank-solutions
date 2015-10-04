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
            long []arr = new long[n];
            for (int i = 0; i < n; i++){
                arr[i] = sc.nextLong();
            }
            System.out.println(maxProfit(arr));
        }
    }

    static long maxProfit(long [] arr){
        long total = 0;
        long maxVal = 0;
        for(int i = arr.length - 1; i >= 0; i--){
            maxVal = Math.max(maxVal, arr[i]);
            total += maxVal - arr[i];
        }
        return total;
    }

}