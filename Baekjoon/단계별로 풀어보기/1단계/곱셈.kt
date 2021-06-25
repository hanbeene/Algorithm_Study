import java.util.*

fun main(args: Array<String>) {
    val sc: Scanner = Scanner(System.`in`);
    var A = sc.nextInt();
    var B = sc.nextInt();

    println(A * (B % 10));
    println(A * ((B % 100) / 10));
    println(A * (B / 100));
    println(A * B);
}