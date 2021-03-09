import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] A = new int[N];
        for(int i=0; i<N; i++){
            A[i] = scanner.nextInt();
        }
        int max = -1000000;
        int min = 1000000;
        for(int i=0; i<N; i++){
            if(A[i] > max){
                max = A[i];
            }
            if(A[i] < min){
                min = A[i];
            }
        }
        System.out.print(min+" "+max);
    }
}
