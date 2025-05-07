import java.util.*;

public class gcd{
    public static void main( String args[]){
    Scanner sc= new  Scanner(System.in);          
    System.out.println("welcome to the GCD !!");
    System.out.println("enter the first number a :");
    int a=sc.nextInt();
    System.out.println("enter the second number b: ");
    int b=sc.nextInt();
    int r=1;
    int q=0; 
     int temp=0;

    if(a%b!=0){
        while(r!=0){
           temp=r;
            r=a%b;
            a=b;
            b=r;
      
        }
        System.out.println("GCD IS :"+temp);
    }else{
        System.out.print("GCD :"+b);
    }
  }
 }