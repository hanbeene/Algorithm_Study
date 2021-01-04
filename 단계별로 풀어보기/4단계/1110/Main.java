import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int newN = N;
        int count = 0;
        while (true){
            int index1 = newN/10;
            int index2 = newN%10;
            int sum = (index1 + index2)%10;
            newN = Integer.parseInt(Integer.toString(index2)+Integer.toString(sum));
            count++;
            if (N == newN){
                System.out.println(count);
                break;
            }
        }
    }
}
