import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        int zero = 0, one = 0, two = 0, three = 0, four = 0, five = 0, six = 0, seven = 0, eight = 0, nine = 0, ten = 0;
        String sum = Integer.toString(A*B*C);
        for(int i = 0; i<sum.length(); i++){
            if(sum.charAt(i) == '0'){
                zero++;
            }
            else if(sum.charAt(i) == '1'){
                one++;
            }
            else if(sum.charAt(i) == '2'){
                two++;
            }
            else if(sum.charAt(i) == '3'){
                three++;
            }
            else if(sum.charAt(i) == '4'){
                four++;
            }
            else if(sum.charAt(i) == '5'){
                five++;
            }
            else if(sum.charAt(i) == '6'){
                six++;
            }
            else if(sum.charAt(i) == '7'){
                seven++;
            }
            else if(sum.charAt(i) == '8'){
                eight++;
            }
            else if(sum.charAt(i) == '9'){
                nine++;
            }
        }
        System.out.println(zero);
        System.out.println(one);
        System.out.println(two);
        System.out.println(three);
        System.out.println(four);
        System.out.println(five);
        System.out.println(six);
        System.out.println(seven);
        System.out.println(eight);
        System.out.println(nine);
    }
}
