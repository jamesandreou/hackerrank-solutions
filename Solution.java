// hackerrank - Algorithms: Coin Change
// Written by James Andreou, University of Waterloo
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int [] coins;
    static int [][] memo;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        coins = new int[m];
        memo = new int[n+1][m+1];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                memo[i][j] = 0;
            }
        }
        for(int i = 0; i < m; i++){
            coins[i] = sc.nextInt();
        }
        System.out.println(coinChange(n, m-1));
    }

    //implement memo if too slow
    static int coinChange(int n, int m){
        if(n < 0 || m < 0){
            return 0;
        } 
        if(n == 0){
            memo[n][m] = 1; 
            return 1;
        }
        int ret1, ret2;
        if(memo[n][m-1] != 0){
            ret1 = memo[n][m-1];
        }else{
            ret1 = coinChange(n, m-1);
        }
        if(n-coins[m] > 0 && memo[n - coins[m]][m] != 0){
            ret2 = memo[n - coins[m]][m];
        }else{
            ret2 = coinChange(n - coins[m], m);
        }
        return ret1 + ret2;
    }


}