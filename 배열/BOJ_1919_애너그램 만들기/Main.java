import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String s1, s2;
        Scanner sc = new Scanner(System.in);
        s1 = sc.nextLine();
        s2 = sc.nextLine();
        
        int[] alphabet_count = new int[26];
        for (int i=0; i < s1.length(); i++) {
            alphabet_count[s1.charAt(i) - 'a']++;
        }
        for (int i=0; i < s2.length(); i++) {
            alphabet_count[(int)s2.charAt(i) - 'a']--;
        }
        int sum = 0;
        for (int count : alphabet_count) {
            sum += Math.abs(count);
        }
        System.out.print(sum);
    }
}