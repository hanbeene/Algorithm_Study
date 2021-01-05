import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] A = new int[10];
        for(int i=0; i<9; i++){
            A[i] = scanner.nextInt();
        }
        int max = 0;
        int count = 0;
        for(int i=0; i<10; i++){
            if(A[i] > max){
                max = A[i];
                count = i+1;
            }
        }
        System.out.println(max);
        System.out.println(count);
    }
}
